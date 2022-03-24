import json
import requests

print('Please enter your zip code:')
zip = input()

r =requests.get('http://api.openweathermap.org/data/2.5/weather?zip=%s,us&appid=3b37bed3adc657714e8cac13c80e618d' % zip)
data=r.json()
print(data['weather'][0]['description'])
