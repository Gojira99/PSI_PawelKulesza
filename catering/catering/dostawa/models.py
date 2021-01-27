from django.db import models
from django.contrib.auth.models import User

class Klient(models.Model):
    imie = models.CharField(max_length=45,)
    nazwisko = models.CharField(max_length=45, null=True)
    ulica = models.CharField(max_length=45, null=True)
    miasto = models.CharField(max_length=45, null=True )
    nr_telefonu = models.IntegerField(null=True)
    wlasciciel = models.ForeignKey('auth.User', on_delete=models.CASCADE, default='Admin')

    class Meta:
        ordering = ('nazwisko',)

    def __str__(self):
        return str(self.imie) + " " + str(self.nazwisko) + " " + str(self.nr_telefonu)


class Lokalizacja(models.Model):
    dystans = models.FloatField()
    cena_lokalizacja = models.FloatField(null=True)
    class Meta:
        ordering = ('dystans',)
    def __str__(self):
        return "Odległość: " + str(self.dystans) + " Cena: " + str(self.cena_lokalizacja)

class Menu(models.Model):
    nazwa_potrawyMenu = models.CharField(max_length=45, null=True)
    cenaMenu = models.FloatField(null=True)

    class Meta:
        ordering = ('nazwa_potrawyMenu',)

    def __str__(self):
        return   str(self.nazwa_potrawyMenu) + " Cena" + str(self.cenaMenu)





class Zamowienie(models.Model):
    nazwa_potrawy = models.CharField(max_length=45)
    ilosc = models.IntegerField(null=False)
    koszt = models.FloatField(null=False)
    data_zamoienia = models.DateField(null=False)
    Klient_Zamowienie = models.ForeignKey(Klient, on_delete=models.CASCADE, null=False)
    Lokalizacja_Zamowienie = models.ForeignKey(Lokalizacja, models.CASCADE, null=False)


    def __str__(self):
        return str(Menu.nazwa_potrawyMenu) + str(Menu.cenaMenu) +"zł"

    class Meta:
        ordering = ('nazwa_potrawy',)

class Catering_dietetyczny(models.Model):
    rodzaj = models.CharField(max_length=45)
    liczba = models.IntegerField(null=False)
    liczba_kalori = models.IntegerField(null=False)
    cena = models.FloatField(null=False)
    Zamowienie_Catering_dieteyczny = models.ForeignKey(Zamowienie,on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ('rodzaj',)

    def __str__(self):
        return str(self.rodzaj) + " " + str(self.liczba_kalori) + " " + str(self.cena)

class Platnosc(models.Model):
    KARTA = 'K'
    GOTOWKA = 'G'
    BLIK = 'B'

    platnosc_wybor = ((KARTA, 'Karta'), (GOTOWKA, 'Gotowka'), (BLIK, 'Blik'),)
    rodzaj_Platnosci = models.CharField(

        max_length=1,
        choices=platnosc_wybor,
        default='Brak'
    )
    kwota = models.FloatField(null=False)
    Klient_Platnosc = models.ForeignKey(Klient, on_delete=models.CASCADE, null=False)

