from django.contrib import admin
from django.urls import path
from main import views 

urlpatterns = [
<<<<<<< HEAD
    # path('', views.home, name="index"),
    # path('print/', views.print, name="print"), 
    # path('temp/', views.temperature, name="temp"),
    path('weather/',views.weather, name="weatherPage"),
   
    
=======
<<<<<<< HEAD
    # path('', views.showGeneric, name="showGeneric"),
    # path('index/',views.home, name="index"),
    path('',views.weather, name="weatherPage")
=======
    path('', views.home, name="index"),
<<<<<<< HEAD
    path('print/', views.print), # print all
    path('temp/', views.temperature), # print checkbox
=======
    path('', views.temperature),
>>>>>>> 8ce72b43dc7b8c8857b9dd5767786680afa992b8
>>>>>>> cb3488b9cb6ab8d9777f84bced4db3ce9463d9fb
>>>>>>> 435619e6dfa9cd0bc55fe8b8727adf8b215486fc
]