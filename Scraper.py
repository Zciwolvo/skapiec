import requests
from bs4 import BeautifulSoup

def scrapping(fraza):
    url = f"https://www.skapiec.pl/szukaj?query={fraza}&categoryId="
    r = requests.get(url)
    if r.status_code == 200:
        soup = BeautifulSoup(r.text, 'html.parser')
        
        products = soup.find_all('h2', title=True)
        prices = soup.find_all('span', class_='price')
        wewURLs = soup.find_all('a', class_='product-box-narrow__title')

        if len(products) == len(prices):
            products_info = []

            for product, price, wewURL in zip(products, prices, wewURLs):
                name = product['title']
                price_value = price.get_text().replace('\xa0zł', '').replace(',', '.')
                skURL = wewURL['href'] if wewURL else None
                products_info.append({'name': name, 'price': price_value, 'URL wewnętrzne': skURL})

            return products_info
        else:
            return None 
    else:
        return None
    

search_phrase = input("Podaj frazę: ")
result = scrapping(search_phrase)
if result:
    for item in result:
        skURL = item['URL wewnętrzne'] if item['URL wewnętrzne'] else "Brak"
        print(f"Nazwa: {item['name']}, Cena: {item['price']} zł, URL wewnętrzne: {"skapiec.pl"+skURL}")
else:
    print("Brak wyników")
