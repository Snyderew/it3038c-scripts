import json
import requests

#r = requests.get('http://localhost:3000/')
with open('/home/student/widgets.json') as data:
    widgets = json.load(data)

for i in widgets:
    print(i['name'], "is", i['color'])
    #print("is", i['color'])
