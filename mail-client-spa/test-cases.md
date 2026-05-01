# Test Cases – Mail Client (SPA)

## Testowany projekt
https://github.com/awaw92/mail

---

### TC_01 – Wyświetlanie skrzynki Inbox
Kroki:
1. Otwórz aplikację
2. Przejdź do Inbox

Oczekiwany rezultat:
Wyświetlane są odebrane wiadomości

---

### TC_02 – Wysłanie wiadomości
Kroki:
1. Kliknij "Compose"
2. Wpisz odbiorcę, temat i treść
3. Kliknij "Send"

Oczekiwany rezultat:
Wiadomość trafia do Sent

---

### TC_03 – Otwieranie wiadomości
Kroki:
1. Kliknij wiadomość z listy

Oczekiwany rezultat:
Treść wiadomości wyświetla się bez przeładowania strony

---

### TC_04 – Archiwizacja wiadomości
Kroki:
1. Otwórz wiadomość
2. Kliknij "Archive"

Oczekiwany rezultat:
Wiadomość zostaje przeniesiona do archiwum

---

### TC_05 – Odpowiedź na wiadomość
Kroki:
1. Otwórz wiadomość
2. Kliknij "Reply"
3. Wyślij odpowiedź

Oczekiwany rezultat:
Odpowiedź zostaje wysłana i zapisana w Sent
