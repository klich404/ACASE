from bs4 import BeautifulSoup
from re import search
from acase_app.consts import months_format

class Scraper():
    def __init__(self, html_element):
        self.soup = BeautifulSoup(html_element, 'html.parser')
        # uncomment to save the entire html object and
        # execute this program without open the browser

        # with open('hrt', 'w') as f:
            # f.write(self.soup.prettify())

    def find_ads(self):
        element_target = {'a': [], 'button': []}
        # Get all divs elements from a website
        divs = self.soup.find_all('div')
        # Iterate each div element
        for div in divs:
            # Iterate the attributes that contains each div tag
            for attribute in div.attrs.values():
                # Searching for 'modal' word in each attribute
                if search('modal', str(attribute)):
                    for anchor in div.find_all('a'):
                        for key, attr in anchor.attrs.items():
                            if search('close', str(attr).lower()):
                                element_target['a'].append({str(key): attr})
                    for button in div.find_all('button'):
                        for key, attr in button.attrs.items():
                            if search('close', str(attr).lower()):
                                element_target['button'].append({str(key): attr})
        return element_target



    def find_search_field(self):
        inputs = self.soup.find_all('input')
        target = []

        for input_elem in inputs:
            for attr, value in input_elem.attrs.items():
                if str(attr) == 'placeholder' and search('search', str(value).lower()):
                    target.append({attr: value})
                if str(attr) == 'placeholder' and search('buscar', str(value).lower()):
                    target.append({attr: value})

        return target


    def find_search_enable_btn(self):
        """ This method returns the 'attr=value'
        of the element that once clicked allows write
        in the placeholder"""

        target = {
            'span':  [],
            'button': [],
            'a': []
        }

        for tag in target.keys():
            elems = self.soup.find_all(str(tag))
            for btn in elems:
                for attr, value in btn.attrs.items():
                    if search('search', str(value).lower()):
                        target[tag].append({attr: value})
                if len(target[tag]) > 0:
                    return target


    def get_results(self, keyword='liderazgo'):
        """ This method returns a list of articles
        displayed on the current website"""

        target = {
            'li': [],
            # 'div': [],
        }

        for tag in target.keys():
            elems = self.soup.find_all(str(tag))
            for element in elems:
                p = 0
                a = 0
                for e in element.find_all('p'):
                    for text in e:
                        if len(text) > 100:
                            if search(keyword.lower(), str(text.string).lower()):
                                p += 1
                for anc in element.find_all('a'):
                    for anchor in anc:
                        if len(anchor) > 0:
                            a += 1
                if p > 0 and a > 0:
                    target[tag].append(element)
        if len(target[tag]) > 0:
            result = self.results_to_object(target[tag], keyword)
            return result


    def results_to_object(self, results, keyword):
        """ This method takes a list of articles,
        to convert them into a parsed object """

        articles = []

        for element in results:
            item = {}
            # Find the Article's title
            h = element.find('h3')
            if len(h) != 0:
                item['title'] = h.string
            else:
                anchors = element.find_all('a')
                anchor_title = []
                for anchor in anchors:
                    # if anchor has text related with a title,
                    # append to anchor_title
                    pass
                if len(anchor_title) == 0:
                    divs = element.find_all('div')
                    div_title = []
                    for div in divs:
                        # if div has text related with a title,
                        # append to div_title
                        pass

            # Find the Article's url
            anchors = element.find_all('a')
            for anchor in anchors:
                if len(anchor.attrs.get('href')) > 50:
                       item['url'] = anchor.attrs.get('href')

            # Find the Article's date
            spans = element.find_all('span')
            for span in spans:
                for month in months_format:
                    if search(month, span.string.lower()):
                        item['date'] = span.string

            # Find the Article's body
            ps = element.find_all('p')
            for p in ps:
                for text in p:
                    if len(text) > 100:
                        if search(keyword.lower(), str(text.string).lower()):
                            item['text'] = text.string

            item['Associated_KW'] = keyword
            articles.append(item)
        return articles
