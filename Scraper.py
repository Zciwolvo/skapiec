import requests
from bs4 import BeautifulSoup
import re

def remove_html_tags(text):
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)

def scrapping(fraza):
    url = f"https://www.skapiec.pl/szukaj?query={fraza}&categoryId="
    r = requests.get(url)
    if r.status_code == 200:
        soup = BeautifulSoup(r.text, 'html.parser')
        
        products = soup.find_all('h2', title=True)
        prices = soup.find_all('span', class_='price')
        wewURLs = soup.find_all('a', class_='product-box-narrow__title')
        photos = soup.find_all('div', class_='product-box-narrow__photo-box-image')
        zewURLs = soup.find_all('a', class_='button button--primary button--md button--fw-500 product-box-narrow__button product-box-narrow__button--shop')

        if len(products) == len(prices):
            products_info = []

            for product, price, wewURL, photo, zewURL in zip(products, prices, wewURLs, photos, zewURLs):
                name = product['title']
                price_value = price.get_text().replace('\xa0zł', '').replace(',', '.')
                skURL = wewURL['href'] if wewURL else None
                photo = photo.find('img')['src'] if photo.find('img') else None
                sklepURL = zewURL['href'] if zewURL else None 
                products_info.append({'name': name, 'price': price_value, 'URL wewnętrzne': skURL, 'photo': photo, 'URL zewnętrzne': sklepURL})


            return products_info
        else:
            return None 
    else:
        return None

def scrapDescription(skURL):
    response = requests.get('https://skapiec.pl'+skURL+'#opis')
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        description = soup.find_all('div', class_='expander__text expander__text--show-more')
        cleaned_description = [remove_html_tags(desc.get_text()) for desc in description]
        return cleaned_description
    else:
        return None
    
if __name__ == '__main__':

    search_phrase = input("Podaj frazę: ")
    result = scrapping(search_phrase) 

    if result:
        for item in result:
            skURL = item['URL wewnętrzne'] if item['URL wewnętrzne'] else "Brak"
            sklepURL = item['URL zewnętrzne'] if item['URL zewnętrzne'] else "brak"
            description = scrapDescription(skURL)
            if description:
                print(f"Nazwa: {item['name']}, Cena: {item['price']} zł, URL wewnętrzne: {'skapiec.pl'+skURL}, URL zewnętrzne: {sklepURL}, Zdjęcie: {item['photo']},\nOpis: {description[0]}\n")
    else:
        print("Brak wyników")
