# ACASE
## Automated Crawler and Scraper Engine
![Imgur](https://i.imgur.com/82Y4cvn.png)
ACASE is a bot of specialized research where the user has the possibility of make the investigation giving parameters according the needs of the company and save or delete this data.

## Requeriments
```
python3-pip
beautifulsoup4
Django              == 3.2.8
django-cors-headers == 3.10.0
mysqlclient         == 2.0.3
```

## Use
ACASE (Automated Crawler and Scrapper Engine) is a bot developed in Python with the library Selenium. This scrapper is capable of search information of three websites recommended by the company and return all this information into an API developed with Django and save all the data in a database created with MySQL. All this information is sent into a view to the Frontend where it starts to consume of and return new information sent by the user.
The user site was developed in HTML, CSS and Javascript where the watchman has the posibility of make the research filtering by keywords and urls, watch a little description about the content of the card, the name, visit the url and make some notes about it also, the user has the posibility of save the card in a different view named Selección or if the user is not interested has the posibility of send it to Papelera view.

![Imgur](https://i.imgur.com/rwKLEEd.png)

### Steps
- Run Django on port 8000 "`~/Django/ACASE/api$ python3 manage.py runserver`" and run Flask on port 3000 "`~/Django/ACASE/bot_app$ python3 run.py`"
- Do the following curl in the parent directory: "`~/Django/ACASE$ curl -X POST localhost:3000/bot -H 'Content-Type: application/json' -d @example_to_activate_bot.json`"
- Run the FrontEnd on port 5500 "`~/Django/ACASE/Frontend/index.html`"
- Select **keyword**, **web page** and click the **search** button
- Handle items to your liking

## Version
**ACASE 1.0**

## Authors
**Esneider Granada Valencia** - *Web Developer* - [sneidergv](https://github.com/sneidergv)

**Natalia Arteaga Corrales** - *Frontend Developer* - [natyarteagac](https://github.com/natyarteagac)

**Carlos Cruz Zuluaga** - *Backend Developer* - [klich404](https://github.com/klich404)
