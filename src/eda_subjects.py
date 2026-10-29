# biblioteka do wczytywania i analizowania danych
import pandas as pd


def main():

    # wczytanie zbioru danych z pliku csv
    dane = pd.read_csv("data/raw/adhdata.csv")

    # sprawdzenie liczby unikalnych uczestników badania
    print("LICZBA UCZESTNIKÓW:")
    print(dane["ID"].nunique())

    # sprawdzenie liczby rekordów przypisanych do każdej klasy
    print("\nLICZBA REKORDÓW W KAŻDEJ KLASIE:")
    print(dane["Class"].value_counts())

    # sprawdzenie liczby unikalnych uczestników w każdej klasie
    print("\nLICZBA UCZESTNIKÓW W KAŻDEJ KLASIE:")
    print(dane.groupby("Class")["ID"].nunique())

    # analiza liczby rekordów przypadających na jednego uczestnika
    rekordy_na_osobe = dane.groupby("ID").size()

    # statystyki opisowe dotyczące liczby rekordów na uczestnika
    print("\nLICZBA REKORDÓW NA UCZESTNIKA:")
    print(rekordy_na_osobe.describe())

    # sprawdzenie, czy uczestnicy mają przypisaną tylko jedną klasę
    klasy_na_osobe = dane.groupby("ID")["Class"].nunique()

    print("\nUCZESTNICY Z WIĘCEJ NIŻ JEDNĄ KLASĄ:")
    print((klasy_na_osobe > 1).sum())


# sprawdzamy, czy plik został uruchomiony bezpośrednio
if __name__ == "__main__":

    # jeśli tak, uruchamiamy główną funkcję programu
    main()