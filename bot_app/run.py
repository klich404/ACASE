import time
import pdb
import json
from termcolor import colored
from acase_app.crawler import Crawler
from acase_app.scraper import Scraper
from flask import Flask, request

app = Flask(__name__)


@ app.route("/bot", strict_slashes=False, methods=['POST'])
def run_bot():
    farming = []

    target = json.loads(request.data)
    if type(target) is not list:
        print('Please insert a list of objects')
    else:
        for resource in target:
            if len(resource.get('keywords')) == 0:
                print('no hay keywords')
                continue
            for keyword in resource.get('keywords'):
                print(
                    colored(f'Scraping {keyword} from {resource.get("name")}...', 'blue'))
                with Crawler(url=resource.get('url'), teardown=True, keywords=keyword) as bot:
                    bot.start()
                    bot.ads_breaker()
                    bot.enable_search()
                    bot.perform_search()
                    results = bot.extract_results()  # [{}, {}, {}]
                    # print(f'{len(results)} from {keyword}: {resource.get("name")}')
                    try:
                        for result in results:
                            farming.append(result)
                    except Exception as err:
                        print(f'except error:', err)
        with open('results.json', 'w', encoding='utf-8') as f:
            json.dump(farming, f)
    print(colored('The process has been successfully completed.', 'green'))

    for count, item in enumerate(farming):
        if not 'Date' in item:
            item['Date'] = 'No Date'
        if not 'Url' in item:
            item['Url'] = ':: suspicious item ::'
        if count + 1 == len(results):
            print(
                colored(f'\n>>> {count + 1} items have been obtained', 'green'))

    # En vez de retornar el JSON, se debe enviar a un endpoint de Django
    # para que Django lo almacene en la base de datos.
    return json.dumps(farming)


if __name__ == '__main__':
    app.run(host='localhost', port='3000', debug=True)
