from django.contrib import admin
from django.urls import path
from main import views 

urlpatterns = [
    # path('', views.showGeneric, name="showGeneric"),
    # path('index/',views.home, name="index"),
    path('',views.weather, name="weatherPage")
]