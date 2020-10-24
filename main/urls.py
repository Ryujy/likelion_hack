from django.contrib import admin
from django.urls import path
from main import views 

urlpatterns = [
    path('weather/',views.weather, name="weatherPage"),   
    path('', views.home, name="index"),
    path('temperature/', views.temperature, name="temperature")

]