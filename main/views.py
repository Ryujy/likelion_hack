from django.shortcuts import render
from . import models

def home(request):
    return render(request, 'index.html')

# 온도 나눠서 가져오기
def temperature(request, max_temp, min_temp):
    query = 10

    # # query가 있으면
    # if not (query == None or  query == ''):
    #     first_filter = items.filter(temp_name = query)
    #     second_filter = first_filter.objects.filter(max_temp)
    #     last_filter = second_filter.objects.filter(min_temp)


    if (query == 'to4'):
        items = models.Cloth.objects.filter(temp=query)
        first_filter = items.objects.filter(max_temp)
        last_filter = first_filter.objects.filter(min_temp)

    elif (query == '5to8'):
        items = models.Cloth.objects.filter(temp=query)
        first_filter = items.objects.filter(max_temp)
        last_filter = first_filter.objects.filter(min_temp)

    elif (query == '12to16'):
        items = models.Cloth.objects.filter(temp=query)
        first_filter = items.objects.filter(max_temp)
        last_filter = first_filter.objects.filter(min_temp)

    elif (query == '17to19'):
        items = models.Cloth.objects.filter(temp=query)
        first_filter = items.objects.filter(max_temp)
        last_filter = first_filter.objects.filter(min_temp)

    elif (query == '20to22'):
        items = models.Cloth.objects.filter(temp=query)
        first_filter = items.objects.filter(max_temp)
        last_filter = first_filter.objects.filter(min_temp)

    elif (query == '23to26'):
        items = models.Cloth.objects.filter(temp=query)
        first_filter = items.objects.filter(max_temp)
        last_filter = first_filter.objects.filter(min_temp)

    elif (query == '28to'):
        items = models.Cloth.objects.filter(temp=query)
        first_filter = items.objects.filter(max_temp)
        last_filter = first_filter.objects.filter(min_temp)


    print(last_filter)
    return render(request, "index.html", {"last_filter": last_filter})
