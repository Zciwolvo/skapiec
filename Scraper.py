import requests
from bs4 import BeautifulSoup
import re

if __name__ == '__main__':
    # Removing html tags
    def remove_html_tags(text):
        clean = re.compile('<.*?>')
        return re.sub(clean, '', text)
    
    # Scraping method
    def scrapping(phrase):
        # Loading skapiec page, parsing html
        url = f"https://www.skapiec.pl/szukaj?query={phrase}&categoryId="
        r = requests.get(url)
        if r.status_code == 200:
            soup = BeautifulSoup(r.text, 'html.parser')
            # Finding data with bs4 by tags
            products = soup.find_all('h2', title=True)
            prices = soup.find_all('span', class_='price')
            iternalUrls = soup.find_all('a', class_='product-box-narrow__title')
            photos = soup.find_all('div', class_='product-box-narrow__photo-box-image')
            externalUrls = soup.find_all('a', class_='button button--primary button--md button--fw-500 product-box-narrow__button product-box-narrow__button--shop')
            # Consistensy check
            if len(products) == len(prices):
                # Getting data and appending to list
                productsInfo = []
                for product, price, iternalUrl, photo, externalurl in zip(products, prices, iternalUrls, photos, externalUrls):
                    name = product['title']
                    priceValue = price.get_text().replace('\xa0zł', '').replace(',', '.')
                    skapiecUrl = iternalUrl['href'] if iternalUrl else None
                    photo = photo.find('img')['src'] if photo.find('img') else None
                    shopUrl = externalurl['href'] if externalurl else None 
                    productsInfo.append({'name': name, 'price': priceValue, 'iternalUrl': skapiecUrl, 'photo': photo, 'externalUrl': shopUrl})
                return productsInfo
            else:
                return None 
        else:
            return None 

    # Description scrapper (iternal url)
    '''
    def scrapDescription(skURL):
        response = requests.get('https://skapiec.pl'+skURL+'#opis')
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')

            description = soup.find_all('div', class_='expander__text expander__text--show-more')
            cleaned_description = [remove_html_tags(desc.get_text()) for desc in description]
            return cleaned_description
        else:
            return None
    ''' 

    # Take phrase from user and scrap!
    searchPhrase = input("Podaj frazę: ")
    result = scrapping(searchPhrase) 

    if result:
        for item in result:
            skapiecUrl = item['iternalUrl'] if item['iternalUrl'] else "Brak"
            shopUrl = item['externalUrl'] if item['externalUrl'] else "brak"
            # description = scrapDescription(skURL)
            # if description:
            print(f"Nazwa: {item['name']}, Cena: {item['price']} zł, URL wewnętrzne: {'skapiec.pl'+skapiecUrl}, URL zewnętrzne: {shopUrl}, Zdjęcie: {item['photo']},\n")
    else:
        print("Brak wyników")
