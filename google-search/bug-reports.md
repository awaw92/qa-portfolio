# Bug Reports – Google Search Front-End

## Testowany projekt
https://github.com/awaw92/search

---

### BUG_01 – Brak obsługi pustego wyszukiwania
Kroki:
1. Kliknij "Search" bez wpisania tekstu

Oczekiwany rezultat:
Komunikat o konieczności wpisania frazy

Aktualny rezultat:
Brak reakcji lub pusta strona wyników

---

### BUG_02 – Brak walidacji formularza Advanced Search
Kroki:
1. Wypełnij tylko część pól
2. Kliknij "Search"

Oczekiwany rezultat:
System powinien walidować dane wejściowe

Aktualny rezultat:
Możliwe niepełne lub niepoprawne wyniki

---

### BUG_03 – Niespójne wyniki Images
Kroki:
1. Wyszukaj obraz
2. Porównaj z query tekstowym

Oczekiwany rezultat:
Spójne wyniki z zapytaniem

Aktualny rezultat:
Możliwe rozbieżności w wynikach
