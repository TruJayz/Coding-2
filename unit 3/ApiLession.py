import requests


data = requests.get('https://restcountries.com/v3.1/name/peru')

print(data)
print(data.json())

