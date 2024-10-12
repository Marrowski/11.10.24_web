import json
import urllib.parse
from urllib.request import urlopen
from urllib.error import URLError, HTTPError
import requests



#1. За допомогою urllib
#GET
url = 'https://jsonplaceholder.typicode.com/users'
response = urllib.request.urlopen(url)
data = json.loads(response.read().decode('utf-8'))

for user in data:
    print(f'ID:{user['id']}, Name: {user['username']}, email: {user['email']}, city: {user['address']['city']}')

url_posts = 'https://jsonplaceholder.typicode.com/posts'
response_posts = urllib.request.urlopen(url_posts)
data_posts = json.loads(response_posts.read().decode('utf-8'))

for posts in data_posts:
    if posts['id'] < 5:
        print(f'ID:{posts['id']}, title: {posts['title']}, text: {posts['body']}')


url_img = 'https://jsonplaceholder.typicode.com/photos'
response_img = urllib.request.urlopen(url_img)
data_img = json.loads(response_img.read().decode('utf-8'))

for images in data_img:
    if images['id'] <= 5:
        print(f'URL of image {images['url']}')


# 2. За допомогою requests
# GET
response_req = requests.get('https://jsonplaceholder.typicode.com/users')
print(response_req.ok)

posts = response_req.json()

for info in posts:
    if info['id'] <= 5:
        print(f'ID:{info['id']}, name: {info['name']}, email: {info['email']}, phone number: {info['phone']}')

#POST
data_response = requests.post('https://jsonplaceholder.typicode.com/users', data = {'name':'Oleh', 'surname': 'Yemelianov', 'email': 'qwerty123@gmail.com', 'phone':'+380000000'})
print(data_response.text)

#DELETE
data_delete = requests.delete('https://jsonplaceholder.typicode.com/users')
print(data_delete)