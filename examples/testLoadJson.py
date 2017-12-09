#From https://stackoverflow.com/questions/38644480/reading-json-file-with-python-3#38644565
#Posted in https://stackoverflow.com/ by @lcastillov


import json

with open('payload.json', 'r') as f:
    array = json.load(f)

print (array)