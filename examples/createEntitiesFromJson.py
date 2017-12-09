import requests
import json


file_json = 'payload.json'
with open(file_json, 'r') as f:
    entitiesDataList = json.load(f)

values = """
{
  "actionType": "APPEND",
  "entities":
  """
values = values + (str(entitiesDataList)).replace('\'', '\"')
values = values + "}"
headers = {
    'Content-Type': 'application/json',
}
binary_values = values.encode('UTF-8')
try:
    request_to_orion = requests.post('http://localhost:1026/v2/op/update', data=binary_values, headers=headers)
    status = request_to_orion.status_code
    CODE_SUCESSFUL = {204, 201}
    if status in CODE_SUCESSFUL:
        print("Entity(ies) updated.")
    else:
        print("Code HTTP: {}".format(request_to_orion.status_code))
        print(request_to_orion.text)

except Exception as e:
    print("Exception found: {}".format(e))


