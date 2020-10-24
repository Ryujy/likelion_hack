from django.contrib import admin
from django.urls import path
from main import views 

urlpatterns = [
    path('', views.home, name="index"),
    path('print/', views.print), # print all
    path('temp/', views.temperature), # print checkbox
]