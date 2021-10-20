import os
from termcolor import colored
from selenium import webdriver
from acase_app.consts import driver_dir
from acase_app.scraper import Scraper
from selenium.webdriver.common.keys import Keys

class Crawler(webdriver.Chrome):
    def __init__(self, driver_path=driver_dir, teardown=False, keywords=False):
        # Driver path is required for Selenium to execute the brower driver
        self.driver_path = driver_path

        # Teardown indicates to the program if it must to close the window browser
        # Once the script is ended or let it open.
        self.teardown = teardown

        # The OS PATH takes the driver_path to concatenate it, then Selenium executes it
        os.environ['PATH'] += self.driver_path

        self.keywords = keywords

        # The Super method brings to Crawler class some attributes given in
        # webdriver class,  like Session_id for instance.
        super(Crawler, self).__init__()

    def start(self, url):
        """ Open the browser with a given url"""
        self.get(url)

    def __exit__(self, *args):
        """Close the browser application if teardown
        is True once the program is done"""
        if self.teardown:
            super().__exit__(*args)

    def ads_breaker(self):
        """ This method searching for the body html element,
        sends it to the Scraper class to find potencials pop-ups
        and finally close them """

        try:
            self.find_element_by_xpath('/html/body').send_keys(Keys.ESCAPE)
            return
        except:
            pass

        html_element = self.find_element_by_xpath('/html/body').get_attribute('outerHTML')
        soup = Scraper(html_element)
        target_element = soup.find_ads()

        for tag, keyattr_list in target_element.items():
            for keyattr in keyattr_list:
                for key, attr in keyattr.items():
                    try:
                        self.find_element_by_css_selector(
                            f'{tag}[{key}="{attr}"]'
                        ).click()
                        print(colored('\n:: Pop-up deleted ::\n', 'green'))
                    except:
                        print('Pop-up still alive =(')


    def enable_search(self):
        """ This method find and press the button that let
        interact with the placeholder input
        """
        html_element = self.find_element_by_xpath('/html/body').get_attribute('outerHTML')
        soup = Scraper(html_element)

        elms_obj = soup.find_search_enable_btn()

        for tag, target in elms_obj.items():
            if len(target) > 0:
                for elem in target:
                    for attr, value in elem.items():
                        try:
                            if str(attr) == 'class':
                                for element in value:
                                    btn = self.find_elements_by_class_name(f'{element}')
                                    for e in btn:
                                        try:
                                            e.click()
                                            print(colored('\n:: The Searching is able ::\n', 'green'))
                                            return
                                        except:
                                            print('The searching isn\'t able yet =(')
                        except:
                            pass
                        btn = self.find_elements_by_css_selector(
                            f'{tag}[{attr}="{value}"]'
                        )
                        for element in btn:
                            try:
                                element.click()
                                print(colored('\n:: The Searching is able ::\n', 'green'))
                                return
                            except:
                                print('The searching isn\'t able yet =(')


    def perform_search(self):
        """ This method writes into the placelholder input
        and perform the searching depends on the KeyWord """

        self.implicitly_wait(3)
        html_element = self.find_element_by_xpath('/html/body').get_attribute('outerHTML')
        soup = Scraper(html_element)
        target = soup.find_search_field()

        for elem in target:
            for attr, value in elem.items():
                placeholder = self.find_elements_by_css_selector(
                    f'input[{attr}="{value}"]'
                )
                for element in placeholder:
                    try:
                        element.send_keys(self.keywords)
                        element.send_keys(Keys.RETURN)
                        print(colored('\n:: Placeholder fullfilled ::\n', 'green'))
                        return
                    except:
                        print('Can\'t type in search placeholder =(')


    def extract_results(self):
        html_element = self.find_element_by_xpath('/html/body').get_attribute('outerHTML')
        soup = Scraper(html_element)
        target = soup.get_results(self.keywords)
        return target
