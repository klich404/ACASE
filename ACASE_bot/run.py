import time
from acase_app.crawler import Crawler
from acase_app.consts import target
from acase_app.scraper import Scraper

# with open('hrt', 'r') as mercer:
    # scraper = Scraper()
    # scraper.find_input()

# for _, url in target.items():
    # with Crawler(teardown=True) as bot:
        # bot.start(url)
        # bot.ads_breaker()
        # bot.enable_search()
        # bot.perform_search()
        # bot.extract_results()
keywords = 'liderazgo'
with Crawler(teardown=False, keywords=keywords) as bot:
    bot.start(target.get('mercer'))
    bot.ads_breaker()
    bot.enable_search()
    bot.perform_search()
    print(bot.extract_results())
