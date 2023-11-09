# Django
from django.urls import path
from .views import osoba_detail
from .views import osoba_list
from .views import stanowisko_detail
from .views import stanowisko_list

app_name = 'wwwapp'

urlpatterns = [
    path('osoby/', osoba_list),
    path('osoby/<int:pk>/', osoba_detail),
    path('stanowiska/', stanowisko_list),
    path('stanowiska/<int:pk>/', stanowisko_detail),
]
