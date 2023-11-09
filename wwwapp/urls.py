# Django
from django.urls import path
from .views import OsobaDetail
from .views import OsobaList
from .views import StanowiskoList
from .views import StanowiskoDetail

app_name = 'wwwapp'

urlpatterns = [
    path('osoby/', OsobaList.as_view(), name='osoba_list'),
    path('osoby/<int:pk>/', OsobaDetail.as_view(), name='osoba_detail'),
    path('stanowiska/', StanowiskoList.as_view(), name='stanowisko_list'),
    path('stanowiska/<int:pk>/', StanowiskoDetail.as_view(), name='stanowisko_detail'),
]
