import requests
from bs4 import BeautifulSoup

def fetch_quotes(url):
    quotes_data = []
    count = 0
    while url:
        response = requests.get(url)
        response.encoding = 'utf-8'
        
        if response.status_code != 200:
            print("Failed to retrieve page")
            break
            
        soup = BeautifulSoup(response.text, 'html.parser')
        quotes = soup.find_all('div', class_='quote')
        
        for quote in quotes:
            text = quote.find('span', class_='text').text.strip()
            author = quote.find('small', class_='author').text.strip()
            tags = [tag.text for tag in quote.find_all('a', class_='tag')]
            quotes_data.append({
                'text': text,
                'author': author,
                'tags': tags
            })
            
        next_button = soup.find('li', class_='next')
        if next_button:
            count += 1
            next_url = next_button.find('a')['href']
            url = f"https://quotes.toscrape.com{next_url}"
            print(f"Getting data: {count} / ?")
        else:
            url = None
            
    return quotes_data

def all_quotes():
    url = 'https://quotes.toscrape.com/'
    quotes_data = fetch_quotes(url)
    for idx, quote_data in enumerate(quotes_data, 1):
        print(f"\nQuote #{idx}:")
        print(f"Text: {quote_data['text']}")
        print(f"Author: {quote_data['author']}")
        print(f"Tags: {', '.join(quote_data['tags'])}")
        print('-' * 50)
        
def random_quote():
    url = 'https://quotes.toscrape.com/random'
    quotes_data = fetch_quotes(url)
    for idx, quote_data in enumerate(quotes_data, 1):
        print(f"\nQuote #{idx}:")
        print(f"Text: {quote_data['text']}")
        print(f"Author: {quote_data['author']}")
        print(f"Tags: {', '.join(quote_data['tags'])}")
        print('-' * 50)
        
print("""
What would you like to see?
1. All quotes (may take some time to load)
2. One random quote
""")
qhar = input()

try:
    qhar = int(qhar)
except ValueError:
    print("Not a valid number, please try again.")
    
if qhar == 1:
    all_quotes()
elif qhar == 2:
    random_quote()
else:
    print("Not a valid number, please try again.")