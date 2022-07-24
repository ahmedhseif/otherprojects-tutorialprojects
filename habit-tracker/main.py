import requests
from datetime import datetime


USERNAME = "ahmedseif98"
TOKEN = "bshidf1basi5fda4bdqw"
pixela_endpoint = "https://pixe.la/v1/users"
graphid = "graph1"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url= pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": graphid,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers= headers)
# print(response.text)

today = datetime(year=2022, month=1, day=28)


pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "25"
}

pixel_endpoint = f"{graph_endpoint}/{graphid}"



# response = requests.post(url=pixel_endpoint, json=pixel_data, headers=headers)
# print(response.text)

# response = requests.delete(url=f"{pixel_endpoint}/{today.strftime('%Y%m%d')}", headers=headers)
# print(response.text)



