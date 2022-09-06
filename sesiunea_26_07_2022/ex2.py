import requests
import json

try:
    # 1. Facem requests
    response = requests.get("https://jsonplaceholder.typicode.com/users")
except requests.exceptions.RequestException as err:
    print(err)
else:
    # 2. Verificam status code sa fie 200
    if response.status_code == 200:
        # 3. Extragem datele
        data = response.json()
        

        for i in data:
            print(i["username"])



# sites

# https://developer.mozilla.org/en-US/docs/Web/HTTP/Status
# https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/GET
# https://developer.accuweather.com/packages
# http://dataservice.accuweather.com/locations/v1/cities/search?apikey=&q=Constanta
# http://dataservice.accuweather.com/currentconditions/v1/287719?apikey=
# https://requests.readthedocs.io/en/latest/
# https://jsonplaceholder.typicode.com/comments?postId=1
# https://jsonplaceholder.typicode.com/users