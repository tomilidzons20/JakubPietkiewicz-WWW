from django.db import models
from django.utils import timezone

# Create your models here.


class Osoba(models.Model):
    PLCI = (
        ('M', 'Mężczyzna'),
        ('K', 'Kobieta'),
        ('I', 'Inne'),
    )

    imie = models.CharField(
        blank=False,
    )
    nazwisko = models.CharField(
        blank=False,
    )
    plec = models.CharField(
        choices=PLCI,
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


class Stanowisko(models.Model):
    nazwa = models.CharField(
        blank=False,
    )
    opis = models.CharField(
        blank=True,
    )

    def __str__(self):
        return self.nazwa
