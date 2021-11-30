# import requests
# from requests import Response
#
#
# def get_curriculum() -> Response:
#     # url_post = 'http://localhost:8081/usuario'
#     url_get = 'http://localhost:8081/usuario'  # http://localhost:8081/usuario/{email}
#     email = 'teste@gmail.com'
#
#     response = requests.get(url=f'{url_get}/{email}')
#     # data = response.json()['data']
#     # print(type(response))
#     print(response.status_code)
#
#     # with open('file.pdf', 'wb') as file:
#     #     file.write(base64.b64decode(data))
#
#
# get_curriculum()

with open('/home/marcos/Downloads/original.txt', 'r') as file:
    # print(file.read())

    # print()

    with open('/home/marcos/Downloads/new.txt', 'w') as new_file:
        new_file.write(file.read().upper())
