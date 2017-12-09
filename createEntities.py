import requests

values = """
{
  "actionType": "APPEND",
  "entities":[
    {
      "id": "Room1",
      "type": "Room",
      "temperature": {
        "value": 23,
        "type": "Float"
      },
      "pressure": {
        "value": 720,
        "type": "Integer"
      }
    },
    {
      "id": "Room2",
      "type": "Room",
      "temperature": {
        "value": 21,
        "type": "Float"
      },
      "pressure": {
        "value": 711,
        "type": "Integer"
      }
    },
  {
      "type": "Room",
      "id": "Room3",
      "temperature": {
        "value": 21.2,
        "type": "Float"
      },
      "pressure": {
        "value": 722,
        "type": "Integer"
      }
    },
    {
      "type": "Room",
      "id": "Room4",
      "temperature": {
        "value": 31.8,
        "type": "Float"
      },
      "pressure": {
        "value": 712,
        "type": "Integer"
      }
    }
  ]
}
"""

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


