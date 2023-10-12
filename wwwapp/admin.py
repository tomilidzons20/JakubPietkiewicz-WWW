from django.contrib import admin

from .models import Person
from .models import Team

# Register your models here.


@admin.register(Person)
class AdminPerson(admin.ModelAdmin):
    pass


@admin.register(Team)
class AdminTeam(admin.ModelAdmin):
    pass
