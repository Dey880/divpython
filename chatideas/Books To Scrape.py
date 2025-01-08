import requests
from bs4 import BeautifulSoup

url = 'https://books.toscrape.com/'
response = requests.get(url)
response.encoding = 'utf-8'


if response.status_code == 200:
    print('Successfully retrieved data')
else:
    print('Failed to retrieve data!')
    
soup = BeautifulSoup(response.text, 'html.parser')

books_data = []

books = soup.find_all('article', class_='product_pod')

for book in books:
    name = book.find('h3').find('a').get('title').strip()
    price = book.find('p', class_='price_color').text.strip()
    in_stock = book.find('p', class_='availability')
    
    if in_stock:
        i_tag = in_stock.find('i')
        if i_tag:
            i_tag.decompose()
            
        availability_text = in_stock.text.strip()
        
    books_data.append({
        'name': name,
        'price': price,
        'availability': availability_text
    })
    
books_data.sort(key=lambda x: x['availability'])

for idx, book_data in enumerate(books_data, 1):
    print(f"\nBook #{idx}:")
    print(f"Name: {book_data['name']}")
    print(f"Price: {book_data['price']}")
    print(f"Availability: {book_data['availability']}")
    print('-' * 50)