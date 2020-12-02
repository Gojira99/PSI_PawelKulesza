import  random

#1
#Stwórz funkcję, która jako parametry przyjmuje dwie listy a_list oraz b_list. Następnie
#zwróć listę, która będzie posiadać parzyste indeksy z listy a_list oraz nieparzyste z b_list

def random_liczby(lsita, liczba_elememtow,zakres_od, zakres_do):
    for i in range(liczba_elememtow):
        lsita.append(random.randrange(zakres_od, zakres_do))

lista = list()
random_liczby(lista , 3,5,23)
#print(lista)
#2
#Stwórz funkcję, która przyjmuje parametr data_text, a następnie zwróci następujące informacje o parametrze w formie słownika (dict):
#length: długość podanego tekstu,
#letters: lista znaków w wyrazie np. ['D', 'o', 'g'],
#big_letters: zamieniony parametr w kapitaliki np. DOG
#small_letters: zamieniony parametr w małe litery np. dog

def info(data_text):
    dlugosc = len(data_text)
    litery = list()
    for i in range(dlugosc):
        litery.append(data_text[i])

    duze_litery = data_text.upper()
    male_litery = data_text.lower()

    dane = \
    {
        'dlugosc': dlugosc,
        'litery': litery,
        'male_litery': male_litery,
        'duze_litery': duze_litery
    }
    return dane
def Slownik(slownik):
    for klucz, wartosc in slownik.items():
        print("{} : {}".format(str(klucz), str(wartosc)))


tekst = "gsakgwgwSAFGDASGWEgdasfsdafwefA"
og = info(tekst)
Slownik(og)

#Stwórz funkcję, która przyjmie jako parametry text oraz letter,
#a następnie zwróci wynik usunięcia wszytkich wystąpień wartości w letter z tekstu text
def usun(tekst, litery):
    litera = str(litery)
    usuwanko = tekst.replace(litera.upper(),"").replace((litera.lower()),"")
    return usuwanko
modyfikacja = usun(tekst,"k")
print(modyfikacja)

#Stwórz funkcję, która przelicza temperaturę w stopniach Celsjusza na
#Fahrenheit, Rankine, Kelvin. Typ konwersji powinien być
#przekazany w parametrze temperature_type i uwzględniać błędne wartości.

def temperatura(temp, temp_type):
    temeratura = format(temp)
    kelin = temeratura + 273.15
    fahrenheit = ((9 / 5) * temperatura) + 32
    rankine = fahrenheit + 459, 67
    if temp_type == "far":
        return fahrenheit
    elif temp_type == "ran":
        return rankine
    elif temp_type == "kel":
        return kelin

#cel = float(input("Podaj tempertaure"))
#print("kelin = kel, fara = far, ran = ran")
#typ = str()
#while typ != "kel" or typ != "far" or typ !="ran":
#    typ = input("Podaj na jaka skale chcesz zamianić kelin = kel, fara = far, ran = ran" )

#print(temperatura(cel, typ))

#5Stwórz klasę Calculator, która będzie posiadać funkcje add,
#difference, multiply, divide.

class Calculator:

    def __init__(self,liczba1,liczba2):
        self.liczba1 = liczba1
        self.liczba2 = liczba2
    def add(self):
        print(self.liczba1+self.liczba2)

    def difference(self):
        print(self.liczba1-self.liczba2)
    def multiply(self):
        print(self.liczba1*self.liczba2)
    def divine(self):
        if(self.liczba2 ==0):
            print("Nie dziel przez 0")
        else:
            print(self.liczba1 / self.liczba2)

#6 Stwórz klasę ScienceCalculator, która dziedziczy po klasie Calculator i
# dodaj dodatkowe funkcje np. potęgowanie.
class Sincecalculator(Calculator):
    def wlasna(self):
        print(pow(self.liczba1,self.liczba2))

cal = Sincecalculator(1,2)
cal.add()
cal.difference()
cal.divine()
cal.wlasna()
#7 Stwórz funkcję, która wypisuje podany tekst od tyłu np. koteł -> łetok.

def wspak(slowo):
    slowo = slowo[::-1]
    return slowo
print(wspak("Ivan Komarenko"))


