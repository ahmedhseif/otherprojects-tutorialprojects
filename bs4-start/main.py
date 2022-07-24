from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
articles = soup.find_all(name="a", class_="product__title")
article_texts = []
article_links = []
for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.get("href")
    article_links.append(link)


article_upvote = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

print(article_texts)
print(article_links)
print(article_upvote)

highest = max(article_upvote)

# idk why (+ 1)
position = article_upvote.index(highest) + 1
print(position)

print(article_texts[position])
print(article_links[position])
print(highest)















# # import lxml
#
# with open("website.html", encoding="utf-8") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")
# all_anchors = soup.find_all(name="a")
# # print(all_anchors)
#
# # for tag in all_anchors:
# #     print(tag.get("href"))
#
# heading = soup.find(name="h1", id="name")
# # print(heading)
#
# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading)
#
# headings = soup.select(".heading")
# print(headings)