# skapiec

## TODO

- Aplikacja desktopowa
  - Tkinter/Avalonia
- Baza danych
  - Relational/Non relational?
- Server
  - Flask
- Scrapper
  - Python
- Testy

## Idea

Użytkownik wpisuje sobie frazę w program,
program wysyła zapytanie do servera, który ściąga dane ze strony pod daną frazą,
następnie wrzuca zdobyte dane do bazy danych,
program wyświetla produkty pod tą kategorią

## Przebieg

Aplikacja desktopowa > Server > Scrapper > Server > Baza danych > Aplikacja desktopowa

## Struktura JSON

- Nazwy
- URL sklepu wewnetrzne
- URL sklepu zewnetrzne
- Cena aktualne
- Cena najnizsza
- URL obrazu
- Opis
- Data aktualizacji

| TAB1    | TAB2     | TAB3     |
| ------- | -------- | -------- |
| rekord1 | rekord 2 | rekord 3 |

## Skład zespołu

- Igor Gawłowicz - Szef, Developer
- Patryk Pawełek - UX designer, Developer
- Piotr Rucki - Developer, Tester
- Paweł Mirecki - Developer, Tester

## Definicja wymagań funkcjonalnych

Program składa się z dwóch części,

- frontu w postaci SPA (single page application) zbudowanego na bibliotece React
- servera odpowiedzialnego za komunikacje pomiędzy frontem a bazą danych, a także za uzupełnianie bazy danych i jej korekty

Wcześniej wspomnianą bazą danych jest plik JSON jako nie-relacyjna baza danych, dane są pobierane przez program ściągający kod źródłowy strony uruchamiany przez server.

Program jest aplikacją webową pozwalającą użytkownikowi na wprowadzenie frazy która następnie zostanie przesłana na server po czym on ściągnie wyniki wyszukiwania ze strony `Skąpiec.pl`, zapisze je do bazy danych po czym przekaże do frontu, który następnie wyświetli odpowiednio otagowane dane w postaci tabeli.

## Wymagania niefunkcjonalne

## Wybór technologii realizacji

### Biblioteki

- React

### Frameworki

- Flask

### Hosting

- github (ghpages)
- pythonanywhere

### Bazy danych

- JSON

## Wybór narzędzi realizacji

### Repozytorium Kodu

- github - kontrola wersji

### Narzędzia do zarządzania projektem

- discord - z racji na małą skalę projektu, rozpisaliśmy wszystkie potrzebne do zrobienia fragmentu na czacie

### Narzędzia do komunikacji

- discord

## Projekt systemu
