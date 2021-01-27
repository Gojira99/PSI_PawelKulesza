from rest_framework import serializers
from dostawa.models import Klient, Lokalizacja, Zamowienie, Catering_dietetyczny, Menu, Platnosc
from django.contrib.auth.models import User

class KlientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Klient
        fields = ['imie', 'nazwisko', 'ulica', 'miasto', 'nr_telefonu',]


class LokalizacjaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lokalizacja
        fields = ['dystans','cena_lokalizacja']

class ZamowienieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zamowienie
        fields = ['nazwa_potrawy', 'ilosc', 'koszt', 'data_zamoienia', 'Klient_Zamowienie', 'Lokalizacja_Zamowienie']

class Catering_dietetycznySerializer(serializers.ModelSerializer):
    class Meta:
        model = Catering_dietetyczny
        fields = ['rodzaj', 'liczba', 'liczba_kalori', 'cena']

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['nazwa_potrawyMenu', 'cenaMenu']

class PlatnoscSerializer(serializers.ModelSerializer):
    Klient_Platnosc = serializers.SlugRelatedField(queryset=Klient.objects.all(), slug_field='ulica')
    class Meta:



        model = Platnosc
        fields = ['rodzaj_Platnosci', 'kwota', 'Klient_Platnosc']

