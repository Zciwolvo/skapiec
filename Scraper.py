import requests
from bs4 import BeautifulSoup
import re


# Removing html tags
def remove_html_tags(text:str):
    """
    This method removing HTML tags from text. 
    """
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)

# Scraping method
def scrapping(phrase:str):
    """
        This function takes a phrase as an argument, searches for items on the skapiec.pl website using BeautifulSoup.
        It parses the data, finds specific data by HTML tags: name, price, PNG, internal URL, external URL,
        and saves everything to a list, then returns that list.
    """
    # Loading skapiec page, parsing html
    url = f"https://www.skapiec.pl/szukaj?query={phrase}&categoryId="
    r = requests.get(url)
    if r.status_code == 200:
        soup = BeautifulSoup(r.text, 'html.parser')
        # Finding data with bs4 by tags
        products = soup.find_all('h2', title=True)
        prices = soup.find_all('span', class_='price')
        internal_urls = soup.find_all('a', class_='product-box-narrow__title')
        photos = soup.find_all('div', class_='product-box-narrow__photo-box-image')
        external_urls = soup.find_all('a', class_='button button--primary button--md button--fw-500 product-box-narrow__button product-box-narrow__button--shop')
        # Consistensy check
        if len(products) == len(prices):
            # Getting data and appending to list
            product_info = []
            for product, price, internal_url, photo, external_url in zip(products, prices, internal_urls, photos, external_urls):
                name = product['title']
                price_value = price.get_text().replace('\xa0zł', '').replace(',', '.')
                skapiec_url = internal_url['href'] if internal_url else None
                photo = photo.find('img')['src'] if photo.find('img') else None
                shop_url = external_url['href'] if external_url else None 
                product_info.append({'name': name, 'price': price_value, 'internal_url': skapiec_url, 'photo': photo, 'external_url': shop_url})
            return product_info
        else:
            return None 
    else:
        return None 

# Description scrapper (iternal url)

def scrapDescription(skapiec_url:str):
    """
    This function takes skapiec_url from function "scrapping" and scrap description for items from it.
    """
    response = requests.get('https://skapiec.pl'+skURL+'#opis')
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        description = soup.find_all('div', class_='expander__text expander__text--show-more')
        cleaned_description = [remove_html_tags(desc.get_text()) for desc in description]
        return cleaned_description
    else:
        return None
if __name__ == '__main__':

    # Take phrase from user and scrap!
    search_phrase = input("Podaj frazę: ")
    result = scrapping(search_phrase) 

    if result:
        for item in result:
            skapiec_url = item['internal_url'] if item['internal_url'] else "Brak"
            shop_url = item['external_url'] if item['external_url'] else "brak"
            # description = scrapDescription(skURL)
            # if description:
            print(f"Nazwa: {item['name']}, Cena: {item['price']} zł, URL wewnętrzne: {'skapiec.pl'+skapiec_url}, URL zewnętrzne: {shop_url}, Zdjęcie: {item['photo']},\n")
    else:
        print("Brak wyników")
