# ACASE Crawler & Scraper
Automated Crawling And Scraping Engine (ACASE) is a software that navigates into a web site and extract specific information.

## Installation
#### Clone this repository
```git clone https://github.com/sneidergv/ACASE_Crawler-Scraper.git```

#### Create a virtual environment
```cd ACASE_Crawler-Scraper/```
```python3 -m venv .```

#### Activate the virtual environment
```. bin/activate```

#### Install dependencies
```pip install -r requirements.txt```

#### Download the driver
This program works with Chrome browser, thus you've to download both Chrome driver for selenium and Chrome browser application for your OS.

- Download the Chrome driver according to your Chrome browser version.
To know which version you use, copy and paste in url field:
```chrome://version/```
- Download the corresponding driver from this web site:
https://chromedriver.storage.googleapis.com/index.html

- Now uncompress the zip file and move the **chromedriver** file that is inside of the zip archive to the ```ACASE_Crawler-Scraper/selenium_drivers/``` folder.

#### Run the program
```python3 run.py```