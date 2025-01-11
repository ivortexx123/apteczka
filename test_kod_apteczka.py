from kod import Apteczka, LekPrzyjmowany, Lek, Uzytkownik
import pytest
def test_utworzenie_uzytkownika():
    jednostki_chorobowe = ["nadciśnienie"]
    uczulenia = ["paracetamol"]
    leki_przyjmowane = []

    uzytkownik = Uzytkownik("mama", 35, jednostki_chorobowe, uczulenia, leki_przyjmowane)

    assert uzytkownik.imie == "mama"
    assert uzytkownik.wiek == 35
    assert uzytkownik.jednostki_chorobowe == jednostki_chorobowe
    assert uzytkownik.uczulenia == uczulenia
    assert uzytkownik.leki_przyjmowane == leki_przyjmowane


def test_dodaj_lek():
    apteczka = Apteczka()
    lek = Lek("Paracetamol", "XYZ Pharma", ["gorączka"], ["dorosły"], ["paracetamol"], 12, 20, 20, "31-12-2025",
              "na gorączkę")

    apteczka.dodaj_lek(lek)

    assert len(apteczka.leki) == 1
    assert apteczka.leki[0] == lek


def test_usun_lek():
    apteczka = Apteczka()
    lek = Lek("Paracetamol", "XYZ Pharma", ["gorączka"], ["dorosły"], ["paracetamol"], 12, 20, 20, "31-12-2025",
              "na gorączkę")

    apteczka.dodaj_lek(lek)
    apteczka.usun_lek("Paracetamol")

    assert len(apteczka.leki) == 0


def test_znajdz_lek():
    apteczka = Apteczka()
    lek = Lek("Paracetamol", "XYZ Pharma", ["gorączka"], ["dorosły"], ["paracetamol"], 12, 20, 20, "31-12-2025",
              "na gorączkę")

    apteczka.dodaj_lek(lek)
    znaleziony_lek = apteczka.znajdz_lek("Paracetamol")

    assert znaleziony_lek == lek


def test_sprawdz_bezpieczenstwo():
    apteczka = Apteczka()
    lek = Lek("Paracetamol", "XYZ Pharma", ["gorączka"], ["dorosły"], ["paracetamol"], 12, 20, 20, "31-12-2025",
              "na gorączkę")
    uzytkownik = Uzytkownik("Jan", 30, [], ["paracetamol"], [])

    apteczka.dodaj_lek(lek)
    apteczka.dodaj_uzytkownika(uzytkownik)
    bezpieczny, powod = apteczka.sprawdz_bezpieczenstwo(lek, uzytkownik)

    assert not bezpieczny
    assert powod == "Lek niebezpieczny ze względu na uczulenie na substancje czynne (paracetamol)"


def test_wez_dawke():
    apteczka = Apteczka()
    lek = Lek("Paracetamol", "XYZ Pharma", ["gorączka"], ["dorosły"], ["paracetamol"], 12, 20, 20, "31-12-2025",
              "na gorączkę")

    apteczka.dodaj_lek(lek)
    apteczka.wez_dawke("Paracetamol")

    assert lek.liczba_dostepnych_dawek == 19


def test_harmonogram_przyjmowania():
    apteczka = Apteczka()
    lek = Lek("Paracetamol", "XYZ Pharma", ["gorączka"], ["dorosły"], ["paracetamol"], 12, 20, 20, "31-12-2025",
              "na gorączkę")
    lek_przyjmowany = LekPrzyjmowany(lek, "1 tabletka", "poniedziałek")
    uzytkownik = Uzytkownik("Jan", 30, [], [], [lek_przyjmowany])

    apteczka.dodaj_uzytkownika(uzytkownik)
    harmonogram = apteczka.harmonogram_przyjmowania("Jan")

    expected_output = "Harmonogram przyjmowania leków dla Jan:\nParacetamol - Dawka: 1 tabletka - Dzień: poniedziałek"
    assert harmonogram == expected_output

def test_dodaj_lek_niepoprawny_typ():
    apteczka = Apteczka()
    with pytest.raises(ValueError):
        apteczka.dodaj_lek("Paracetamol")  # Przekazanie niepoprawnego typu danych


def test_usun_lek_niepoprawny_typ():
    apteczka = Apteczka()
    with pytest.raises(ValueError):
        apteczka.usun_lek(12345)  # Przekazanie niepoprawnego typu danych


def test_znajdz_lek_niepoprawny_typ():
    apteczka = Apteczka()
    with pytest.raises(ValueError):
        apteczka.znajdz_lek(12345)  # Przekazanie niepoprawnego typu danych


def test_dodaj_uzytkownika_niepoprawny_typ():
    apteczka = Apteczka()
    with pytest.raises(ValueError):
        apteczka.dodaj_uzytkownika("Jan")  # Przekazanie niepoprawnego typu danych


def test_usun_uzytkownika_niepoprawny_typ():
    apteczka = Apteczka()
    with pytest.raises(ValueError):
        apteczka.usun_uzytkownika(12345)  # Przekazanie niepoprawnego typu danych


def test_sprawdz_bezpieczenstwo_niepoprawny_typ_lek():
    apteczka = Apteczka()
    uzytkownik = Uzytkownik("Jan", 30, [], [], [])
    apteczka.dodaj_uzytkownika(uzytkownik)
    with pytest.raises(ValueError):
        apteczka.sprawdz_bezpieczenstwo("Paracetamol", uzytkownik)  # Przekazanie niepoprawnego typu danych


def test_sprawdz_bezpieczenstwo_niepoprawny_typ_uzytkownik():
    apteczka = Apteczka()
    lek = Lek("Paracetamol", "XYZ Pharma", ["gorączka"], ["dorosły"], ["paracetamol"], 12, 20, 20, "31-12-2025",
              "na gorączkę")
    apteczka.dodaj_lek(lek)
    with pytest.raises(ValueError):
        apteczka.sprawdz_bezpieczenstwo(lek, "Jan")  # Przekazanie niepoprawnego typu danych


def test_edytuj_uzytkownika():
    apteczka = Apteczka()
    uzytkownik = Uzytkownik("Janusz", 30, ["nadciśnienie"], ["penicylina"], [])
    apteczka.dodaj_uzytkownika(uzytkownik)

    # Test edycji wieku
    apteczka.edytuj_uzytkownika("Janusz", wiek=35)
    assert uzytkownik.wiek == 35

    # Test edycji jednostek chorobowych
    nowe_jednostki_chorobowe = ["cukrzyca"]
    apteczka.edytuj_uzytkownika("Janusz", jednostki_chorobowe=nowe_jednostki_chorobowe)
    assert uzytkownik.jednostki_chorobowe == nowe_jednostki_chorobowe

    # Test edycji uczuleń
    nowe_uczulenia = ["kurz"]
    apteczka.edytuj_uzytkownika("Janusz", uczulenia=nowe_uczulenia)
    assert uzytkownik.uczulenia == nowe_uczulenia

    # Test edycji leków przyjmowanych
    lek = Lek("Aspiryna", "XYZ Pharma", ["ból"], ["dorosły"], ["kwas acetylosalicylowy"], 12, 20, 20, "31-12-2025", "na ból głowy")
    lek_przyjmowany = LekPrzyjmowany(lek, "1 tabletka", "poniedziałek")
    apteczka.dodaj_lek(lek)
    apteczka.edytuj_uzytkownika("Janusz", leki_przyjmowane=[lek_przyjmowany])
    assert uzytkownik.leki_przyjmowane == [lek_przyjmowany]

def test_edytuj_lek():
    apteczka = Apteczka()
    lek = Lek("Aspiryna", "XYZ Pharma", ["ból"], ["dorosły"], ["kwas acetylosalicylowy"], 12, 20, 20, "31-12-2025", "na ból głowy")
    apteczka.dodaj_lek(lek)

    # Test edycji nazwy leku
    apteczka.edytuj_lek("Aspiryna", nazwa="Ibuprofen")
    assert lek.nazwa == "Ibuprofen"

    # Test edycji producenta
    apteczka.edytuj_lek("Ibuprofen", producent="ABC Pharma")
    assert lek.producent == "ABC Pharma"

    # Test edycji jednostek chorobowych
    nowe_jednostki_chorobowe = ["gorączka"]
    apteczka.edytuj_lek("Ibuprofen", jednostki_chorobowe=nowe_jednostki_chorobowe)
    assert lek.jednostki_chorobowe == nowe_jednostki_chorobowe

    # Test edycji przeznaczenia leku
    nowy_dla_kogo = ["dziecko"]
    apteczka.edytuj_lek("Ibuprofen", dla_kogo=nowy_dla_kogo)
    assert lek.dla_kogo == nowy_dla_kogo

    # Test edycji substancji czynnych
    nowe_substancje_czynne = ["ibuprofen"]
    apteczka.edytuj_lek("Ibuprofen", substancje_czynne=nowe_substancje_czynne)
    assert lek.substancje_czynne == nowe_substancje_czynne

    # Test edycji zalecanego wieku
    apteczka.edytuj_lek("Ibuprofen", zalecany_wiek=6)
    assert lek.zalecany_wiek == 6

    # Test edycji liczby dawek
    apteczka.edytuj_lek("Ibuprofen", liczba_dawek=15)
    assert lek.liczba_dawek == 15

    # Test edycji liczby dostępnych dawek
    apteczka.edytuj_lek("Ibuprofen", liczba_dostepnych_dawek=15)
    assert lek.liczba_dostepnych_dawek == 15

    # Test edycji terminu ważności
    apteczka.edytuj_lek("Ibuprofen", termin_waznosci="31-12-2026")
    assert lek.termin_waznosci == "31-12-2026"

    # Test edycji notatki
    apteczka.edytuj_lek("Ibuprofen", notatka="na gorączkę")
    assert lek.notatka == "na gorączkę"
