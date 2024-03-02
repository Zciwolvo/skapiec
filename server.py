from flask import Flask, request, jsonify
import json
from Scraper import scrapping
import time
import re
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
JSON_PATH = "./data.json"

def read_json_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data

def write_json_file(file_path, data):
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def find_index(data, url):
    for i, item in enumerate(data):
        if item['internal_url'] == url:
            return i
        
def extract_money_value(money_string):
    pattern = r'\d+(\.\d+)?'
    match = re.search(pattern, money_string)
    if match:
        return float(match.group())
    else:
        return None


@app.route('/scrape', methods=['GET'])
def index_get():
    phrase = request.args.get('phrase')
    if phrase:
        result = scrapping(phrase)
        data = read_json_file(JSON_PATH)
        for item in result:
            if any(x['internal_url'] == item['internal_url'] for x in data):
                index_of_item = find_index(data, item['internal_url'])
                price_new = extract_money_value(item['price'])
                price_old = extract_money_value(data[index_of_item]['price_lowest'])
                if price_new <= price_old:
                    data[index_of_item]['price_lowest'] = item['price']
                    data[index_of_item]['price'] = item['price']
                    data[index_of_item]['update_lowest'] = time.time()
                    data[index_of_item]['update'] = time.time()
                else:
                    data[index_of_item]['price'] = item['price']
                    data[index_of_item]['update'] = time.time()
            else:
                data_item = {
                    'id': len(data)+1,
                    'search': phrase,
                    'name': item['name'],
                    'price': item['price'],
                    'price_lowest': item['price'],
                    'external_url': item['external_url'],
                    'internal_url': item['internal_url'],
                    'photo': item['photo'],
                    'update': time.time(),
                    'update_lowest': time.time()
                }
                data.append(data_item)
        write_json_file(JSON_PATH, data)
        return 'Data saved to JSON file'
    else:
        return 'Missing phrase parameter', 400


@app.route('/get_data', methods=['GET'])
def get_data():
    data = read_json_file(JSON_PATH)
    print(data)
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
