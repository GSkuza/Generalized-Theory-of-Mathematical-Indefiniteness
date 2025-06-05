import os
from indefiniteness_core import O, AlienatedNumber, SingularityError

# Domyślne zachowanie (pochłaniające)
wynik1 = O + 10
print(f"O + 10 = {wynik1}")  # Wynik: O_empty_singularity

liczba_w = AlienatedNumber("przyklad")
wynik2 = liczba_w * 5
print(f"AlienatedNumber * 5 = {wynik2}")  # Wynik: O_empty_singularity

print(f"Czy O jest fałszywe? {not O}")  # Wynik: True
print(f"O is O: {O is O}")             # Wynik: True
print(f"O jako JSON: {O.to_json()}") # Wynik: "\"O_empty_singularity\""
print(f"liczba_w jako JSON: {liczba_w.to_json()}") # Wynik: "\"l_empty_num(przyklad)\""

# Przykład Trybu Ścisłego (wymaga zmiennej środowiskowej GTM_STRICT=1)
if os.getenv("GTM_STRICT", "0") == "1":
    print("\nTryb Ścisły jest WŁĄCZONY")
    try:
        wynik_strict = O / 2
        print(f"O / 2 w trybie ścisłym = {wynik_strict}") # Ta linia nie zostanie osiągnięta
    except SingularityError as e:
        print(f"Tryb ścisły przechwycił błąd dla 'O / 2': {e}")

    try:
        wynik_an_strict = liczba_w - 7
        print(f"AlienatedNumber - 7 w trybie ścisłym = {wynik_an_strict}") # Ta linia nie zostanie osiągnięta
    except SingularityError as e:
        print(f"Tryb ścisły przechwycił błąd dla 'AlienatedNumber - 7': {e}")
else:
    print("\nTryb Ścisły jest WYŁĄCZONY (ustaw GTM_STRICT=1, aby włączyć)")
