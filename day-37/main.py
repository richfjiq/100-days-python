import requests
from datetime import datetime

USERNAME = "rfjiq86"
TOKEN = "sdfmgeterioter4385893"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}


# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

GRAPH_ID = "graph1"

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
pixel_creation_endpoint = f"{graph_endpoint}/{GRAPH_ID}"
update_pixel_endpoint = f"{pixel_creation_endpoint}"

graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai",
}

headers = {"X-USER-TOKEN": TOKEN}

today = datetime(year=2023, month=9, day=5)

pixel_data = {"date": today.strftime("%Y%m%d"), "quantity": "9.85"}

update_pixel_endpoint = f"{pixel_creation_endpoint}/{today.strftime('%Y%m%d')}"

update_pixel_data = {"quantity": "7.5"}

delete_pixel_endpoint = f"{pixel_creation_endpoint}/{today.strftime('%Y%m%d')}"


# Create a Graph
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)

# Records pixel data in the Graph
# response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)

# Update pixel
# response = requests.put(
#     url=update_pixel_endpoint, json=update_pixel_data, headers=headers
# )

# Delete a pixel
response = requests.delete(url=delete_pixel_endpoint, headers=headers)

print(response.text)
