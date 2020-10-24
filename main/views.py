from django.shortcuts import render
from .models import *

def home(request):
    return render(request, 'index.html')

# 온도 나눠서 가져오기
def temperature(request, max_temp, min_temp):
    # query = 10
    query = request.GET.get('query')

    # # query가 있으면
    # if not (query == None or  query == ''):
    #     first_filter = items.filter(temp_name = query)
    #     second_filter = first_filter.objects.filter(max_temp)
    #     last_filter = second_filter.objects.filter(min_temp)


    if (query == 'to4'):  # ~3.999도
        items = models.Cloth.objects.filter(temp=query)
        first_filter = items.objects.filter(max_temp)
        last_filter = first_filter.objects.filter(min_temp)

    elif (query == '4to8'): # 4이상 8미만
        items = models.Cloth.objects.filter(temp=query)
        first_filter = items.objects.filter(max_temp)
        last_filter = first_filter.objects.filter(min_temp)

    elif (query == '8to11'):
        items = models.Cloth.objects.filter(temp=query)
        first_filter = items.objects.filter(max_temp)
        last_filter = first_filter.objects.filter(min_temp)

    elif (query == '11to16'):
        items = models.Cloth.objects.filter(temp=query)
        first_filter = items.objects.filter(max_temp)
        last_filter = first_filter.objects.filter(min_temp)

    elif (query == '16to19'):
        items = models.Cloth.objects.filter(temp=query)
        first_filter = items.objects.filter(max_temp)
        last_filter = first_filter.objects.filter(min_temp)

    elif (query == '19to22'):
        items = models.Cloth.objects.filter(temp=query)
        first_filter = items.objects.filter(max_temp)
        last_filter = first_filter.objects.filter(min_temp)

    elif (query == '22to26'):
        items = models.Cloth.objects.filter(temp=query)
        first_filter = items.objects.filter(max_temp)
        last_filter = first_filter.objects.filter(min_temp)

    elif (query == '26to'):
        items = models.Cloth.objects.filter(temp=query)
        first_filter = items.objects.filter(max_temp)
        last_filter = first_filter.objects.filter(min_temp)

    return render(request, "index.html", {"last_filter": last_filter})
