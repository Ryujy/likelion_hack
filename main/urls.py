from django.contrib import admin
from django.urls import path
from main import views 

urlpatterns = [
<<<<<<< HEAD
    # path('', views.showGeneric, name="showGeneric"),
    # path('index/',views.home, name="index"),
    path('',views.weather, name="weatherPage")
=======
    path('', views.home, name="index"),
    path('', views.temperature),
>>>>>>> 8ce72b43dc7b8c8857b9dd5767786680afa992b8
]