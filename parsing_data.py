
import requests
from bs4 import BeautifulSoup
import random


random_bash = random.randint(1, 87932)
url = "http://www.bashorg.org/quote/" + str(random_bash)

# print(url)
# print('цитата #' + str(random_bash))

r = requests.get(url)

# print(r.text)

soup = BeautifulSoup(r.text, 'html.parser')

for link in soup.find_all('div', class_='quote'):

    data = link.text
    # print(data)


