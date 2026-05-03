# 📌 QA Portfolio – Adrian

## 👋 O mnie

Jestem początkującym specjalistą QA z zapleczem programistycznym (Python, Django, JavaScript).

Skupiam się na testowaniu aplikacji webowych – zarówno manualnym, jak i automatycznym (UI testing z Selenium). Analizuję logikę biznesową aplikacji, identyfikuję błędy oraz projektuję przypadki testowe (test cases i test scenarios).

Dzięki doświadczeniu w tworzeniu aplikacji webowych lepiej rozumiem ich architekturę, co pozwala mi skuteczniej wykrywać potencjalne problemy.

---

# 🧪 Zakres QA w portfolio

W tym repozytorium znajdują się:

- dokumentacja testowa (test plans)
- przypadki testowe (test cases)
- raporty błędów (bug reports)
- testy automatyczne UI (Selenium WebDriver)
- testy backendowe (Django Test Client)

Każdy projekt opiera się na rzeczywistych aplikacjach webowych stworzonych przeze mnie w celach edukacyjnych.

---

# 📂 Testowane projekty

## 1. World Geography Quiz (Django)

- logika quizu oparta o sesje
- system punktacji i ranking użytkowników
- dynamiczne pytania i poziomy trudności

---

## 2. Auction Web Application (Django)

- system aukcji i licytacji (bids)
- watchlist (obserwowane aukcje)
- komentarze użytkowników i kategorie
- pełna logika tworzenia i przeglądania aukcji

---

## 3. Wiki Encyclopedia (Django)

- tworzenie i edycja stron (Markdown)
- wyszukiwanie treści
- losowa strona i obsługa błędów

---

## 4. Mail Client (SPA / REST API)

- skrzynki mailowe (Inbox / Sent / Archive)
- dynamiczne ładowanie danych (SPA)
- komunikacja z API
- wysyłanie i odpowiadanie na wiadomości

---

## 5. Google Search Front-End

- wyszukiwanie standardowe i zaawansowane
- obsługa formularzy GET
- testowanie UI i walidacji formularzy

---

# 🤖 Testy automatyczne (Selenium WebDriver + Django Test Client)

W ramach nauki automatyzacji QA tworzę testy UI oraz backendowe z użyciem:

- Selenium WebDriver (Python)
- Django Test Client

---

## ✔ Przykładowe testy

### 🔐 Login Test (UI – Selenium)
- otwarcie strony logowania
- wpisanie niepoprawnych danych
- walidacja komunikatu błędu

---

### 🔎 Google Search Test (UI – Selenium)
- otwarcie Google
- wykonanie zapytania
- weryfikacja wyników

---

### 📝 Register Test (Django)
- tworzenie użytkownika
- walidacja formularza
- sprawdzenie poprawnej rejestracji

---

### 🧪 Quiz Application Test (Backend – Django Test Client)
- inicjalizacja sesji użytkownika
- ustawienie wyniku początkowego (score = 0)
- uruchomienie quizu
- walidacja logiki gry

---

### 🏷️ Auction E2E Automation Test (Selenium WebDriver)

Automatyczny test end-to-end dla aplikacji aukcyjnej (Django).

#### 📌 Zakres:
- logowanie użytkownika
- tworzenie nowej aukcji (listing)
- wybór kategorii (Cars / Trucks / Phones)
- dodanie zdjęcia (image URL)
- składanie oferty (bid)
- weryfikacja zmiany ceny po licytacji

#### 📁 Lokalizacja:
automation-tests/test_login_and_bid.py

#### 🎯 Cel:
Test symuluje pełny przepływ użytkownika w systemie aukcyjnym i weryfikuje logikę biznesową licytacji.

---

# 🛠️ Technologie

- Python
- Selenium WebDriver
- ChromeDriver
- Django
- HTML / CSS / JavaScript
- REST API
- SQLite

---

# 🎯 Cel portfolio

Celem tego repozytorium jest pokazanie umiejętności:

- analizy aplikacji webowych
- myślenia testerskiego (QA mindset)
- projektowania testów manualnych i automatycznych
- automatyzacji testów UI (Selenium)
- zrozumienia działania systemów webowych
- pracy na realnych scenariuszach E2E

---

# 📌 Podsumowanie

To portfolio pokazuje:

- testy manualne
- testy automatyczne UI
- testy backendowe
- realne scenariusze E2E
- pełne zrozumienie działania aplikacji webowych

