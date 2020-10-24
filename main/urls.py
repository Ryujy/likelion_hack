from django.contrib import admin
from django.urls import path
from main import views 

urlpatterns = [
    # path('', views.home, name="index"),
    # path('print/', views.print, name="print"), 
    # path('temp/', views.temperature, name="temp"),
    path('weather/',views.weather, name="weatherPage"),
   
    
]