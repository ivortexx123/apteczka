import csv
from datetime import datetime

class Lek:
    def __init__(self, nazwa, producent, jednostki_chorobowe, dla_kogo, substancje_czynne, zalecany_wiek, liczba_dawek, liczba_dostepnych_dawek, termin_waznosci, notatka):
        self.nazwa = nazwa
        self.producent = producent
        self.jednostki_chorobowe = jednostki_chorobowe
        self.dla_kogo = dla_kogo
        self.substancje_czynne = substancje_czynne
        self.zalecany_wiek = zalecany_wiek
        self.liczba_dawek = liczba_dawek
        self.liczba_dostepnych_dawek = liczba_dostepnych_dawek
        self.termin_waznosci = termin_waznosci
        self.notatka = notatka

    def jest_przeterminowany(self):
        return datetime.strptime(self.termin_waznosci, '%d-%m-%Y') < datetime.now()

    def edytuj(self, nazwa=None, producent=None, jednostki_chorobowe=None, dla_kogo=None, substancje_czynne=None, zalecany_wiek=None, liczba_dawek=None, liczba_dostepnych_dawek=None, termin_waznosci=None, notatka=None):
        if nazwa is not None:
            self.nazwa = nazwa
        if producent is not None:
            self.producent = producent
        if jednostki_chorobowe is not None:
            self.jednostki_chorobowe = jednostki_chorobowe
        if dla_kogo is not None:
            self.dla_kogo = dla_kogo
        if substancje_czynne is not None:
            self.substancje_czynne = substancje_czynne
        if zalecany_wiek is not None:
            self.zalecany_wiek = zalecany_wiek
        if liczba_dawek is not None:
            self.liczba_dawek = liczba_dawek
        if liczba_dostepnych_dawek is not None:
            self.liczba_dostepnych_dawek = liczba_dostepnych_dawek
        if termin_waznosci is not None:
            self.termin_waznosci = termin_waznosci
        if notatka is not None:
            self.notatka = notatka

    def __str__(self):
        return (f"Lek: {self.nazwa}\n"
                f"Producent: {self.producent}\n"
                f"Jednostki chorobowe: {', '.join(self.jednostki_chorobowe)}\n"
                f"Dla kogo: {', '.join(self.dla_kogo)}\n"
                f"Substancje czynne: {', '.join(self.substancje_czynne)}\n"
                f"Zalecany wiek: {self.zalecany_wiek}\n"
                f"Liczba dawek: {self.liczba_dawek}\n"
                f"Liczba dostępnych dawek: {self.liczba_dostepnych_dawek}\n"
                f"Termin ważności: {self.termin_waznosci}\n"
                f"Notatka: {self.notatka}\n")

class LekPrzyjmowany:
    def __init__(self, lek, dawka, dzien):
        self.lek = lek
        self.dawka = dawka
        self.dzien = dzien

    def __str__(self):
        return f"{self.lek.nazwa} - Dawka: {self.dawka} - Dzień: {self.dzien}"

class Uzytkownik:
    def __init__(self, imie, wiek, jednostki_chorobowe, uczulenia, leki_przyjmowane):
        self.imie = imie
        self.wiek = wiek
        self.jednostki_chorobowe = jednostki_chorobowe
        self.uczulenia = uczulenia
        # Sprawdzanie, czy leki przyjmowane są zgodne z klasą LekPrzyjmowany
        self.leki_przyjmowane = []
        for lek_przyjmowany in leki_przyjmowane:
            if isinstance(lek_przyjmowany, LekPrzyjmowany):
                self.leki_przyjmowane.append(lek_przyjmowany)
            else:
                raise ValueError("Każdy element leki_przyjmowane musi być instancją klasy LekPrzyjmowany")

    def dodaj_lek_przyjmowany(self, lek_przyjmowany):
        if isinstance(lek_przyjmowany, LekPrzyjmowany):
            self.leki_przyjmowane.append(lek_przyjmowany)
        else:
            raise ValueError("Dodawany lek musi być instancją klasy LekPrzyjmowany")

    def edytuj(self, imie=None, wiek=None, jednostki_chorobowe=None, uczulenia=None, leki_przyjmowane=None):
        if imie is not None:
            self.imie = imie
        if wiek is not None:
            self.wiek = wiek
        if jednostki_chorobowe is not None:
            self.jednostki_chorobowe = jednostki_chorobowe
        if uczulenia is not None:
            self.uczulenia = uczulenia
        if leki_przyjmowane is not None:
            for lek_przyjmowany in leki_przyjmowane:
                if isinstance(lek_przyjmowany, LekPrzyjmowany):
                    self.leki_przyjmowane = leki_przyjmowane
                else:
                    raise ValueError("Każdy element leki_przyjmowane musi być instancją klasy LekPrzyjmowany")

    def __str__(self):
        return (f"Użytkownik: {self.imie}\n"
                f"Wiek: {self.wiek}\n"
                f"Jednostki chorobowe: {', '.join(self.jednostki_chorobowe)}\n"
                f"Uczulenia: {', '.join(self.uczulenia)}\n"
                f"Leki przyjmowane: {', '.join([str(lek_przyjmowany) for lek_przyjmowany in self.leki_przyjmowane])}\n")

class Apteczka:
    def __init__(self):
        self.leki = []
        self.uzytkownicy = []

    def dodaj_lek(self, lek):
        self.leki.append(lek)

    def usun_lek(self, nazwa_leku):
        self.leki = [lek for lek in self.leki if lek.nazwa != nazwa_leku]

    def znajdz_lek(self, nazwa_leku):
        for lek in self.leki:
            if lek.nazwa == nazwa_leku:
                return lek
        return None

    def dodaj_uzytkownika(self, uzytkownik):
        self.uzytkownicy.append(uzytkownik)

    def usun_uzytkownika(self, imie):
        self.uzytkownicy = [uzytkownik for uzytkownik in self.uzytkownicy if uzytkownik.imie != imie]

    def wczytaj_baze(self, plik):
        with open(plik, newline='') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=';')
            for row in reader:
                lek = Lek(
                    row['nazwa'], row['producent'], row['jednostki_chorobowe'].split(';'),
                    row['dla_kogo'].split(';'), row['substancje_czynne'].split(';'),
                    int(row['zalecany_wiek']), int(row['liczba_dawek']),
                    int(row['liczba_dostepnych_dawek']), row['termin_waznosci'], row['notatka']
                )
                self.dodaj_lek(lek)

    def zapisz_baze(self, plik):
        with open(plik, 'w', newline='') as csvfile:
            fieldnames = ['nazwa', 'producent', 'jednostki_chorobowe', 'dla_kogo', 'substancje_czynne',
                          'zalecany_wiek', 'liczba_dawek', 'liczba_dostepnych_dawek', 'termin_waznosci', 'notatka']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=';')
            writer.writeheader()
            for lek in self.leki:
                writer.writerow({
                    'nazwa': lek.nazwa,
                    'producent': lek.producent,
                    'jednostki_chorobowe': ';'.join(lek.jednostki_chorobowe),
                    'dla_kogo': ';'.join(lek.dla_kogo),
                    'substancje_czynne': ';'.join(lek.substancje_czynne),
                    'zalecany_wiek': lek.zalecany_wiek,
                    'liczba_dawek': lek.liczba_dawek,
                    'liczba_dostepnych_dawek': lek.liczba_dostepnych_dawek,
                    'termin_waznosci': lek.termin_waznosci,
                    'notatka': lek.notatka
                })

    def przypomnij_przeterminowane(self):
        przeterminowane = [lek for lek in self.leki if lek.jest_przeterminowany()]
        if przeterminowane:
            print("Przeterminowane leki:")
            for lek in przeterminowane:
                print(f"{lek.nazwa} (termin ważności: {lek.termin_waznosci})")
        else:
            print("Brak przeterminowanych leków.")

    def sprawdz_bezpieczenstwo(self, lek, uzytkownik):
        if uzytkownik.wiek < lek.zalecany_wiek:
            return False
        for uczulenie in uzytkownik.uczulenia:
            if uczulenie in lek.substancje_czynne:
                return False
        return True

    def harmonogram_przyjmowania(self):
        for uzytkownik in self.uzytkownicy:
            print(f"\nHarmonogram przyjmowania leków dla {uzytkownik.imie}:")
            for lek_przyjmowany in uzytkownik.leki_przyjmowane:
                print(f"{lek_przyjmowany['lek']} - Dawka: {lek_przyjmowany['dawka']} - Dzień: {lek_przyjmowany['dzien']}")



# Przykład użycia
apteczka = Apteczka()
lek1 = Lek("Paracetamol", "XYZ Pharma", ["gorączka", "ból"], ["mama", "tata"], ["paracetamol"], 12, 10, 8, "31-12-2024", "na gorączkę")
lek2 = Lek("Ibuprofen", "ABC Pharma", ["ból", "zapal"], ["tata"], ["ibuprofen"], 12, 20, 20, "30-06-2025", "na ból")


uzytkownik1 = Uzytkownik("mama", 35, ["nadciśnienie"], ["paracetamol"], [{"lek": "Paracetamol", "dawka": "1 tabletka", "dzien": "poniedziałek"}])
uzytkownik2 = Uzytkownik("tata", 40, ["cholesterol"], ["ibuprofen"], [{"lek": "Ibuprofen", "dawka": "1 tabletka", "dzien": "wtorek"}])


apteczka.dodaj_lek(lek1)
apteczka.dodaj_lek(lek2)

print("Przed edycją:")
print(lek1)

# Edytowanie leku
lek_do_edytowania = apteczka.znajdz_lek("Paracetamol")
if lek_do_edytowania:
    lek_do_edytowania.edytuj(producent="Nowy Producent", liczba_dostepnych_dawek=5)

print("Po edycją:")
print(lek1)
