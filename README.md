# QA Portfolio – Adrian

## 👋 O mnie
Jestem początkującym specjalistą QA z zapleczem programistycznym (Python, Django, JavaScript).

Skupiam się na testowaniu aplikacji webowych – zarówno manualnym, jak i automatycznym (UI testing z Selenium). Analizuję logikę biznesową aplikacji, identyfikuję błędy oraz projektuję przypadki testowe (test cases i test scenarios).

Dzięki doświadczeniu w tworzeniu aplikacji webowych lepiej rozumiem ich architekturę, co pozwala mi skuteczniej wykrywać potencjalne problemy.

---

## 🧪 Zakres QA w portfolio

W tym repozytorium znajdują się:

- dokumentacja testowa (test plans)
- przypadki testowe (test cases)
- raporty błędów (bug reports)
- testy automatyczne UI (Selenium WebDriver)

Każdy projekt opiera się na rzeczywistych aplikacjach webowych stworzonych przeze mnie w celach edukacyjnych.

---

## 📂 Testowane projekty

### 1. World Geography Quiz (Django)
- logika quizu oparta o sesje
- system punktacji i ranking użytkowników
- dynamiczne pytania i poziomy trudności

### 2. Auction Web Application (Django)
- system aukcji i licytacji (bids)
- watchlist (obserwowane aukcje)
- komentarze użytkowników i kategorie

### 3. Wiki Encyclopedia (Django)
- tworzenie i edycja stron (Markdown)
- wyszukiwanie treści
- losowa strona i obsługa błędów

### 4. Mail Client (SPA / REST API)
- skrzynki mailowe (Inbox / Sent / Archive)
- dynamiczne ładowanie danych (SPA)
- komunikacja z API
- wysyłanie i odpowiadanie na wiadomości

### 5. Google Search Front-End
- wyszukiwanie standardowe i zaawansowane
- obsługa formularzy GET
- testowanie UI i walidacji formularzy

---

## 🤖 Testy automatyczne (Selenium WebDriver + Django Test Client)

W ramach nauki automatyzacji QA tworzę testy UI oraz backendowe z użyciem Selenium WebDriver (Python) oraz Django Test Client.

Testy znajdują się w folderze:

automation-tests

✔ test logowania (negative login test – invalid credentials)  
✔ test wyszukiwania Google (UI automation)  
✔ test rejestracji użytkownika (Django application)  
✔ test logiki quizu (backend functional test – Django Test Client)  
  - sprawdzenie inicjalizacji sesji użytkownika  
  - walidacja ustawienia początkowego wyniku (score = 0)  
  - symulacja rozpoczęcia quizu przez POST request  

---

Testy obejmują zarówno warstwę UI (Selenium), jak i logikę backendu aplikacji webowych (Django Test Client), co pozwala na pełniejsze pokrycie scenariuszy testowych.

## 🧪 Przykładowe scenariusze testowe

### 🔐 Login Test (Negative – UI Automation / Selenium)
- otwarcie strony logowania
- wpisanie niepoprawnych danych (invalid credentials)
- wysłanie formularza
- weryfikacja komunikatu błędu

---

### 🔎 Google Search Test (UI Automation / Selenium)
- otwarcie przeglądarki
- wejście na stronę Google
- wykonanie zapytania
- weryfikacja wyników wyszukiwania

---

### 📝 Register Test (Web Application – Functional Test)
- otwarcie formularza rejestracji
- wypełnienie pól (username, email, password)
- walidacja danych wejściowych
- sprawdzenie poprawnej rejestracji użytkownika

---

### 🧪 Quiz Application Test (Backend Functional Test – Django Test Client)
- wysłanie żądania POST do rozpoczęcia quizu
- inicjalizacja sesji użytkownika
- ustawienie początkowego wyniku (score = 0)
- przygotowanie struktury quizu (pytania, poziom trudności)
- walidacja poprawnej inicjalizacji stanu gry
---

## 🛠️ Technologie

- Python
- Selenium WebDriver
- ChromeDriver
- Django
- HTML / CSS / JavaScript
- REST API
- SQLite

---

## 🎯 Cel portfolio

Celem tego repozytorium jest pokazanie umiejętności:

- analizy aplikacji webowych
- myślenia testerskiego (QA mindset)
- projektowania testów manualnych i automatycznych
- automatyzacji testów UI (Selenium)
- zrozumienia działania systemów webowych

---

