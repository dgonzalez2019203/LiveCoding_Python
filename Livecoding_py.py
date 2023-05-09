import requests
import json

url = "https://api.chucknorris.io/jokes/random"
list = [];
list_json = {};


for i in range(0,24):
    response = requests.get(url)
    if response.status_code == 200:
        list.append(response.json())
    else:
        print("Page not found")
    
print(json.dumps(list))
