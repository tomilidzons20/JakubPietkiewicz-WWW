from django.contrib import admin
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


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
        default=PLCI.MEZCZYZNA,
    )
    stanowisko = models.ForeignKey(
        'Stanowisko',
        on_delete=models.CASCADE,
    )
    data_dodania = models.DateField(
        default=timezone.now().date(),
    )
    wlasciciel = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    def __str__(self):
        return f'{self.imie} {self.nazwisko}'

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
