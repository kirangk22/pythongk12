url="https://jsonplaceholder.typicode.com/posts"

import requests

res_data=requests.get(url).json()
print(res_data)