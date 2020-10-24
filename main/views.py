from django.shortcuts import render
from .weatherdata import getData
import datetime
import json
from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup

def weather(request):
    weather_data = None
    days_list=[]
    image_list=[]
    maxtemp_list=[]
    mintemp_list=[]
    if 'city' in request.GET:
        city  = request.GET.get('city')
        html_content = getData(city)
        soup = BeautifulSoup(html_content.text)
        weather_data = dict()
        weather_data['region'] = soup.find('div', attrs={'id':'wob_loc'}).text
        weather_data['date_time'] = soup.find('div', attrs={'id':'wob_dts'}).text
        weather_data['desc'] = soup.find('span', attrs={'id':'wob_dc'}).text
        weather_data['icon'] = soup.find('img', attrs={'id':'wob_tci'}).get('src')
        weather_data['temp'] = soup.find('span', attrs={'id':'wob_tm'}).text
        for i in range(0,8):          
            days=soup.find('div', attrs={'data-wob-di':{i}})
            days1 = days.find('div', attrs={'class':'QrNVmd Z1VzSb'}).get('aria-label')
            days_list.append(days1)
            image=soup.find('div', attrs={'data-wob-di':{i}})
            image_all = image.find('img', attrs={'class':'uW5pk'}).get('src')
            image_list.append(image_all) 
            maxtemp=soup.find('div', attrs={'data-wob-di':{i}})
            maxtemp_all = maxtemp.find('span', attrs={'class':'wob_t'}).text
            maxtemp_list.append(maxtemp_all)
            mintemp=soup.find('div', attrs={'data-wob-di':{i}})
            mintemp_all = mintemp.find('div', attrs={'class':'QrNVmd ZXCv8e'})
            __mintemp= mintemp_all.find('span', attrs={'class':'wob_t'}).text
            mintemp_list.append(__mintemp)                      
        associate_fields= zip(days_list, image_list,maxtemp_list, mintemp_list)
        return render(request,'weatherPage.html',{'weather_data': weather_data, 'associate':associate_fields})
    else:
        html_content = getData('seoul')
        soup = BeautifulSoup(html_content.text, "html.parser")
        weather_data = dict()
        weather_data['region'] = soup.find('div', attrs={'id':'wob_loc'}).text
        weather_data['date_time'] = soup.find('div', attrs={'id':'wob_dts'}).text
        weather_data['desc'] = soup.find('span', attrs={'id':'wob_dc'}).text
        weather_data['icon'] = soup.find('img', attrs={'id':'wob_tci'}).get('src')
        weather_data['temp'] = soup.find('span', attrs={'id':'wob_tm'}).text
        for i in range(0,8):          
            days=soup.find('div', attrs={'data-wob-di':{i}})
            days1 = days.find('div', attrs={'class':'QrNVmd Z1VzSb'}).get('aria-label')
            days_list.append(days1)
            image=soup.find('div', attrs={'data-wob-di':{i}})
            image_all = image.find('img', attrs={'class':'uW5pk'}).get('src')
            image_list.append(image_all) 
            maxtemp=soup.find('div', attrs={'data-wob-di':{i}})
            maxtemp_all = maxtemp.find('span', attrs={'class':'wob_t'}).text
            maxtemp_list.append(maxtemp_all)
            mintemp=soup.find('div', attrs={'data-wob-di':{i}})
            mintemp_all = mintemp.find('div', attrs={'class':'QrNVmd ZXCv8e'})
            __mintemp= mintemp_all.find('span', attrs={'class':'wob_t'}).text
            mintemp_list.append(__mintemp)                      
        associate_fields= zip(days_list, image_list,maxtemp_list, mintemp_list)
        return render(request, 'weatherPage.html',{'weather_data': weather_data, 'associate':associate_fields})    

