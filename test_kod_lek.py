from kod import Lek


def test_lek_init():
    lek = Lek("Paracetamol", "XYZ Pharma", ["gorączka", "ból"], ["mama", "tata"], ["paracetamol"], 12, 10, 8, "31-12-2024", "na gorączkę")
    assert lek.nazwa == "Paracetamol"
    assert lek.producent == "XYZ Pharma"
    assert lek.jednostki_chorobowe == ["gorączka", "ból"]
    assert lek.dla_kogo == ["mama", "tata"]
    assert lek.substancje_czynne == ["paracetamol"]
    assert lek.zalecany_wiek == 12
    assert lek.liczba_dawek == 10
    assert lek.liczba_dostepnych_dawek == 8
    assert lek.termin_waznosci == "31-12-2024"
    assert lek.notatka == "na gorączkę"

def test_lek_jest_przeterminowany():
    lek = Lek("Paracetamol", "XYZ Pharma", ["gorączka", "ból"], ["mama", "tata"], ["paracetamol"], 12, 10, 8, "31-12-2025", "na gorączkę")
    assert not lek.jest_przeterminowany()
    lek_przeterminowany = Lek("Ibuprofen", "ABC Pharma", ["ból"], ["tata"], ["ibuprofen"], 12, 20, 20, "01-01-2020", "na ból")
    assert lek_przeterminowany.jest_przeterminowany()

def test_lek_edytuj():
    lek = Lek("Paracetamol", "XYZ Pharma", ["gorączka", "ból"], ["mama", "tata"], ["paracetamol"], 12, 10, 8, "31-12-2024", "na gorączkę")
    lek.edytuj(nazwa="Aspiryna", producent="DEF Pharma", liczba_dostepnych_dawek=5)
    assert lek.nazwa == "Aspiryna"
    assert lek.producent == "DEF Pharma"
    assert lek.liczba_dostepnych_dawek == 5

def test_lek_init_errors():
    try:
        Lek("", "XYZ Pharma", ["gorączka", "ból"], ["mama", "tata"], ["paracetamol"], 12, 10, 8, "31-12-2024", "na gorączkę")
    except ValueError as e:
        assert str(e) == "Wszystkie zmienne muszą być podane"

    try:
        Lek("Paracetamol", "", ["gorączka", "ból"], ["mama", "tata"], ["paracetamol"], 12, 10, 8, "31-12-2024", "na gorączkę")
    except ValueError as e:
        assert str(e) == "Wszystkie zmienne muszą być podane"

    try:
        Lek("Paracetamol", "XYZ Pharma", [], ["mama", "tata"], ["paracetamol"], 12, 10, 8, "31-12-2024", "na gorączkę")
    except ValueError as e:
        assert str(e) == "Wszystkie zmienne muszą być podane"

    try:
        Lek("Paracetamol", "XYZ Pharma", ["gorączka", "ból"], ["mama", "tata"], ["paracetamol"], 12, 10, 8, "31-12-2024", "")
    except ValueError as e:
        assert str(e) == "Wszystkie zmienne muszą być podane"

def test_lek_init_format_errors():
    try:
        Lek("Paracetamol", "XYZ Pharma", "gorączka, ból", ["mama", "tata"], ["paracetamol"], 12, 10, 8, "31-12-2024", "na gorączkę")
    except ValueError as e:
        assert str(e) == "Zmienne: jednostki_chorobowe, dla_kogo, substancje_czynne  muszą być listami"

    try:
        Lek("Paracetamol", ["XYZ Pharma"], ["gorączka", "ból"], ["mama", "tata"], ["paracetamol"], 12, 10, 8, "31-12-2024", "na gorączkę")
    except ValueError as e:
        assert str(e) == "Zmienne: nazwa, producent, notatka  muszą być ciągami znaków"

    try:
        Lek("Paracetamol", "XYZ Pharma", ["gorączka", "ból"], ["mama", "tata"], ["paracetamol"], "dwanaście", 10, 8, "31-12-2024", "na gorączkę")
    except ValueError as e:
        assert str(e) == "Zmienne: zalecany_wiek, liczba_dawek, liczba_dostepnych_dawek  muszą być liczbami"

    try:
        Lek("Paracetamol", "XYZ Pharma", ["gorączka", "ból"], ["mama", "tata"], ["paracetamol"], 12, 10, 8, "31/12/2024", "na gorączkę")
    except ValueError as e:
        assert str(e) == "Termin ważności musi być w formacie dd-mm-YYYY"

def test_lek_edytuj_format_errors():
    lek = Lek("Paracetamol", "XYZ Pharma", ["gorączka", "ból"], ["mama", "tata"], ["paracetamol"], 12, 10, 8, "31-12-2024", "na gorączkę")
    try:
        lek.edytuj(nazwa=123)
    except ValueError as e:
        assert str(e) == "Nazwa musi być ciągiem znaków"

    try:
        lek.edytuj(producent=123)
    except ValueError as e:
        assert str(e) == "Producent musi być ciągiem znaków"

    try:
        lek.edytuj(jednostki_chorobowe="gorączka, ból")
    except ValueError as e:
        assert str(e) == "Jednostki chorobowe muszą być listą"

    try:
        lek.edytuj(dla_kogo="mama, tata")
    except ValueError as e:
        assert str(e) == "Dla kogo musi być listą"

    try:
        lek.edytuj(substancje_czynne="paracetamol")
    except ValueError as e:
        assert str(e) == "Substancje czynne muszą być listą"

    try:
        lek.edytuj(zalecany_wiek="dwanaście")
    except ValueError as e:
        assert str(e) == "Zalecany wiek musi być liczbą całkowitą"

    try:
        lek.edytuj(termin_waznosci="31/12/2024")
    except ValueError as e:
        assert str(e) == "Termin ważności musi być w formacie dd-mm-YYYY"
