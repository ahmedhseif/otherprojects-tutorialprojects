import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
API_KEY_STOCKS = "ZDJGDQSG1PTHD5NL"
API_KEY_NEWS = "e201b6da92974187b6bea36abf40e498"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
account_sid = "ACe6007b4eda72b44cf44f8026f1917be4"
auth_token = "b0e7d9769aa840ed677c76fb4dc58cc3"

PARAMS_STOCKS = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": API_KEY_STOCKS
}

PARAMS_NEWS = {
    "apiKey": API_KEY_NEWS,
    "qInTitle": COMPANY_NAME
}

## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

# TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
response_stocks = requests.get(STOCK_ENDPOINT, params=PARAMS_STOCKS)
response_stocks.raise_for_status()
result = response_stocks.json()["Time Series (Daily)"]
result_items = [value for (key, value) in result.items()]
yesterday = float(result_items[0]["4. close"])

# TODO 2. - Get the day before yesterday's closing stock price
before_yesterday = float(result_items[1]["4. close"])

# TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
# TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
if yesterday - before_yesterday >= 0:
    arrow = "🔺"
else:
    arrow = "🔻"

difference = abs(yesterday - before_yesterday)
percentage = (difference / before_yesterday) * 100
# TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
# TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
# TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
# TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.
if percentage > 5:
    response_news = requests.get(NEWS_ENDPOINT, params=PARAMS_NEWS)
    response_news.raise_for_status()
    messages_list = response_news.json()["articles"][:3]
    titles = [item["title"] for item in messages_list]
    descriptions = [item["description"] for item in messages_list]
    message_1 = f"\n{STOCK_NAME}: {arrow}{percentage}%\nHeadline: {titles[0]} ({STOCK_NAME})?.\nBrief: {descriptions[0]}"
    message_2 = f"\n{STOCK_NAME}: {arrow}{percentage}%\nHeadline: {titles[1]} ({STOCK_NAME})?.\nBrief: {descriptions[1]}"
    message_3 = f"\n{STOCK_NAME}: {arrow}{percentage}%\nHeadline: {titles[2]} ({STOCK_NAME})?.\nBrief: {descriptions[2]}"
    # /// HER WORK /// formatted_articles = [
    #     f"{STOCK_NAME}: {up_down}{diff_percent}%\nHeadline: {article['title']}. \nBrief: {article['description']}" for
    #     article in three_articles]

    client = Client(account_sid, auth_token)
    send_message_1 = client.messages \
        .create(
        body=f"{message_1}",
        from_='+17376373457',
        to='+201096365437'
    )
    send_message_2 = client.messages \
        .create(
        body=f"{message_2}",
        from_='+17376373457',
        to='+201096365437'
    )
    send_message_3 = client.messages \
        .create(
        body=f"{message_3}",
        from_='+17376373457',
        to='+201096365437'
    )

    ## STEP 2: https://newsapi.org/
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    # to send a separate message with each article's title and description to your phone number.

# TODO 9. - Send each article as a separate message via Twilio.


# Optional TODO: Format the message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
