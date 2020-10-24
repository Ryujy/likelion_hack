from urllib.request import urlopen
import xmltodict
import json
import requests


def getData(city):
    try:
        USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
        LANGUAGE = "en-US,en;q=0.5"
        session = requests.Session()
        session.headers['User-Agent'] = USER_AGENT
        session.headers['Accept-Language'] = LANGUAGE
        session.headers['Content-Language'] = LANGUAGE
        city = city.replace('', '+')
        html_content = session.get(f'https://www.google.com/search?q=weather+in+{city}')     
    except Exception as er:
        print(er)
    else:
        return html_content



