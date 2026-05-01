# Bug Reports – Mail Client (SPA)

## Testowany projekt
https://github.com/awaw92/mail

---

### BUG_01 – Brak walidacji pustej wiadomości
Kroki:
1. Kliknij "Compose"
2. Kliknij "Send" bez treści

Oczekiwany rezultat:
System blokuje wysłanie pustej wiadomości

Aktualny rezultat:
Wiadomość może zostać wysłana

---

### BUG_02 – Brak potwierdzenia wysłania
Kroki:
1. Wyślij wiadomość

Oczekiwany rezultat:
Komunikat potwierdzający wysłanie

Aktualny rezultat:
Brak informacji zwrotnej

---

### BUG_03 – Opóźnione ładowanie wiadomości (SPA)
Kroki:
1. Otwórz Inbox
2. Przełącz między wiadomościami

Oczekiwany rezultat:
Natychmiastowa zmiana widoku

Aktualny rezultat:
Możliwe opóźnienia w renderowaniu treści
