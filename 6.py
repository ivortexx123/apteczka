import csv
from datetime import datetime

class Lek:
    def __init__(self, nazwa, producent, jednostki_chorobowe, dla_kogo, substancje_czynne, zalecany_wiek, liczba_dawek,
                 liczba_dostepnych_dawek, termin_waznosci, notatka):
        if (not isinstance(nazwa, str) or
            not isinstance(producent, str) or
            not isinstance(jednostki_chorobowe, list) or
            not isinstance(dla_kogo, list) or
            not isinstance(substancje_czynne, list) or
            not isinstance(zalecany_wiek, int) or not isinstance(liczba_dawek, int) or
            not isinstance(liczba_dostepnych_dawek, int) or
            not isinstance(notatka, str)):
            raise ValueError("Podane zmienne muszą być w odpowiednich formatach")
        try:
            datetime.strptime(termin_waznosci, '%d-%m-%Y')
        except ValueError:
            raise ValueError("Termin ważności musi być w formacie dd-mm-YYYY")

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

    def edytuj(self, nazwa=None, producent=None, jednostki_chorobowe=None, dla_kogo=None, substancje_czynne=None,
               zalecany_wiek=None, liczba_dawek=None, liczba_dostepnych_dawek=None, termin_waznosci=None, notatka=None):
        if nazwa is not None and not isinstance(nazwa, str):
            raise ValueError("Nazwa musi być ciągiem znaków")
        if producent is not None and not isinstance(producent, str):
            raise ValueError("Producent musi być ciągiem znaków")
        if jednostki_chorobowe is not None and not isinstance(jednostki_chorobowe, list):
            raise ValueError("Jednostki chorobowe muszą być listą")
        if dla_kogo is not None and not isinstance(dla_kogo, list):
            raise ValueError("Dla kogo musi być listą")
        if substancje_czynne is not None and not isinstance(substancje_czynne, list):
            raise ValueError("Substancje czynne muszą być listą")
        if zalecany_wiek is not None and not isinstance(zalecany_wiek, int):
            raise ValueError("Zalecany wiek musi być liczbą całkowitą")
        if liczba_dawek is not None and not isinstance(liczba_dawek, int):
            raise ValueError("Liczba dawek musi być liczbą całkowitą")
        if liczba_dostepnych_dawek is not None and not isinstance(liczba_dostepnych_dawek, int):
            raise ValueError("Liczba dostępnych dawek musi być liczbą całkowitą")
        if termin_waznosci is not None:
            try:
                datetime.strptime(termin_waznosci, '%d-%m-%Y')
            except ValueError:
                raise ValueError("Termin ważności musi być w formacie dd-mm-YYYY")
        if notatka is not None and not isinstance(notatka, str):
            raise ValueError("Notatka musi być ciągiem znaków")

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
        if not isinstance(lek, Lek):
            raise ValueError("Lek musi być instancją klasy Lek")
        if not isinstance(dawka, str):
            raise ValueError("Dawka musi być ciągiem znaków")
        if not isinstance(dzien, str):
            raise ValueError("Dzień musi być ciągiem znaków")

        self.lek = lek
        self.dawka = dawka
        self.dzien = dzien

    def __str__(self):
        return f"{self.lek.nazwa} - Dawka: {self.dawka} - Dzień: {self.dzien}"


class Uzytkownik:
    def __init__(self, imie, wiek, jednostki_chorobowe, uczulenia, leki_przyjmowane):
        if not isinstance(imie, str):
            raise ValueError("Imię musi być ciągiem znaków")
        if not isinstance(wiek, int):
            raise ValueError("Wiek musi być liczbą całkowitą")
        if not isinstance(jednostki_chorobowe, list):
            raise ValueError("Jednostki chorobowe muszą być listą")
        if not isinstance(uczulenia, list):
            raise ValueError("Uczulenia muszą być listą")
        if not isinstance(leki_przyjmowane, list):
            raise ValueError("Leki przyjmowane muszą być listą")

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
        if imie is not None and not isinstance(imie, str):
            raise ValueError("Imię musi być ciągiem znaków")
        if wiek is not None and not isinstance(wiek, int):
            raise ValueError("Wiek musi być liczbą całkowitą")
        if jednostki_chorobowe is not None and not isinstance(jednostki_chorobowe, list):
            raise ValueError("Jednostki chorobowe muszą być listą")
        if uczulenia is not None and not isinstance(uczulenia, list):
            raise ValueError("Uczulenia muszą być listą")
        if leki_przyjmowane is not None:
            for lek_przyjmowany in leki_przyjmowane:
                if not isinstance(lek_przyjmowany, LekPrzyjmowany):
                    raise ValueError("Każdy element leki_przyjmowane musi być instancją klasy LekPrzyjmowany")
            self.leki_przyjmowane = leki_przyjmowane

        if imie is not None:
            self.imie = imie
        if wiek is not None:
            self.wiek = wiek
        if jednostki_chorobowe is not None:
            self.jednostki_chorobowe = jednostki_chorobowe
        if uczulenia is not None:
            self.uczulenia = uczulenia

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
        if not isinstance(lek, Lek):
            raise ValueError("Dodawany lek musi być instancją klasy Lek")
        self.leki.append(lek)

    def usun_lek(self, nazwa_leku):
        if not isinstance(nazwa_leku, str):
            raise ValueError("Nazwa leku musi być ciągiem znaków")
        poczatkowa_dlugosc = len(self.leki)
        self.leki = [lek for lek in self.leki if lek.nazwa != nazwa_leku]
        if len(self.leki) == poczatkowa_dlugosc:
            print(f"Leku o nazwie {nazwa_leku} nie znaleziono. Nic nie usunięto.")

    def znajdz_lek(self, nazwa_leku):
        if not isinstance(nazwa_leku, str):
            raise ValueError("Nazwa leku musi być ciągiem znaków")
        for lek in self.leki:
            if lek.nazwa == nazwa_leku:
                return lek
        return None

    def dodaj_uzytkownika(self, uzytkownik):
        if not isinstance(uzytkownik, Uzytkownik):
            raise ValueError("Dodawany użytkownik musi być instancją klasy Uzytkownik")
        self.uzytkownicy.append(uzytkownik)

    def usun_uzytkownika(self, imie):
        if not isinstance(imie, str):
            raise ValueError("Imię użytkownika musi być ciągiem znaków")
        poczatkowa_dlugosc = len(self.uzytkownicy)
        self.uzytkownicy = [uzytkownik for uzytkownik in self.uzytkownicy if uzytkownik.imie != imie]
        if len(self.uzytkownicy) == poczatkowa_dlugosc:
            print(f"Użytkownika o imieniu {imie} nie znaleziono. Nic nie usunięto.")

    def sprawdz_bezpieczenstwo(self, lek, uzytkownik):
        if not isinstance(lek, Lek):
            raise ValueError("Lek musi być instancją klasy Lek")
        if not isinstance(uzytkownik, Uzytkownik):
            raise ValueError("Użytkownik musi być instancją klasy Uzytkownik")

        if uzytkownik.wiek < lek.zalecany_wiek:
            return False, f"Lek niebezpieczny ze względu na wiek (zalecany wiek: {lek.zalecany_wiek}, wiek użytkownika: {uzytkownik.wiek})"
        for uczulenie in uzytkownik.uczulenia:
            if uczulenie in lek.substancje_czynne:
                return False, f"Lek niebezpieczny ze względu na uczulenie na substancje czynne ({uczulenie})"

        return True, "Lek bezpieczny dla użytkownika"

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

    def harmonogram_przyjmowania(self):
        for uzytkownik in self.uzytkownicy:
            print(f"\nHarmonogram przyjmowania leków dla {uzytkownik.imie}:")
            for lek_przyjmowany in uzytkownik.leki_przyjmowane:
                print(f"{lek_przyjmowany.lek.nazwa} - Dawka: {lek_przyjmowany.dawka} - Dzień: {lek_przyjmowany.dzien}")


def main_menu():
    apteczka = Apteczka()

    while True:
        print("\nMenu główne:")
        print("1. Dodaj lek")
        print("2. Usuń lek")
        print("3. Dodaj użytkownika")
        print("4. Usuń użytkownika")
        print("5. Sprawdź bezpieczeństwo leku")
        print("6. Wyświetl harmonogram przyjmowania leków")
        print("7. Wczytaj bazę danych z pliku")
        print("8. Zapisz bazę danych do pliku")
        print("9. Wyjście")

        wybor = input("Wybierz opcję (1-9): ")

        if wybor == "1":
            dodaj_lek(apteczka)
        elif wybor == "2":
            usun_lek(apteczka)
        elif wybor == "3":
            dodaj_uzytkownika(apteczka)
        elif wybor == "4":
            usun_uzytkownika(apteczka)
        elif wybor == "5":
            sprawdz_bezpieczenstwo(apteczka)
        elif wybor == "6":
            apteczka.harmonogram_przyjmowania()
        elif wybor == "7":
            plik = input("Podaj nazwę pliku do wczytania: ")
            apteczka.wczytaj_baze(plik)
        elif wybor == "8":
            plik = input("Podaj nazwę pliku do zapisania: ")
            apteczka.zapisz_baze(plik)
        elif wybor == "9":
            print("Do widzenia!")
            break
        else:
            print("Nieprawidłowy wybór. Spróbuj ponownie.")


def dodaj_lek(apteczka):
    nazwa = input("Podaj nazwę leku: ")
    producent = input("Podaj producenta: ")
    jednostki_chorobowe = input("Podaj jednostki chorobowe (oddzielone średnikiem): ").split(';')
    dla_kogo = input("Podaj osoby, dla których lek jest przeznaczony (oddzielone średnikiem): ").split(';')
    substancje_czynne = input("Podaj substancje czynne (oddzielone średnikiem): ").split(';')
    zalecany_wiek = int(input("Podaj zalecany wiek: "))
    liczba_dawek = int(input("Podaj liczbę dawek: "))
    liczba_dostepnych_dawek = int(input("Podaj liczbę dostępnych dawek: "))
    termin_waznosci = input("Podaj termin ważności (dd-mm-YYYY): ")
    notatka = input("Podaj notatkę: ")

    lek = Lek(nazwa, producent, jednostki_chorobowe, dla_kogo, substancje_czynne, zalecany_wiek, liczba_dawek,
              liczba_dostepnych_dawek, termin_waznosci, notatka)
    apteczka.dodaj_lek(lek)
    print("Lek został dodany.")


def usun_lek(apteczka):
    nazwa = input("Podaj nazwę leku do usunięcia: ")
    apteczka.usun_lek(nazwa)


def dodaj_uzytkownika(apteczka):
    imie = input("Podaj imię użytkownika: ")
    wiek = int(input("Podaj wiek użytkownika: "))
    jednostki_chorobowe = input("Podaj jednostki chorobowe (oddzielone średnikiem): ").split(';')
    uczulenia = input("Podaj uczulenia (oddzielone średnikiem): ").split(';')
    leki_przyjmowane = []

    dodaj_kolejny = input("Czy chcesz dodać leki przyjmowane? (tak/nie): ").lower()
    while dodaj_kolejny == "tak":
        nazwa_leku = input("Podaj nazwę leku: ")
        lek = apteczka.znajdz_lek(nazwa_leku)
        if lek:
            dawka = input("Podaj dawkę: ")
            dzien = input("Podaj dzień: ")
            lek_przyjmowany = LekPrzyjmowany(lek, dawka, dzien)
            leki_przyjmowane.append(lek_przyjmowany)
        else:
            print("Lek nie został znaleziony w apteczce.")

        dodaj_kolejny = input("Czy chcesz dodać kolejny lek przyjmowany? (tak/nie): ").lower()

    uzytkownik = Uzytkownik(imie, wiek, jednostki_chorobowe, uczulenia, leki_przyjmowane)
    apteczka.dodaj_uzytkownika(uzytkownik)
    print("Użytkownik został dodany.")


def usun_uzytkownika(apteczka):
    imie = input("Podaj imię użytkownika do usunięcia: ")
    apteczka.usun_uzytkownika(imie)


def sprawdz_bezpieczenstwo(apteczka):
    nazwa_leku = input("Podaj nazwę leku: ")
    imie_uzytkownika = input("Podaj imię użytkownika: ")

    lek = apteczka.znajdz_lek(nazwa_leku)
    uzytkownik = None
    for user in apteczka.uzytkownicy:
        if user.imie == imie_uzytkownika:
            uzytkownik = user
            break

    if lek and uzytkownik:
        bezpieczny, powod = apteczka.sprawdz_bezpieczenstwo(lek, uzytkownik)
        if bezpieczny:
            print("Lek jest bezpieczny dla użytkownika.")
        else:
            print(f"Lek nie jest bezpieczny: {powod}")
    else:
        print("Nie znaleziono leku lub użytkownika.")


if __name__ == "__main__":
    main_menu()

