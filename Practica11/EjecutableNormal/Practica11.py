import requests
from bs4 import BeautifulSoup
import random

url = 'https://www.vix.com/es/comics/195990/los-100-mejores-anime-de-todos-los-tiempos-ordenados-de-peor-a-mejor-segun-imdb'
pagina = requests.get(url)
soup = BeautifulSoup(pagina.content, 'html.parser')
#print(soup)

#an = soup.find_all('span', class_='copyright')
an = soup.find_all('i')
animes = list()
for i in an:
    animes.append(i.text)
random = random.randrange(0, 99)
print("Anime que Recomendamos es : ", animes[random])
a = input("Presione Enter para cerrar........")
