from flask import Flask, request, jsonify
import json
from scraper import scrapping

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        phrase = request.args.get('phrase')
        print(phrase)
        result = scrapping(phrase)
        data = []
        for item in result:
            data_item = {
                'Name': item['name'],
                'price': item['price'],
                'url': item['URL wewnętrzne']
            }
            data.append(data_item)
        with open('data.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False)
        return 'Data saved to JSON file'
    elif request.method == 'POST':
        data = request.get_json()
        return jsonify(data)
    else:
        return 'Invalid method'

if __name__ == '__main__':
    app.run(debug=True)
