from django.contrib import admin
from django.db import models

# Create your models here.


class Osoba(models.Model):
    class PLCI(models.IntegerChoices):
        MEZCZYZNA = 1
        KOBIETA = 2
        INNE = 3

    imie = models.CharField(
        blank=False,
    )
    nazwisko = models.CharField(
        blank=False,
    )
    plec = models.IntegerField(
        choices=PLCI.choices,
    )
    stanowisko = models.ForeignKey(
        'Stanowisko',
        on_delete=models.CASCADE,
    )
    data_dodania = models.DateField(
        auto_now_add=True,
    )

    def __str__(self):
        return f'{self.imie} {self.nazwisko}'

    @admin.display(description='Stanowisko')
    def stanowisko_admin(self):
        return f'{self.stanowisko.nazwa} ({self.stanowisko.id})'

    class Meta:
        ordering = [
            'nazwisko'
        ]


class Stanowisko(models.Model):
    nazwa = models.CharField(
        blank=False,
    )
    opis = models.CharField(
        blank=True,
    )

    def __str__(self):
        return self.nazwa
