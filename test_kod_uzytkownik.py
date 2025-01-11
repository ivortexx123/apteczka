from kod import Uzytkownik, Lek, LekPrzyjmowany


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

def test_dodaj_lek_przyjmowany():
    lek1 = Lek("Paracetamol", "XYZ", ["gorączka", "ból"], ["mama"], ["paracetamol"], 12, 10, 8, "31-12-2024", "na gorączkę")
    lek_przyjmowany1 = LekPrzyjmowany(lek1, "1 tabletka", "poniedziałek")

    jednostki_chorobowe = ["nadciśnienie"]
    uczulenia = ["paracetamol"]
    leki_przyjmowane = []

    uzytkownik = Uzytkownik("mama", 35, jednostki_chorobowe, uczulenia, leki_przyjmowane)
    uzytkownik.dodaj_lek_przyjmowany(lek_przyjmowany1)

    assert len(uzytkownik.leki_przyjmowane) == 1
    assert uzytkownik.leki_przyjmowane[0] == lek_przyjmowany1

def test_edytuj_uzytkownika():
    jednostki_chorobowe = ["nadciśnienie"]
    uczulenia = ["paracetamol"]
    leki_przyjmowane = []

    uzytkownik = Uzytkownik("mama", 35, jednostki_chorobowe, uczulenia, leki_przyjmowane)
    uzytkownik.edytuj(imie="tata", wiek=40)

    assert uzytkownik.imie == "tata"
    assert uzytkownik.wiek == 40

def test_bledne_utworzenie_uzytkownika():
    jednostki_chorobowe = "nadciśnienie"  # Powinno być listą
    uczulenia = ["paracetamol"]
    leki_przyjmowane = []

    try:
        uzytkownik = Uzytkownik("mama", 35, jednostki_chorobowe, uczulenia, leki_przyjmowane)
    except ValueError as e:
        assert str(e) == "Jednostki chorobowe muszą być listą"

def test_bledne_dodanie_lek_przyjmowany():
    lek1 = Lek("Paracetamol", "XYZ Pharma", ["gorączka", "ból"], ["mama"], ["paracetamol"], 12, 10, 8, "31-12-2024", "na gorączkę")

    jednostki_chorobowe = ["nadciśnienie"]
    uczulenia = ["paracetamol"]
    leki_przyjmowane = []

    uzytkownik = Uzytkownik("mama", 35, jednostki_chorobowe, uczulenia, leki_przyjmowane)

    try:
        uzytkownik.dodaj_lek_przyjmowany(lek1)  # Powinno być instancją LekPrzyjmowany
    except ValueError as e:
        assert str(e) == "Dodawany lek musi być instancją klasy LekPrzyjmowany"

def test_bledne_edytowanie_uzytkownika():
    jednostki_chorobowe = ["nadciśnienie"]
    uczulenia = ["paracetamol"]
    leki_przyjmowane = []

    uzytkownik = Uzytkownik("mama", 35, jednostki_chorobowe, uczulenia, leki_przyjmowane)

    try:
        uzytkownik.edytuj(jednostki_chorobowe="nadciśnienie")  #Powinno być listą
    except ValueError as e:
        assert str(e) == "Jednostki chorobowe muszą być listą"
