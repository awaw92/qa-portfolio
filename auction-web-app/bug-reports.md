# Bug Reports – Auction Web Application

## Testowany projekt
https://github.com/awaw92/commerce

---

### BUG_01 – Brak walidacji licytacji
Kroki:
1. Wejdź na aukcję
2. Wprowadź niższą kwotę niż aktualna
3. Kliknij "Place Bid"

Oczekiwany rezultat:
System odrzuca ofertę

Aktualny rezultat:
Oferta może zostać przyjęta

---

### BUG_02 – Możliwość dodania tej samej aukcji do watchlisty
Kroki:
1. Kliknij "Add to Watchlist" kilka razy

Oczekiwany rezultat:
Aukcja dodana tylko raz

Aktualny rezultat:
Możliwe duplikowanie

---

### BUG_03 – Brak komunikatu po dodaniu komentarza
Kroki:
1. Dodaj komentarz
2. Kliknij "Submit"

Oczekiwany rezultat:
Potwierdzenie dodania komentarza

Aktualny rezultat:
Brak informacji zwrotnej
