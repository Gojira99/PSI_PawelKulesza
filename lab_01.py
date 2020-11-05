lorem_Ipsum = "Lorem Ipsum jest tekstem stosowanym jako przykładowy wypełniacz w poligraficznym." \
        "Został po raz pierwszy użyty w XV w. Przez nieznanego drukarza do wypełnienia tekstem próbnej książki." \
        "Pięć wieków zaczął być używany jako elektronicznym, pozostając niezmienionym później." \
        "Spopularyzował się w latach 60. XX w. Wraz z publikacją przewodnika" \
        "Letrasetu, niestety fragmenty Lorem Ipsum, a ostatnio z zawierającym różne wersje" \
        "Lorem Ipsum przeznaczonym do realizacji druków na komputerach osobistych, jak Aldus PageMaker"
imie = "Pawel"
nazwisko = "Kulesza"
litera_1 = imie[2]
litera_2 = nazwisko[3]
print(imie[:: -1].capitalize() + "" + nazwisko[:: -1].capitalize())
lista1 = []
lsita2 = []
a=[a for a in range(1,11)]
b=a[5:10]
print(b)
a[5:] = []
print(a)
a[5:]=b
a.insert(0,0)
a.sort(reverse=True)
print(a)
krotka1 = tuple(["Paweł Kulesza", 151223])
krotka2 = tuple(["Marian Kowalski", 151232])
krotka3 = tuple(["Wojciech Jabłonowski",666999])
war1 = [21,1999,"tom@gmail.com","Warszawa ul.Bukat 312/C"]
war2 = [21,1999,"tom4321432@gmail.com","Warszawa ul.Bukat 312/d"]
war3 = [22,1998,"tom41324213@gmail.com","Warszawa ul.Bukat 312/e"]
laczenie = [krotka1,krotka2,krotka3]
slownik = {krotka1:war1, krotka2:war2,krotka3:war3}
print(slownik)
telefony = [501333444,501333444,600800900]
lista = []
lista = set(telefony)
print(lista)
for i in range(1,11):
    print(i)
for j in reversed(range(20,101,5)):
        print(j)
slownik1 = {"Paweł":"Tanajno"}
slownik2 = {"Paweł":"Tramwajno"}
slownik3 = {"Piekny":"Mairan_Kowalski"}
lista = [slownik1,slownik2,slownik3]
print(lista)
