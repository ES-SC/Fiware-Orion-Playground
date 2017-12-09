# Create a new entity - keyValues mode
# from urllib2 import urlopen
# from urllib2 import Request
import requests
from urllib.request import urlopen
import json


file_json = 'payloadOneEntity.json'
with open(file_json, 'r') as f:
    entitiesDataList = json.load(f)
#Criou um lista de dicionário com os dados do arquivo json

values = (str(entitiesDataList)).replace('\'', '\"')
headers = {
    'Content-Type': 'application/json'
}
binary_values = values.encode('UTF-8')
try:
    request_to_orion = requests.post('http://localhost:1026/v2/entities', data=binary_values, headers=headers)
    status = request_to_orion.status_code
    if status != 201:
        print("Code HTTP: {}".format(request_to_orion.status_code))
        print(request_to_orion.text)
    else:
        print("Entity(ies) created.")

except Exception as e:
    print("Exception found: {}".format(e))


