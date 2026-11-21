# Jak dodać aktualność (ok. 10 minut)

## Sposób 1 – przez Claude (najprościej)
Wklej w rozmowie z Claude tytuł, tekst i zdjęcie. Claude przygotuje wpis jako propozycję zmian, a Ty klikasz **Merge** na GitHubie.

## Sposób 2 – samodzielnie na GitHubie
1. **Zdjęcie:** wejdź do folderu `assets/img` → **Add file → Upload files** → wgraj zdjęcie.
   Nazwa bez spacji i polskich znaków, np. `mistrzostwa-polski-2026.jpg`. Najlepiej ok. 1400 px szerokości.
2. **Wpis:** wejdź do folderu `_posts` → **Add file → Create new file**.
   Nazwa pliku: `RRRR-MM-DD-tytul-bez-polskich-znakow.md`, np. `2026-12-05-mikolajkowy-trening.md`.
3. Wklej wzór i podmień treść:

```
---
layout: post
title: "Tytuł wpisu"
kategoria: Szosa
zdjecie: /assets/img/nazwa-zdjecia.jpg
zdjecie_opis: "Krótki opis, co widać na zdjęciu"
---
Pierwszy akapit – to on pokaże się jako zapowiedź na liście aktualności.

Kolejne akapity oddzielaj pustą linią.

**Pogrubienie** i [link](https://adres.pl) działają tak jak tutaj.
```

4. Kliknij **Commit changes**. Wpis pojawi się na stronie po 1–2 minutach.

## Kategorie (wpisuj dokładnie tak)
Szosa · Tor · Przełaj · Szkoły · Z życia klubu · Partnerzy

## Zasady
- Zdjęcia dzieci tylko ze zgodą rodziców na publikację wizerunku.
- Nie wpisuj danych osobowych poza imieniem i nazwiskiem zawodnika oraz wynikiem.
- Pomyłka? Każda zmiana ma historię – w zakładce **Commits** można ją cofnąć.
