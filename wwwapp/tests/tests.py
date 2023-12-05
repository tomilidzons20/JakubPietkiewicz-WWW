import datetime

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from rest_framework.test import APIClient

from ..models import Osoba
from ..models import Stanowisko


class PersonModelTest(TestCase):
    def setUp(cls):
        Osoba.objects.create(imie='Jan', nazwisko='L')

    def test_first_name_label(self):
        osoba = Osoba.objects.get()
        field_label = osoba._meta.get_field('imie').verbose_name
        self.assertEqual(field_label, 'imie')

    def test_stanowisko_id(self):
        stanowisko = Stanowisko.objects.create(nazwa='krol', opis='wladca')
        osoba = Osoba.objects.get()
        osoba.stanowisko = stanowisko
        osoba.save()
        self.assertEqual(stanowisko.id, osoba.stanowisko.id)

    def test_data_dodania(self):
        osoba = Osoba.objects.get()
        self.assertEqual(osoba.data_dodania, datetime.date.today())


class ExampleViewTest(TestCase):
    def test_get(self):
        response = self.client.get(reverse('wwwapp:test'))
        self.assertEqual(response.status_code, 200)

    def test_post(self):
        response = self.client.post(reverse('wwwapp:test'))
        self.assertEqual(response.status_code, 201)


client = APIClient()


class OsobyTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='test', password='12345')
        Token.objects.create(user=self.user)
        self.stanowisko = Stanowisko.objects.create(nazwa='krol')

    def test_create_osoba(self):
        url = reverse('wwwapp:osoby')
        data = [{
            'imie': 'Mirek',
            'nazwisko': 'Miras',
        }]
        client.force_authenticate(user=self.user)
        response = client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Osoba.objects.count(), 1)
        self.assertEqual(Osoba.objects.get().imie, 'Mirek')
        client.force_authenticate(user=None)

    def test_token_auth(self):
        url = reverse('wwwapp:osoba_stanowisko', kwargs={'pk': self.stanowisko.id})
        response = client.get(url, headers={'AUTHORIZATION': f'Bearer {self.user.auth_token}'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

