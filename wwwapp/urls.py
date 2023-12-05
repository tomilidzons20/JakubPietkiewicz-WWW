# Django
from django.urls import path
from .views import osoba_get
from .views import osoba_put
from .views import osoba_delete
from .views import osoba_list
from .views import stanowisko_detail
from .views import stanowisko_list
from .views import osoba_stanowisko
from .views import osoba_view
from .views import OsobaListView
from .views import test_view

app_name = 'wwwapp'

urlpatterns = [
    path('osoby/', osoba_list, name='osoby'),
    path('osoby/put/<int:pk>/', osoba_put),
    path('osoby/delete/<int:pk>/', osoba_delete),
    path('osoby/<int:pk>/', osoba_get),
    path('stanowiska/', stanowisko_list),
    path('stanowiska/<int:pk>/', stanowisko_detail),
    path('stanowisko/<int:pk>/members/', osoba_stanowisko, name='osoba_stanowisko'),
    path('osoba/view/', osoba_view),
    path('osoba/list/', OsobaListView.as_view()),
    path('test/', test_view, name='test'),
]
