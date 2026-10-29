# biblioteka pracy ze ściezkami do plikow
from pathlib import Path

# biblioteka do wczytywania i analizowania danych
import pandas as pd


def main():

    # folder z danymi
    folder_danych = Path("data/raw")

    #  wszystkie pliki csv w folderze i sort alfabetyczny
    pliki_csv = sorted(folder_danych.glob("*.csv"))

    # jesli nie znaleziono jakichkolwiek plikow csv
    if not pliki_csv:

        print("Nie znaleziono plików CSV w folderze data/raw.")

        print("Sprawdź, czy przesłałaś dane do właściwego folderu.")

        # koniec dzialania funkcji
        return

    # ilosc el w folderze, dlugosc listy
    print(f"Liczba znalezionych plików CSV: {len(pliki_csv)}")

    # przechodzimy przez każdy plik
    for plik in pliki_csv:

        # separator, żeby oddzielić informacje o plikach
        print("\n" + "=" * 60)

        # nazwa aktualnego pliku
        print(f"Plik: {plik.name}")

        # próbujemy wczytać dane z pliku csv
        try:
            dane = pd.read_csv(plik)

        # jeśli pojawi się błąd podczas wczytywania
        except Exception as blad:

            print(f"Nie udało się wczytać pliku: {blad}")

            # pomijamy ten plik i przechodzimy do następnego
            continue

        # liczba wierszy i kolumn w tabeli
        print(f"Liczba wierszy: {dane.shape[0]}")
        print(f"Liczba kolumn: {dane.shape[1]}")

        # nazwy wszystkich kolumn
        print("\nNazwy kolumn:")
        print(dane.columns.tolist())

        # pierwsze 5 wierszy danych
        print("\nPierwsze 5 wierszy:")
        print(dane.head().to_string())

        # typ danych przechowywanych w każdej kolumnie
        print("\nTypy danych:")
        print(dane.dtypes.to_string())

        # sprawdzamy, ile pustych wartości znajduje się w każdej kolumnie
        print("\nLiczba brakujących wartości w kolumnach:")
        print(dane.isna().sum().to_string())


# sprawdzamy, czy plik został uruchomiony bezpośrednio
if __name__ == "__main__":

    # jeśli tak, uruchamiamy główną funkcję programu
    main()