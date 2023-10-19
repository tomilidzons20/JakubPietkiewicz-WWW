from django.contrib import admin

from .models import Osoba
from .models import Stanowisko

# Register your models here.


@admin.register(Osoba)
class AdminOsoba(admin.ModelAdmin):
    list_display = [
        'imie',
        'nazwisko',
        'stanowisko_admin',
    ]
    readonly_fields = [
        'data_dodania',
    ]
    list_filter = [
        'stanowisko',
        'data_dodania',
    ]


@admin.register(Stanowisko)
class AdminStanowisko(admin.ModelAdmin):
    list_filter = [
        'nazwa',
    ]
