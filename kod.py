import csv
from datetime import datetime


class Lek:
    """
    Klasa reprezentująca lek.

    Atrybuty:
        nazwa (str): Nazwa leku.
        producent (str): Producent leku.
        jednostki_chorobowe (list): Lista jednostek chorobowych, na które lek jest przeznaczony.
        dla_kogo (list): Lista osób, dla których lek jest przeznaczony.
        substancje_czynne (list): Lista substancji czynnych w leku.
        zalecany_wiek (int): Zalecany wiek użytkownika leku.
        liczba_dawek (int): Liczba dawek leku.
        liczba_dostepnych_dawek (int): Liczba dostępnych dawek leku.
        termin_waznosci (str): Termin ważności leku w formacie dd-mm-YYYY.
        notatka (str): Dodatkowa notatka dotycząca leku.
    """

    def __init__(self, nazwa, producent, jednostki_chorobowe, dla_kogo, substancje_czynne, zalecany_wiek, liczba_dawek,
                 liczba_dostepnych_dawek, termin_waznosci, notatka):
        """
        Inicjalizuje obiekt klasy Lek.
        """
        if (not isinstance(nazwa, str) or
                not isinstance(producent, str) or
                not isinstance(notatka, str)):
            raise ValueError("Zmienne: nazwa, producent, notatka  muszą być ciągami znaków")
        if (not isinstance(jednostki_chorobowe, list) or
                not isinstance(dla_kogo, list) or
                not isinstance(substancje_czynne, list)):
            raise ValueError("Zmienne: jednostki_chorobowe, dla_kogo, substancje_czynne  muszą być listami")
        if (not isinstance(zalecany_wiek, int) or
                not isinstance(liczba_dawek, int) or
                not isinstance(liczba_dostepnych_dawek, int)):
            raise ValueError("Zmienne: zalecany_wiek, liczba_dawek, liczba_dostepnych_dawek  muszą być liczbami")
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
        """
        Sprawdza, czy lek jest przeterminowany.

        Returns:
            bool: True, jeśli lek jest przeterminowany, w przeciwnym razie False.
        """
        return datetime.strptime(self.termin_waznosci, '%d-%m-%Y') < datetime.now()

    def edytuj(self, nazwa=None, producent=None, jednostki_chorobowe=None, dla_kogo=None, substancje_czynne=None,
               zalecany_wiek=None, liczba_dawek=None, liczba_dostepnych_dawek=None, termin_waznosci=None, notatka=None):

        """
        Edytuje właściwości leku.

        Args:
            nazwa (str, opcjonalnie): Nowa nazwa leku.
            producent (str, opcjonalnie): Nowy producent leku.
            jednostki_chorobowe (list, opcjonalnie): Nowa lista jednostek chorobowych.
            dla_kogo (list, opcjonalnie): Nowa lista osób, dla których lek jest przeznaczony.
            substancje_czynne (list, opcjonalnie): Nowa lista substancji czynnych.
            zalecany_wiek (int, opcjonalnie): Nowy zalecany wiek użytkownika leku.
            liczba_dawek (int, opcjonalnie): Nowa liczba dawek leku.
            liczba_dostepnych_dawek (int, opcjonalnie): Nowa liczba dostępnych dawek leku.
            termin_waznosci (str, opcjonalnie): Nowy termin ważności leku w formacie dd-mm-YYYY.
            notatka (str, opcjonalnie): Nowa notatka dotycząca leku.
        """

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
        """
        Reprezentacja tekstowa obiektu klasy Lek.

        Returns:
            str: Tekstowa reprezentacja obiektu Lek.
        """
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
    """
    Klasa reprezentująca lek przyjmowany przez użytkownika.

    Atrybuty:
        lek (Lek): Obiekt leku przyjmowanego przez użytkownika.
        dawka (str): Dawka leku.
        dzien (str): Dzień tygodnia przyjmowania leku.
    """

    def __init__(self, lek, dawka, dzien):
        """
        Inicjalizuje obiekt klasy LekPrzyjmowany.

        Args:
            lek (Lek): Obiekt leku.
            dawka (str): Dawka leku.
            dzien (str): Dzień przyjmowania leku.
        """
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
        """
        Reprezentacja tekstowa obiektu klasy LekPrzyjmowany.

        Returns:
            str: Tekstowa reprezentacja obiektu LekPrzyjmowany.
        """
        return f"{self.lek.nazwa} - Dawka: {self.dawka} - Dzień: {self.dzien}"


class Uzytkownik:
    """
    Klasa reprezentująca użytkownika apteczki.

    Atrybuty:
        imie (str): Imię użytkownika.
        wiek (int): Wiek użytkownika.
        jednostki_chorobowe (list): Lista jednostek chorobowych użytkownika.
        uczulenia (list): Lista uczuleń użytkownika.
        leki_przyjmowane (list): Lista leków przyjmowanych przez użytkownika.
    """

    def __init__(self, imie, wiek, jednostki_chorobowe, uczulenia, leki_przyjmowane):
        """
        Inicjalizuje obiekt klasy Uzytkownik.
        """
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
        self.leki_przyjmowane = []
        """
        Sprawdza, czy leki przyjmowane są zgodne z klasą LekPrzyjmowany
        """
        for lek_przyjmowany in leki_przyjmowane:
            if isinstance(lek_przyjmowany, LekPrzyjmowany):
                self.leki_przyjmowane.append(lek_przyjmowany)
            else:
                raise ValueError("Każdy element leki_przyjmowane musi być instancją klasy LekPrzyjmowany")

    def dodaj_lek_przyjmowany(self, lek_przyjmowany):
        """
        Dodaje lek przyjmowany do listy leków przyjmowanych.

        Args:
            lek_przyjmowany (LekPrzyjmowany): Obiekt leku przyjmowanego.
        """
        if isinstance(lek_przyjmowany, LekPrzyjmowany):
            self.leki_przyjmowane.append(lek_przyjmowany)
        else:
            raise ValueError("Dodawany lek musi być instancją klasy LekPrzyjmowany")

    def edytuj(self, imie=None, wiek=None, jednostki_chorobowe=None, uczulenia=None, leki_przyjmowane=None):
        """
          Edytuje atrybuty użytkownika.

          Args:
              imie (str, opcjonalnie): Nowe imię użytkownika.
              wiek (int, opcjonalnie): Nowy wiek użytkownika.
              jednostki_chorobowe (list, opcjonalnie): Nowa lista jednostek chorobowych użytkownika.
              uczulenia (list, opcjonalnie): Nowa lista uczuleń użytkownika.
              leki_przyjmowane (list, opcjonalnie): Nowa lista leków przyjmowanych przez użytkownika.
          """
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
        """
        Reprezentacja tekstowa obiektu klasy Uzytkownik.

        Returns:
            str: Tekstowa reprezentacja obiektu Uzytkownik.
        """
        return (f"Użytkownik: {self.imie}\n"
                f"Wiek: {self.wiek}\n"
                f"Jednostki chorobowe: {', '.join(self.jednostki_chorobowe)}\n"
                f"Uczulenia: {', '.join(self.uczulenia)}\n"
                f"Leki przyjmowane: {', '.join([str(lek_przyjmowany) for lek_przyjmowany in self.leki_przyjmowane])}\n")


class Apteczka:
    """
    Klasa reprezentująca apteczkę, która przechowuje leki i użytkowników.

    Atrybuty:
        leki (list): Lista leków w apteczce.
        uzytkownicy (list): Lista użytkowników apteczki.
    """

    def __init__(self):
        """
        Inicjalizuje obiekt klasy: Apteczka.
        """
        self.leki = []
        self.uzytkownicy = []

    def dodaj_lek(self, lek):
        """
        Dodaje lek do apteczki.

        Args:
            lek (Lek): Obiekt leku do dodania.
        """
        if not isinstance(lek, Lek):
            raise ValueError("Dodawany lek musi być instancją klasy Lek")
        self.leki.append(lek)

    def usun_lek(self, nazwa_leku):
        """
        Usuwa lek o podanej nazwie z apteczki.

        Args:
            nazwa_leku (str): Nazwa leku do usunięcia.
        """
        if not isinstance(nazwa_leku, str):
            raise ValueError("Nazwa leku musi być ciągiem znaków")
        poczatkowa_dlugosc = len(self.leki)
        self.leki = [lek for lek in self.leki if lek.nazwa != nazwa_leku]
        if len(self.leki) == poczatkowa_dlugosc:
            print(f"Leku o nazwie {nazwa_leku} nie znaleziono. Nic nie usunięto.")

    def znajdz_lek(self, nazwa_leku):
        """
        Znajduje lek o podanej nazwie w apteczce.

        Args:
            nazwa_leku (str): Nazwa leku do znalezienia.

        Returns:
            Lek: Obiekt leku o podanej nazwie lub None, jeśli nie znaleziono.
        """
        if not isinstance(nazwa_leku, str):
            raise ValueError("Nazwa leku musi być ciągiem znaków")
        for lek in self.leki:
            if lek.nazwa == nazwa_leku:
                return lek
        return None

    def dodaj_uzytkownika(self, uzytkownik):
        """
        Dodaje użytkownika do apteczki.

        Args:
            uzytkownik (Uzytkownik): Obiekt użytkownika do dodania.
        """
        if not isinstance(uzytkownik, Uzytkownik):
            raise ValueError("Dodawany użytkownik musi być instancją klasy Uzytkownik")
        self.uzytkownicy.append(uzytkownik)

    def usun_uzytkownika(self, imie):
        """
        Usuwa użytkownika o podanym imieniu z apteczki.

        Args:
            imie (str): Imię użytkownika do usunięcia.
        """
        if not isinstance(imie, str):
            raise ValueError("Imię użytkownika musi być ciągiem znaków")
        poczatkowa_dlugosc = len(self.uzytkownicy)
        self.uzytkownicy = [uzytkownik for uzytkownik in self.uzytkownicy if uzytkownik.imie != imie]
        if len(self.uzytkownicy) == poczatkowa_dlugosc:
            print(f"Użytkownika o imieniu {imie} nie znaleziono. Nic nie usunięto.")

    def sprawdz_bezpieczenstwo(self, lek, uzytkownik):
        """
        Sprawdza bezpieczeństwo leku dla danego użytkownika.

        Args:
            lek (Lek): Obiekt leku do sprawdzenia.
            uzytkownik (Uzytkownik): Obiekt użytkownika do sprawdzenia.

        Returns:
            tuple: (bool, str) - True, jeśli lek jest bezpieczny, False w przeciwnym razie, oraz powód.
        """
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

    def wez_dawke(self, nazwa_leku):
        """
        Pobiera jedną dawkę leku o podanej nazwie.

        Args:
            nazwa_leku (str): Nazwa leku, z którego chcesz pobrać dawkę.
        """
        if not isinstance(nazwa_leku, str):
            raise ValueError("Nazwa leku musi być ciągiem znaków")
        lek = self.znajdz_lek(nazwa_leku)
        if lek:
            if lek.liczba_dostepnych_dawek > 0:
                lek.liczba_dostepnych_dawek -= 1
                print(
                    f"Pobrano jedną dawkę leku: {lek.nazwa}. Pozostało dostępnych dawek: {lek.liczba_dostepnych_dawek}")
            else:
                print(f"Brak dostępnych dawek leku: {lek.nazwa}")
        else:
            print(f"Lek o nazwie {nazwa_leku} nie został znaleziony w apteczce.")

    def wczytaj_baze(self, plik):
        """
        Wczytuje bazę danych z pliku CSV.

        Args:
            plik (str): Nazwa pliku CSV do wczytania.
        """
        with open(plik, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=';')
            for row in reader:
                lek = Lek(
                    row['nazwa'], row['producent'], row['jednostki chorobowe'].split(';'),
                    row['dla kogo'].split(';'), row['substancje czynne'].split(';'),
                    int(row['zalecany wiek']), int(row['liczba dawek']),
                    int(row['liczba dostępnych dawek']), row['termin waznosci'], row['notatka']
                )
                self.dodaj_lek(lek)

    def zapisz_baze(self, plik):
        """
        Zapisuje bazę danych do pliku CSV.

        Args:
            plik (str): Nazwa pliku CSV do zapisania.
        """
        with open(plik, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['nazwa', 'producent', 'jednostki chorobowe', 'dla kogo', 'substancje czynne', 'zalecany wiek',
                          'liczba dawek', 'liczba dostępnych dawek', 'termin waznosci', 'notatka']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=';')
            writer.writeheader()
            for lek in self.leki:
                writer.writerow({
                    'nazwa': lek.nazwa,
                    'producent': lek.producent,
                    'jednostki chorobowe': ';'.join(lek.jednostki_chorobowe),
                    'dla kogo': ';'.join(lek.dla_kogo),
                    'substancje czynne': ';'.join(lek.substancje_czynne),
                    'zalecany wiek': lek.zalecany_wiek,
                    'liczba dawek': lek.liczba_dawek,
                    'liczba dostępnych dawek': lek.liczba_dostepnych_dawek,
                    'termin waznosci': lek.termin_waznosci,
                    'notatka': lek.notatka
                })

    def wyswietl_zawartosc(self):
        """
        Wyświetla zawartość apteczki, w tym wszystkie leki i użytkowników.
        """
        if not self.leki and not self.uzytkownicy:
            print("Apteczka jest pusta.")
            return

        if self.leki:
            print("\nLeki w apteczce:")
            for lek in self.leki:
                print(lek)

        if self.uzytkownicy:
            print("\nUżytkownicy apteczki:")
            for uzytkownik in self.uzytkownicy:
                print(uzytkownik)

    def przypomnij_przeterminowane(self):
        """
        Przypomina o przeterminowanych lekach w apteczce.
        """
        przeterminowane = [lek for lek in self.leki if lek.jest_przeterminowany()]
        if przeterminowane:
            print("Przeterminowane leki:")
            for lek in przeterminowane:
                print(f"{lek.nazwa} (termin ważności: {lek.termin_waznosci})")
        else:
            print("Brak przeterminowanych leków.")

    def harmonogram_przyjmowania(self, imie_uzytkownika):
        """
        Wyświetla i zwraca harmonogram przyjmowania leków dla danego użytkownika.

        Args:
            imie_uzytkownika (str): Imię użytkownika, dla którego chcesz wyświetlić harmonogram.

        Returns:
            str: Harmonogram przyjmowania leków użytkownika.
        """
        imie_uzytkownika = imie_uzytkownika.strip()
        for uzytkownik in self.uzytkownicy:
            if uzytkownik.imie.lower() == imie_uzytkownika.lower():
                harmonogram = f"\nHarmonogram przyjmowania leków dla {uzytkownik.imie}:\n"
                for lek_przyjmowany in uzytkownik.leki_przyjmowane:
                    harmonogram += f"{lek_przyjmowany.lek.nazwa} - Dawka: {lek_przyjmowany.dawka} - Dzień: {lek_przyjmowany.dzien}\n"
                print(harmonogram)
                return harmonogram.strip()
        print(f"Użytkownik o imieniu {imie_uzytkownika} nie został znaleziony.")
        return ""

    def edytuj_lek(self, nazwa_leku, **kwargs):
        """
        Edytuje atrybuty leku o podanej nazwie.

        Args:
            nazwa_leku (str): Nazwa leku do edycji.
            kwargs: Nowe wartości atrybutów leku.
        """
        lek = self.znajdz_lek(nazwa_leku)
        if lek:
            lek.edytuj(**kwargs)
            print(f"Lek {nazwa_leku} został zaktualizowany.")
        else:
            print(f"Lek o nazwie {nazwa_leku} nie został znaleziony w apteczce.")

    def edytuj_uzytkownika(self, imie, **kwargs):
        """
        Edytuje atrybuty użytkownika o podanym imieniu.

        Args:
            imie (str): Imię użytkownika do edycji.
            kwargs: Nowe wartości atrybutów użytkownika.
        """
        for uzytkownik in self.uzytkownicy:
            if uzytkownik.imie == imie:
                if isinstance(uzytkownik, Uzytkownik):
                    uzytkownik.edytuj(**kwargs)
                print(f"Użytkownik {uzytkownik.imie} został zaktualizowany.")
                return
        print(f"Użytkownik o imieniu {imie} nie został znaleziony.")


def main_menu():
    apteczka = Apteczka()
    mama = Uzytkownik("Mama", 35, [], [], [])
    tata = Uzytkownik("Tata", 40, [], [], [])
    dziecko = Uzytkownik("Dziecko", 8, [], [], [])

    apteczka.dodaj_uzytkownika(mama)
    apteczka.dodaj_uzytkownika(tata)
    apteczka.dodaj_uzytkownika(dziecko)
    """
    Utworzenie oraz dodanie do apteczki wymaganych użytkowników o pustych danych.
    """
    while True:
        """
        Główne menu interfejsu użytkownika apteczki.
        Pozwala na zarządzanie lekami i użytkownikami oraz wykonuje inne operacje na apteczce.

        Początkowo przeszukuje apteczkę w poszukiwaniu przeterminoawnych leków.

        Wybór opcji z menu:
        1. Dodaj lek - pozwala dodać nowy lek do apteczki.
        2. Usuń lek - pozwala usunąć istniejący lek z apteczki.
        3. Dodaj użytkownika - pozwala dodać nowego użytkownika do apteczki.
        4. Usuń użytkownika - pozwala usunąć istniejącego użytkownika z apteczki.
        5. Sprawdź bezpieczeństwo leku - sprawdza, czy dany lek jest bezpieczny dla użytkownika.
        6. Weź dawkę leku - pobiera dawkę leku z apteczki.
        7. Wyświetl harmonogram przyjmowania leków - wyświetla harmonogram przyjmowania leków dla użytkownika.
        8. Wczytaj bazę danych z pliku - wczytuje bazę danych leków z pliku CSV.
        9. Zapisz bazę danych do pliku - zapisuje bazę danych leków do pliku CSV.
        10. Wyświetl zawartość apteczki - wyświetla wszystkie leki i użytkowników przechowywanych w apteczce.
        11. Edytuj lek - edytuje atrybuty leku w apteczce.
        12. Edytuj użytkownika - edytuje atrybuty użytkownika, w tym leki przyjmowane przez użytkownika.
        13. Wyjście - kończy działanie programu.

        Główne menu działa w pętli, dopóki użytkownik nie wybierze opcji wyjścia.
        """
        apteczka.przypomnij_przeterminowane()

        print("\nMenu główne:")
        print("1. Dodaj lek")
        print("2. Usuń lek")
        print("3. Dodaj użytkownika")
        print("4. Usuń użytkownika")
        print("5. Sprawdź bezpieczeństwo leku")
        print("6. Weź dawkę leku")
        print("7. Wyświetl harmonogram przyjmowania leków")
        print("8. Wczytaj bazę danych z pliku")
        print("9. Zapisz bazę danych do pliku")
        print("10. Wyświetl zawartość apteczki")
        print("11. Edytuj lek")
        print("12. Edytuj użytkownika")
        print("13. Wyjście")

        wybor = input("Wybierz opcję (1-13): ")

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
            wez_dawke(apteczka)
        elif wybor == "7":
            harmonogram_przyjmowania_uzytkownika(apteczka)
        elif wybor == "8":
            plik = input("Podaj nazwę pliku do wczytania: ")
            apteczka.wczytaj_baze(plik)
        elif wybor == "9":
            plik = input("Podaj nazwę pliku do zapisania: ")
            apteczka.zapisz_baze(plik)
        elif wybor == "10":
            apteczka.wyswietl_zawartosc()
        elif wybor == "11":
            edytuj_lek(apteczka)
        elif wybor == "12":
            edytuj_uzytkownika(apteczka)
        elif wybor == "13":
            print("Program konczy działanie")
            break
        else:
            print("Nieprawidłowy wybór. Spróbuj ponownie.")


def wez_dawke(apteczka):
    """
    Pobiera dawkę leku na podstawie nazwy leku wprowadzonej przez użytkownika.

    Args:
        apteczka (Apteczka): Obiekt apteczki zawierający leki.
    """
    nazwa_leku = input("Podaj nazwę leku, z którego chcesz pobrać dawkę: ")
    apteczka.wez_dawke(nazwa_leku)


def dodaj_lek(apteczka):
    """
    Dodaje nowy lek do apteczki na podstawie informacji wprowadzonych przez użytkownika.

    Args:
        apteczka (Apteczka): Obiekt apteczki, do której dodawany jest lek.
    """
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
    """
    Usuwa lek z apteczki na podstawie nazwy leku wprowadzonej przez użytkownika.

    Args:
        apteczka (Apteczka): Obiekt apteczki zawierający leki.
    """
    nazwa = input("Podaj nazwę leku do usunięcia: ")
    apteczka.usun_lek(nazwa)


def dodaj_uzytkownika(apteczka):
    """
    Dodaje nowego użytkownika do apteczki na podstawie informacji wprowadzonych przez użytkownika.

    Args:
        apteczka (Apteczka): Obiekt apteczki, do której dodawany jest użytkownik.
    """
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
    """
    Usuwa użytkownika z apteczki na podstawie imienia użytkownika wprowadzonego przez użytkownika.

    Args:
        apteczka (Apteczka): Obiekt apteczki zawierający użytkowników.
    """
    imie = input("Podaj imię użytkownika do usunięcia: ")
    apteczka.usun_uzytkownika(imie)


def harmonogram_przyjmowania_uzytkownika(apteczka):
    """
    Wyświetla harmonogram przyjmowania leków dla danego użytkownika na podstawie imienia wprowadzonego przez użytkownika.

    Args:
        apteczka (Apteczka): Obiekt apteczki zawierający użytkowników.
    """
    imie_uzytkownika = input("Podaj imię użytkownika, dla którego chcesz wyświetlić harmonogram przyjmowania leków: ")
    apteczka.harmonogram_przyjmowania(imie_uzytkownika)


def sprawdz_bezpieczenstwo(apteczka):
    """
    Sprawdza bezpieczeństwo leku dla danego użytkownika na podstawie nazw leku i użytkownika wprowadzonych przez użytkownika.

    Args:
        apteczka (Apteczka): Obiekt apteczki zawierający leki i użytkowników.
    """
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


def edytuj_lek(apteczka):
    """
        Edytuje atrybuty leku o podanej nazwie w apteczce.

        Args:
            apteczka (Apteczka): Obiekt apteczki, w której przechowywany jest lek.
        """
    nazwa_leku = input("Podaj nazwę leku do edycji: ")
    nowa_nazwa = input("Podaj nową nazwę leku (pozostaw puste, aby nie zmieniać): ")
    nowy_producent = input("Podaj nowego producenta (pozostaw puste, aby nie zmieniać): ")
    nowe_jednostki_chorobowe = input("Podaj nowe jednostki chorobowe (oddzielone średnikiem, pozostaw puste, aby nie zmieniać): ")
    nowy_dla_kogo = input("Podaj nowe osoby, dla których lek jest przeznaczony (oddzielone średnikiem, pozostaw puste, aby nie zmieniać): ")
    nowe_substancje_czynne = input("Podaj nowe substancje czynne (oddzielone średnikiem, pozostaw puste, aby nie zmieniać): ")
    nowy_zalecany_wiek = input("Podaj nowy zalecany wiek (pozostaw puste, aby nie zmieniać): ")
    nowa_liczba_dawek = input("Podaj nową liczbę dawek (pozostaw puste, aby nie zmieniać): ")
    nowa_liczba_dostepnych_dawek = input("Podaj nową liczbę dostępnych dawek (pozostaw puste, aby nie zmieniać): ")
    nowy_termin_waznosci = input("Podaj nowy termin ważności (dd-mm-YYYY, pozostaw puste, aby nie zmieniać): ")
    nowa_notatka = input("Podaj nową notatkę (pozostaw puste, aby nie zmieniać): ")

    apteczka.edytuj_lek(nazwa_leku,
                        nazwa=nowa_nazwa or None,
                        producent=nowy_producent or None,
                        jednostki_chorobowe=nowe_jednostki_chorobowe.split(';') if nowe_jednostki_chorobowe else None,
                        dla_kogo=nowy_dla_kogo.split(';') if nowy_dla_kogo else None,
                        substancje_czynne=nowe_substancje_czynne.split(';') if nowe_substancje_czynne else None,
                        zalecany_wiek=int(nowy_zalecany_wiek) if nowy_zalecany_wiek else None,
                        liczba_dawek=int(nowa_liczba_dawek) if nowa_liczba_dawek else None,
                        liczba_dostepnych_dawek=int(nowa_liczba_dostepnych_dawek) if nowa_liczba_dostepnych_dawek else None,
                        termin_waznosci=nowy_termin_waznosci or None,
                        notatka=nowa_notatka or None)


def edytuj_uzytkownika(apteczka):
    """
    Edytuje atrybuty użytkownika o podanym imieniu w apteczce, w tym możliwość dodawania i usuwania leków przyjmowanych.

    Args:
        apteczka (Apteczka): Obiekt apteczki, w której przechowywany jest użytkownik.
    """
    imie_uzytkownika = input("Podaj imię użytkownika do edycji: ")
    nowy_wiek = input("Podaj nowy wiek (pozostaw puste, aby nie zmieniać): ")
    nowe_jednostki_chorobowe = input(
        "Podaj nowe jednostki chorobowe (oddzielone średnikiem, pozostaw puste, aby nie zmieniać): ")
    nowe_uczulenia = input("Podaj nowe uczulenia (oddzielone średnikiem, pozostaw puste, aby nie zmieniać): ")

    leki_przyjmowane = []

    if input("Czy chcesz edytować leki przyjmowane? (tak/nie): ").lower() == 'tak':
        while True:
            akcja = input(
                "Podaj 'dodaj', aby dodać nowy lek przyjmowany, lub 'usuń', aby usunąć lek przyjmowany: ").lower()
            if akcja == 'dodaj':
                nazwa_leku = input("Podaj nazwę leku: ")
                lek = apteczka.znajdz_lek(nazwa_leku)
                if lek:
                    dawka = input("Podaj dawkę: ")
                    dzien = input("Podaj dzień: ")
                    lek_przyjmowany = LekPrzyjmowany(lek, dawka, dzien)
                    leki_przyjmowane.append(lek_przyjmowany)
                else:
                    print("Lek nie został znaleziony w apteczce.")
            elif akcja == 'usuń':
                nazwa_leku = input("Podaj nazwę leku do usunięcia: ")
                uzytkownik = None
                for user in apteczka.uzytkownicy:
                    if user.imie == imie_uzytkownika:
                        uzytkownik = user
                        break
                if uzytkownik:
                    uzytkownik.leki_przyjmowane = [lek for lek in uzytkownik.leki_przyjmowane if
                                                   lek.lek.nazwa != nazwa_leku]
                    print(
                        f"Lek {nazwa_leku} został usunięty z leków przyjmowanych przez użytkownika {imie_uzytkownika}.")
                else:
                    print(f"Użytkownik {imie_uzytkownika} nie został znaleziony.")
            else:
                print("Nieprawidłowa akcja. Spróbuj ponownie.")

            if input("Czy chcesz kontynuować edycję leków przyjmowanych? (tak/nie): ").lower() != 'tak':
                break

    kwargs = {}
    if nowy_wiek:
        kwargs['wiek'] = int(nowy_wiek)
    if nowe_jednostki_chorobowe:
        kwargs['jednostki_chorobowe'] = nowe_jednostki_chorobowe.split(';')
    if nowe_uczulenia:
        kwargs['uczulenia'] = nowe_uczulenia.split(';')
    if leki_przyjmowane:
        kwargs['leki_przyjmowane'] = leki_przyjmowane

    apteczka.edytuj_uzytkownika(imie_uzytkownika, **kwargs)


if __name__ == "__main__":
    """
    Wywołuje działanie interface
    """
    main_menu()


