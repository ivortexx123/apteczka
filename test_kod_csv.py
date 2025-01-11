import os
import csv
from kod import Apteczka, Lek


def test_zapisz_baze(tmpdir):
    """
    Testuje funkcję zapisz_baze, zapisując dane do pliku CSV.
    """
    apteczka = Apteczka()
    lek = Lek("Paracetamol", "XYZ Pharma", ["gorączka"], ["mama"], ["paracetamol"], 12, 20, 20, "31-12-2025", "na gorączkę")
    apteczka.dodaj_lek(lek)

    tmpfile = os.path.join(tmpdir, "apteczka.csv")
    apteczka.zapisz_baze(tmpfile)

    assert os.path.isfile(tmpfile)

    with open(tmpfile, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        rows = list(reader)
        assert len(rows) == 1
        row = rows[0]
        assert row['nazwa'] == "Paracetamol"
        assert row['producent'] == "XYZ Pharma"
        assert row['jednostki chorobowe'] == "gorączka"
        assert row['dla kogo'] == "mama"
        assert row['substancje czynne'] == "paracetamol"
        assert row['zalecany wiek'] == "12"
        assert row['liczba dawek'] == "20"
        assert row['liczba dostępnych dawek'] == "20"
        assert row['termin waznosci'] == "31-12-2025"
        assert row['notatka'] == "na gorączkę"

def test_wczytaj_baze(tmpdir):
    """
    Testuje funkcję wczytaj_baze, wczytując dane z pliku CSV.
    """
    tmpfile = os.path.join(tmpdir, "apteczka.csv")
    with open(tmpfile, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['nazwa', 'producent', 'jednostki chorobowe', 'dla kogo', 'substancje czynne', 'zalecany wiek',
                      'liczba dawek', 'liczba dostępnych dawek', 'termin waznosci', 'notatka']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=';')
        writer.writeheader()
        writer.writerow({
            'nazwa': "Paracetamol",
            'producent': "XYZ Pharma",
            'jednostki chorobowe': "gorączka",
            'dla kogo': "dorosły",
            'substancje czynne': "paracetamol",
            'zalecany wiek': "12",
            'liczba dawek': "20",
            'liczba dostępnych dawek': "20",
            'termin waznosci': "31-12-2025",
            'notatka': "na gorączkę"
        })

    apteczka = Apteczka()
    apteczka.wczytaj_baze(tmpfile)

    assert len(apteczka.leki) == 1
    lek = apteczka.leki[0]
    assert lek.nazwa == "Paracetamol"
    assert lek.producent == "XYZ Pharma"
    assert lek.jednostki_chorobowe == ["gorączka"]
    assert lek.dla_kogo == ["dorosły"]
    assert lek.substancje_czynne == ["paracetamol"]
    assert lek.zalecany_wiek == 12
    assert lek.liczba_dawek == 20
    assert lek.liczba_dostepnych_dawek == 20
    assert lek.termin_waznosci == "31-12-2025"
    assert lek.notatka == "na gorączkę"
