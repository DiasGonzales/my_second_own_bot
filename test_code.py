import requests
from bs4 import BeautifulSoup
import random

def fetch_random_quote():
    random_bash = random.randint(1, 87932)
    url = f"http://www.bashorg.org/quote/{random_bash}"

    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the quote text within the 'div' element with class 'quote'
        quote_div = soup.find('div', class_='quote')

        if quote_div:
            # Extract the text of the quote and remove leading/trailing whitespace
            quote_text = quote_div.text.strip()
            return f"цитата #{random_bash}: {quote_text}"
        else:
            return f"Извиняйте цитата была удалена #{random_bash}"
    else:
        return f"Извиняй цитаты нет #{random_bash}. Status code: {response.status_code}"


