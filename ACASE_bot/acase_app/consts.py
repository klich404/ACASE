import os

target = {
    'mercer': 'https://www.latam.mercer.com/',
    'gartner': 'https://www.gartner.es/es',
    'deloitte': 'https://www2.deloitte.com/co/es/pages/audit/topics/biblioteca-tecnica.html?icid=nav2_biblioteca-tecnica',
    'weforum': 'https://www.weforum.org/',
    'mckinsey': 'https://www.mckinsey.com/',
    'bcg': 'https://www.bcg.com/en-co/',
    'manpower': 'https://manpowergroupcolombia.co/',
    # 'wired': 'https://www.wired.com/',
    'hrt': 'https://www.humanresourcestoday.com/',
    'thehrdirector': 'https://www.thehrdirector.com/business-news/'
}

months_format = ['january', 'february', 'march', 'april', 'may', 'june',
                 'july', 'august', 'september', 'october', 'november', 'december',
                 'jan', 'feb', 'mar', 'apr', 'jun', 'jul', 'aug', 'sep', 'sept',
                 'oct', 'nov', 'dec', 'enero', 'febrero', 'abril', 'marzo', 'mayo',
                 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre',
                 'diciembre']

# after parsing the next variable must be iqual to a route/path
# for instance, :/users/home/acase/selenium_drivers
driver_dir = ':' + '/'.join(os.getcwd().split('/')[:-1]) + '/ACASE_Crawler-Scraper/selenium_drivers'
