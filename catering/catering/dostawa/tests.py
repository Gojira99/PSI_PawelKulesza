from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework.reverse import reverse
from . import views
from .models import *
from rest_framework import status
from django.utils.http import urlencode
from django import urls




# Create your tests here.
# dystans cena_lokalizacja

class KlienetTests(APITestCase):


    def post_klient(self, imie):
        url = reverse(views.KlientLista.name)
        data = {'imie':imie}
        response = self.client.post(url, data, format='json')
        return response

    def test_post_and_get_klient(self):
        nowe_imie = 'Pawel'
        response = self.post_klient(nowe_imie)
        print("PK {0}".format(Klient.objects.get().pk))
        assert response.status_code == status.HTTP_201_CREATED
        assert Klient.objects.count() == 1
        assert  Klient.objects.get().imie == nowe_imie


class ListaTests(APITestCase):

    def post_lokalizacja(self, dystans):
        url = reverse(views.LokalizacjaLista.name)
        data = {'dystans':dystans}
        response = self.client.post(url, data, format='json')
        return response
    def test_post_and_get_lokalizacja(self):
        nowa_lokalizacja = 5.00
        response = self.post_lokalizacja(nowa_lokalizacja)
        print("PK {0}".format(Lokalizacja.objects.get().pk))
        assert response.status_code == status.HTTP_201_CREATED
        assert Lokalizacja.objects.count() == 1
        assert Lokalizacja.objects.get().dystans == nowa_lokalizacja