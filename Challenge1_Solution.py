import requests

url = 'https://jsonplaceholder.typicode.com/photos'
response = requests.get(url)
json_data = response.json()
list_url = []
for photo in json_data:
    list_url.append(photo['url'])
    print(len(list_url))
    print(len(set(list_url)))
