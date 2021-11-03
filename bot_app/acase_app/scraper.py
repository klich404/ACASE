from bs4 import BeautifulSoup
from re import search
from acase_app.consts import months_format
import pdb

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


    def get_results(self, url, keyword='liderazgo'):
        """ This method returns a list of articles
        displayed on the current website"""

        target = {
            'li': [],
            'div': [],
        }
        # Iterate each target's key to get elements
        # with BeautifulSoup's find_all method
        for tag in target.keys():
            # Get all elements of type {tag}
            elems = self.soup.find_all(str(tag))
            # Traverse all elems until find the element
            # that corresponds to the correct one
            for element in elems:
                count = False
                if element.name != 'li':
                    # print(element.name, 'No es un li')
                    element_classes = element.attrs.get('class') # ['search-item', 'row']
                    if element_classes:
                        for _class in element_classes:
                            if search('search', _class) or search('result', _class):
                                if len(self.soup.find_all(tag, class_=_class)) > 1:
                                    count = True
                    else:
                        pass

                if (element.name != 'li' and count == False):
                    continue
                    # print(f'element tag_name: {element.name}')
                # if (tag != 'li') and (search('search', element.attrs.get('class'))):
                article_description = 0
                article_title = 0
                # Searching for a p element with more than 100 letters
                # inside it's content & contains the keyword within
                for html_e in ['p', 'div']:
                    for e in element.find_all(str(html_e)):
                        concatenated_text = ''
                        for text in e:
                            if len(str(text.string).strip()) > 100:
                                if len(e) > 1:
                                    for single_text in e:
                                        if single_text.string:
                                            concatenated_text += single_text.string
                                else:
                                    concatenated_text = text.string

                                if search(keyword.lower(), str(concatenated_text).lower()):
                                    article_description += 1
                                # Searching for a h3 title with a keyword
                                # inside it's content
                                for titles in element.find_all(['h3', 'a']):
                                    concatenated_title = ''
                                    if len(titles) > 1:
                                        for single_title in titles:
                                            if single_title.string:
                                                concatenated_title += single_title.string
                                    else:
                                        concatenated_title = titles.string

                                    if search(keyword.lower(), str(concatenated_title).lower()) or\
                                            (titles.name == 'a' and len(titles.attrs.get('href')) > 10):
                                        article_title += 1

                # Add the li or div element if exits
                # an valid description && a link - or -
                # a link && a valid title

                # print(article_description, article_title)
                if (article_description > 0 and article_title > 0):
                    target[tag].append(element)
            if len(target[tag]) > 0:
                result = self.results_to_object(target[tag], keyword, url)
                return result


    def results_to_object(self, results, keyword, url):
        """ This method takes a list of articles,
        to convert them into a parsed object """

        articles = []

        for element in results:
            item = {}
            item['Source_url'] = url
            # Find the Article's title
            h = element.find('h3')
            if not search('NoneType', str(type(h))):
                item['Title'] = h.string
            else:
                anchors = element.find_all('a')
                anchor_title = ''
                for anchor in anchors:
                    # if anchor has text related with a title,
                    # append to anchor_title
                    anchor_title += anchor.get_text()
                item['Title'] = anchor_title
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
                # print(anchor)
                if (anchor.attrs.get('href') != None) and (len(anchor.attrs.get('href')) > 19):
                    item['Url'] = url + anchor.attrs.get('href')

            # Find the Article's date
            spans = element.find_all('span')
            for span in spans:
                if not search('NoneType', str(type(h))):
                    for month in months_format:
                        if search(month, span.string.lower()):
                            item['Date'] = span.string

            # Find the Article's body
            # ps = element.find_all('p')
            # for p in ps:
                # for text in p:
                    # if len(text) > 100:
                        # if search(keyword.lower(), str(text.string).lower()):
                            # item['text'] = text.string

            # If text if not yet in item dict
            # if not 'text' in item:
            for html_e in ['p', 'div']:
                for e in element.find_all(str(html_e)):
                    concatenated_text = ''
                    for text in e:
                        if len(str(text.string).strip()) > 100:
                            if len(e) > 1:
                                for single_text in e:
                                    if single_text.string:
                                        concatenated_text += single_text.string
                            else:
                                concatenated_text = text.string
                            if search(keyword.lower(), concatenated_text.lower()):
                                item['Text'] = concatenated_text.strip()

            item['Associated_KW'] = keyword
            articles.append(item)
        return articles
