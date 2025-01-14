import requests

url="https://pokeapi.co/api/v2/pokemon/pikachu"
# https://jsonplaceholder.typicode.com/posts

response=requests.get(url)
print(response)  # 200 means ok sucess...

response_data=response.json()
print(response_data)  # json data...its dictinary k,v pairs
print("===================================")
print(response_data["name"])
print(response_data["height"])
print(response_data["id"])