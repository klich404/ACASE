# ACASE
## Automated Crawler and Scraper Engine
![Imgur](https://i.imgur.com/82Y4cvn.png)
ACASE is a bot of specialized research where the user has the possibility of make the investigation giving parameters according the needs of the company and save or delete this data.

## Install
### pre-requisites
to be able to use ACASE without versioning problems we recommend you to install the following  [requirements](https://github.com/klich404/ACASE/blob/main/api/requirements.txt) as follows:
`pip install -r requirements.txt`

### Installation
Clone this repository to access the app from your local environment:
`git clone https://github.com/klich404/ACASE.git`

Then go into the ACASE/api/ folder and run the Django app with:
`python3 manage.py runserver`

Finally while the api is running open the index.html found in ACASE/Frontend/ with live server or similar and you will be able to see the application from your browser.

## Use
ACASE (Automated Crawler and Scrapper Engine) is a bot developed in Python with his Framework Selenium. This scrapper is capable of search information of three websites recommended by the company and return all this information into an API developed with Django and save all the data in a database created with MySQL. All this information is sent into a view to the Frontend where it starts to consume of and return new information sent by the user.
The user site was developed in HTML, CSS and Javascript where the user has the posibility of make the research filtering by keywords and urls, watch a little description about the content of this research, the name, visit the url and make some notes about it also, the user has the posibility of save the card in a different view named Selección or if the user is not interested about the card has the posibility of send it to Papelera view.
![Imgur](https://i.imgur.com/rwKLEEd.png)

## Version 
ACASE 1.0

## Authors
**Esneider Granada Valencia** - *Web Developer* - [sneidergv](https://github.com/sneidergv)
**Natalia Arteaga Corrales** - *Frontend Developer* - [natyarteagac](https://github.com/natyarteagac)
**Carlos Cruz Zuluaga** - *Backend Developer* - [klich404](https://github.com/klich404)
