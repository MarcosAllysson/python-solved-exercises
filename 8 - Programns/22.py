import base64
import requests
import json


def get_curriculum():
    url_post = 'http://localhost:8081/usuario'
    url_get = 'http://localhost:8081/usuario/'  # http://localhost:8081/usuario/{email}
    email = 'string@gmail.com'

    response = requests.get(url=url_get + email)
    data = response.json()['data']

    # with open('file.pdf', 'wb') as file:
    #     file.write(base64.b64decode(data))



get_curriculum()
