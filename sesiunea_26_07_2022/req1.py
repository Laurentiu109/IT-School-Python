from urllib import response
import requests
import json

try:
    # 1. Facem request
    response = requests.get("https://jsonplaceholder.typicode.com/comments?postID=2")

except requests.exceptions.RequestException as err:
    print(err)
else:
    # 2. Verificam status code sa fie 200
    if response.status_code == 200:
        # data = json.loads(response.content)
        # 3. Extragem datele
        data = response.json()
        print(data)
    else:
        # in cazul in care nu avem raspuns pozitiv
        print(response.content)