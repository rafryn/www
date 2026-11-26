# Jak dodać aktualność – instrukcja dla autora (ok. 5 minut)

## Pierwsze logowanie (raz)
1. Otwórz zaproszenie z e-maila od Pages CMS i kliknij link.
2. Zaloguj się (link w e-mailu albo konto GitHub, jeśli je masz).
3. Zapisz w telefonie/przeglądarce adres panelu: **https://app.pagescms.org**

## Nowy wpis
1. W panelu wybierz **Aktualności** → **Add an entry** (Dodaj wpis).
2. Wypełnij pola:
   - **Tytuł** – krótko i konkretnie, np. „Mikołajkowy trening z rekordową frekwencją”.
   - **Kategoria** – wybierz z listy.
   - **Zdjęcie główne** – najlepiej poziome. Zdjęcie z telefonu jest OK: strona sama je zmniejszy i usunie z niego lokalizację GPS.
   - **Co widać na zdjęciu** – jedno zdanie, np. „Grupa żaków na starcie wyścigu”.
   - **Podpis** – opcjonalnie, np. „Fot. Jan Kowalski”.
   - **Treść** – 3–6 zdań. Pierwszy akapit to zapowiedź na liście aktualności.
3. Kliknij **Save** (Zapisz). Wpis pojawi się na stronie po 2–3 minutach.

## Poprawka lub usunięcie
Otwórz wpis z listy w panelu, popraw i zapisz. Każda zmiana ma historię – pomyłkę da się cofnąć.

## Zasady
- **Zdjęcia dzieci tylko ze zgodą rodziców** na publikację wizerunku.
- Bez danych osobowych poza imieniem i nazwiskiem zawodnika oraz wynikiem.
- Bez nazwisk dzieci przy zdjęciach grupowych z zajęć dla najmłodszych.
- Wpis najlepiej do 48 godzin po wydarzeniu. Ten sam tekst + link do wpisu na Facebooku.

---

## Dla administratora (konfiguracja panelu)
- Ustawienia panelu: plik `.pages.yml` (pola formularza, folder zdjęć `assets/img/aktualnosci`).
- Automatyczne zmniejszanie zdjęć i usuwanie metadanych: `.github/workflows/publikacja.yml` + `.github/scripts/zdjecia.py`.
- Autorzy zaproszeni e-mailem widzą tylko Aktualności i zdjęcia. Nie mogą zmieniać `.pages.yml`, innych podstron ani zapraszać kolejnych osób.
- Bez panelu: wpis to plik `_posts/RRRR-MM-DD-tytul.md` (wzór: dowolny istniejący wpis).
