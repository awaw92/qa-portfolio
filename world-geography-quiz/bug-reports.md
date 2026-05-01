# Bug Reports – World Geography Quiz

## Testowany projekt
https://github.com/awaw92/world-geography-quiz

---

### BUG_01 – Brak walidacji odpowiedzi
Kroki:
1. Rozpocznij quiz
2. Kliknij "Dalej" bez wyboru odpowiedzi

Oczekiwany rezultat:
System powinien wymusić wybór odpowiedzi

Aktualny rezultat:
Przechodzi dalej bez wyboru

---

### BUG_02 – Reset stanu po odświeżeniu
Kroki:
1. Rozpocznij quiz
2. Odśwież stronę

Oczekiwany rezultat:
Quiz kontynuuje od miejsca, w którym był

Aktualny rezultat:
Quiz zaczyna się od początku

---

### BUG_03 – Możliwość wielokrotnego kliknięcia
Kroki:
1. Szybko kliknij kilka razy w odpowiedź

Oczekiwany rezultat:
Jedna odpowiedź = jedna akcja

Aktualny rezultat:
System może zarejestrować niepoprawne zachowanie
