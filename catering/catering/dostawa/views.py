from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions, generics
from django.contrib.auth.models import User
from .models import *
from .serializer import *
from rest_framework.reverse import reverse

class KlientLista(generics.ListCreateAPIView):
    queryset = Klient.objects.all()
    serializer_class = KlientSerializer
    name = 'Klient-lista'
    filterset_fields = ['imie','nazwisko']
    search_fields = ['imie','nazwisko']
    ordering_fields = ['imie', 'nazwisko']
    def perform_create(self, serializer):

        serializer.save(wlasciciel=self.request.user)
    permission_classes = [permissions.IsAdminUser]
class KlientSczegoly(generics.RetrieveUpdateDestroyAPIView):
    queryset = Klient.objects.all()
    serializer_class = KlientSerializer
    name = 'klient-sczegoly'
    permission_classes = [permissions.IsAdminUser]
class LokalizacjaLista(generics.ListCreateAPIView):
    queryset = Lokalizacja.objects.all()
    serializer_class = LokalizacjaSerializer
    name = 'Lokalizacja-lista'
    filterset_fields = ['dystans', 'cena_lokalizacja']
    search_fields = ['dystans', 'cena_lokalizacja']
    ordering_fields = ['dystans', 'cena_lokalizacja']
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class LokalizacjaSczegoly(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lokalizacja.objects.all()
    serializer_class = LokalizacjaSerializer
    name = 'Lokalizacja-sczegoly'
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]



class ZamowienieLista(generics.ListCreateAPIView):
    queryset = Zamowienie.objects.all()
    serializer_class = ZamowienieSerializer
    name = "Zamowienie-Lista"
    filterset_fields = ['nazwa_potrawy', 'ilosc', 'koszt', 'data_zamoienia', 'Klient_Zamowienie', 'Lokalizacja_Zamowienie']
    search_fields = ['nazwa_potrawy', 'ilosc', 'koszt', 'data_zamoienia', 'Klient_Zamowienie', 'Lokalizacja_Zamowienie']
    ordering_fields = ['nazwa_potrawy', 'ilosc', 'koszt', 'data_zamoienia', 'Klient_Zamowienie', 'Lokalizacja_Zamowienie']

class ZamowienieSzczegoly(generics.RetrieveUpdateDestroyAPIView):
     queryset = Zamowienie.objects.all()
     serializer_class = ZamowienieSerializer
     name = 'Zamowienie-Szczegoly'


class Catering_dietetycznyLista(generics.ListCreateAPIView):
    queryset = Catering_dietetyczny.objects.all()
    serializer_class = Catering_dietetycznySerializer
    name = "Catering_dietetyczny-Lista"
    filterset_fields = ['rodzaj', 'liczba', 'liczba_kalori', 'cena', 'Zamowienie_Catering_dieteyczny']
    search_fields = ['rodzaj', 'liczba', 'liczba_kalori', 'cena', 'Zamowienie_Catering_dieteyczny']
    ordering_fields = ['rodzaj', 'liczba', 'liczba_kalori', 'cena', 'Zamowienie_Catering_dieteyczny']
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
class Catering_dietetycznySzczegoly(generics.RetrieveUpdateDestroyAPIView):
    queryset = Catering_dietetyczny.objects.all()
    serializer_class = Catering_dietetycznySerializer
    name = 'Catering_dietetyczny-Szczegoly'
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class MenuLista(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    name = 'Menu-lista'
    filterset_fields = ['nazwa_potrawyMenu', 'cenaMenu']
    search_fields = ['nazwa_potrawyMenu', 'cenaMenu']
    ordering_fields = ['nazwa_potrawyMenu', 'cenaMenu']
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
class MenuSczegoly(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    name = 'Menu-Szczegoly'
    permission_classes = [permissions.IsAdminUser]
class PlatnoscLista(generics.ListCreateAPIView):
    queryset = Platnosc.objects.all()
    serializer_class = PlatnoscSerializer
    name = 'Platnosc-lista'
    filterset_fields = ['rodzaj_Platnosci', 'kwota', 'Klient_Platnosc']
    search_fields = ['rodzaj_Platnosci', 'kwota', 'Klient_Platnosc']
    ordering_fields = ['rodzaj_Platnosci', 'kwota', 'Klient_Platnosc']

class PlatnoscSczegoly(generics.RetrieveUpdateDestroyAPIView):
    queryset = Platnosc.objects.all()
    serializer_class = PlatnoscSerializer



    name = 'Platnosc-Szczegoly'


class ApiRoot(generics.GenericAPIView):
    name = 'api-root'
    def get(self, request, *args, **kwargs):
        return Response({'Klient': reverse(KlientLista.name, request=request),
                         'Lokazizacja': reverse(LokalizacjaLista.name, request=request),
                         'Zamowienie':reverse(ZamowienieLista.name, request=request),
                         'Catering_dietetyczny': reverse(Catering_dietetycznyLista.name, request=request),
                         'Menu': reverse(MenuLista.name, request=request),
                         'Platnosc': reverse(PlatnoscLista.name, request=request),
        })