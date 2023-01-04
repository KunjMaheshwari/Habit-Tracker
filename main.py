import requests
from datetime import datetime

USERNAME = "kunj"
TOKEN = "qwertyuiopasdf"
pixela_endpoint = "https://pixe.la/v1/users"

parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# respond = requests.post(url=pixela_endpoint, json=parameters)
# print(respond.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_params = {
    "id": "graph1",
    "name": "Coding Graph",
    "unit": "Hours",
    "type": "float",
    "color": "shibafu"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

respond = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
print(respond.text)

pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_params['id']}"
today = datetime.now()


pixel_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many hours did you code today? ")
}

# receive = requests.post(url=pixel_endpoint, json=pixel_params, headers=headers)
# print(receive.text)

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_params['id']}/{today.strftime('%Y%m%d')}"

update_params = {
    "quantity": "3.5",
    "date": today.strftime("%Y%m%d")
}

update = requests.put(url=update_endpoint, json=update_params, headers=headers)
print(update.text)
