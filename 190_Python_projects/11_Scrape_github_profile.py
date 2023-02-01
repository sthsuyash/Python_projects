import requests
from bs4 import BeautifulSoup

name = input(f"Enter github username: ")
url = f'https://github.com/{name}'

r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')

profile_image = soup.find('img', {'alt': 'Avatar'})['src']
print(profile_image)
