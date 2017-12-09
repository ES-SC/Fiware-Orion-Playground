

import requests
from urllib.request import urlopen


try:
    request_to_orion = requests.delete('http://localhost:1026/v2/entities/Room1')
    request_to_orion = requests.delete('http://localhost:1026/v2/entities/Room2')
    request_to_orion = requests.delete('http://localhost:1026/v2/entities/Room3')
    request_to_orion = requests.delete('http://localhost:1026/v2/entities/Room4')
    request_to_orion = requests.delete('http://localhost:1026/v2/entities/Room5')
    request_to_orion = requests.delete('http://localhost:1026/v2/entities/Room6')



    status = request_to_orion.status_code
    CODE_SUCESSFUL = 204
    if status != CODE_SUCESSFUL:
        print("Code HTTP: {}".format(request_to_orion.status_code))
        print(request_to_orion.text)
    else:
        print("Entity(ies) delete.")

except Exception as e:
    print("Exception found: {}".format(e))
    print(e)




