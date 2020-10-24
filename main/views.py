from django.shortcuts import render
from .models import *


def home(request):
    return render(request, 'index.html')

# 전체 출력
def print(request):
    items = Cloth.objects.all()
    return render(request, "index.html", {"items": items})

# 온도 나눠서 가져오기 (checkbox)
def temperature(request, max_temp, min_temp):
    query = 'to4'
    # query = request.GET.get('query')

    if (query == 'to4'):  # ~3.999도
        items = models.Cloth.objects.filter(temp=query)
        first_filter_items = items.objects.filter(max_temp)
        last_filter_items = first_filter.objects.filter(min_temp)
        return render(request, "checkbox.html", {"last_filter_items": last_filter_items})

    elif (query == '4to8'): # 4이상 8미만
        items = models.Cloth.objects.filter(temp=query)
        first_filter_items = items.objects.filter(max_temp)
        last_filter_items = first_filter_items.objects.filter(min_temp)
        return render(request, "checkbox.html", {"last_filter_items": last_filter_items})

    elif (query == '8to11'):
        items = models.Cloth.objects.filter(temp=query)
        first_filter_items = items.objects.filter(max_temp)
        last_filter_items = first_filter_items.objects.filter(min_temp)
        return render(request, "checkbox.html", {"last_filter_items": last_filter_items})

    elif (query == '11to16'):
        items = models.Cloth.objects.filter(temp=query)
        first_filter_items = items.objects.filter(max_temp)
        last_filter_items = first_filter_items.objects.filter(min_temp)
        return render(request, "checkbox.html", {"last_filter_items": last_filter_items})

    elif (query == '16to19'):
        items = models.Cloth.objects.filter(temp=query)
        first_filter_items = items.objects.filter(max_temp)
        last_filter_items = first_filter_items.objects.filter(min_temp)
        return render(request, "checkbox.html", {"last_filter_items": last_filter_items})

    elif (query == '19to22'):
        items = models.Cloth.objects.filter(temp=query)
        first_filter_items = items.objects.filter(max_temp)
        last_filter_items = first_filter_items.objects.filter(min_temp)
        return render(request, "checkbox.html", {"last_filter_items": last_filter_items})

    elif (query == '22to26'):
        items = models.Cloth.objects.filter(temp=query)
        first_filter_items = items.objects.filter(max_temp)
        last_filter_items = first_filter_items.objects.filter(min_temp)
        return render(request, "checkbox.html", {"last_filter_items": last_filter_items})

    elif (query == '26to'):
        items = models.Cloth.objects.filter(temp=query)
        first_filter_items = items.objects.filter(max_temp)
        last_filter_items = first_filter.objects.filter(min_temp)
        return render(request, "checkbox.html", {"last_filter_items": last_filter_items})
