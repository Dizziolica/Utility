import os
import requests
from bs4 import BeautifulSoup

# enviar uma solicitação HTTP para o site
response = requests.get('https://www.google.pt/')

# extrair o HTML usando o Beautiful Soup
soup = BeautifulSoup(response.text, 'html.parser')
html = soup.find_all('script')

with open("YourText.html", 'w') as arquivo:
    arquivo.write(html)



print("saved")
