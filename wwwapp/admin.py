from django.contrib import admin

from .models import Osoba
from .models import Stanowisko

# Register your models here.


@admin.register(Osoba)
class AdminOsoba(admin.ModelAdmin):
    pass


@admin.register(Stanowisko)
class AdminStanowisko(admin.ModelAdmin):
    pass
