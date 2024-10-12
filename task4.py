from urllib.request import urlopen
from urllib.error import HTTPError, URLError
import requests

url = 'https://docs.python.org/3/'
response = urlopen(url)

print(response.read())


url_roz = 'https://rozetka.com.ua/ua/'

try:
    response_a = urlopen(url_roz)
except HTTPError as e:
    print(f'HTTP Error: {e.code}, cant access to the resourse.')
except URLError as e:
    print(f'URL Error: {e.reason}')


response_b = requests.get('https://www.youtube.com/')
print(response_b.ok)
print(response_b.text)
