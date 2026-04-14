  # from urllib import response

import requests



 # url = 'https://jsonplaceholder.typicode.com/posts'
# response = requests.get(url)


# print(response.json())



# import requests

 # url = "https://bored-api.appbrewery.com/filter?type=education"
# response = requests.get(url)


 # print(response.json())



 # url = 'https://pokeapi.co/api/v2/pokemon/ditto'
 #response = requests.get(url)










# 4/14/2026 


query = "https://pokeapi.co/api/v2/pokemon/umbreon"
response = requests.get(query)
print(response)
print(response.json())

if response.status_code == 200:
    data = response.json()
    

    filtered_data = {
        "name": data["name"],
        "height": data["height"],
        "weight": data["weight"],
        "type": data["types"],
        "abilities": [ability["ability"]["name"] for ability in data["abilities"]],
        "sprites":data["sprites"]
    }
    print(filtered_data)
else:
    print("Failed to retrieve data")