from django.contrib import admin

from .models import Osoba
from .models import Stanowisko

# Register your models here.


@admin.register(Osoba)
class AdminOsoba(admin.ModelAdmin):
    readonly_fields = [
        'data_dodania',
    ]


@admin.register(Stanowisko)
class AdminStanowisko(admin.ModelAdmin):
    pass
