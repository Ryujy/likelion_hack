from django.shortcuts import render
from .weatherdata import getData
import datetime
import json
from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup
from .models import *




def home(request):
    items = Cloth.objects.all()
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
        return render(request,'index.html',{'weather_data': weather_data, 'associate':associate_fields, "items": items})
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
        return render(request, 'index.html',{'weather_data': weather_data, 'associate':associate_fields, "items": items}) 

# 전체 출력
def print(request):
    items = Cloth.objects.all()
    return render(request, "index.html", {"items": items})

# 온도 나눠서 가져오기 (checkbox)
def temperature(request):
    if request.is_ajax and request.method == "POST":
        
        print("hrllo")
        return render(request,'temperature.html')
    # temp = request.GET.get('max_temp')
    # print(temp)
    # query = 'to4'
    # query = request.GET.get('query')

    # if (query == 'to4'):  # ~3.999도
    #     items = models.Cloth.objects.filter(temp=query)
    #     first_filter_items = items.objects.filter(max_temp)
    #     last_filter_items = first_filter.objects.filter(min_temp)
    #     return render(request, "checkbox.html", {"last_filter_items": last_filter_items})

    # elif (query == '4to8'): # 4이상 8미만
    #     items = models.Cloth.objects.filter(temp=query)
    #     first_filter_items = items.objects.filter(max_temp)
    #     last_filter_items = first_filter_items.objects.filter(min_temp)
    #     return render(request, "checkbox.html", {"last_filter_items": last_filter_items})

    # elif (query == '8to11'):
    #     items = models.Cloth.objects.filter(temp=query)
    #     first_filter_items = items.objects.filter(max_temp)
    #     last_filter_items = first_filter_items.objects.filter(min_temp)
    #     return render(request, "checkbox.html", {"last_filter_items": last_filter_items})

    # elif (query == '11to16'):
    #     items = models.Cloth.objects.filter(temp=query)
    #     first_filter_items = items.objects.filter(max_temp)
    #     last_filter_items = first_filter_items.objects.filter(min_temp)
    #     return render(request, "checkbox.html", {"last_filter_items": last_filter_items})

    # elif (query == '16to19'):
    #     items = models.Cloth.objects.filter(temp=query)
    #     first_filter_items = items.objects.filter(max_temp)
    #     last_filter_items = first_filter_items.objects.filter(min_temp)
    #     return render(request, "checkbox.html", {"last_filter_items": last_filter_items})

    # elif (query == '19to22'):
    #     items = models.Cloth.objects.filter(temp=query)
    #     first_filter_items = items.objects.filter(max_temp)
    #     last_filter_items = first_filter_items.objects.filter(min_temp)
    #     return render(request, "checkbox.html", {"last_filter_items": last_filter_items})

    # elif (query == '22to26'):
    #     items = models.Cloth.objects.filter(temp=query)
    #     first_filter_items = items.objects.filter(max_temp)
    #     last_filter_items = first_filter_items.objects.filter(min_temp)
    #     return render(request, "checkbox.html", {"last_filter_items": last_filter_items})

    # elif (query == '26to'):
    #     items = models.Cloth.objects.filter(temp=query)
    #     first_filter = items.objects.filter(max_temp)
    #     last_filter = first_filter.objects.filter(min_temp)
   
    # return render(request, "index.html", {"last_filter": last_filter})
    return render(request, "temperature.html", )

