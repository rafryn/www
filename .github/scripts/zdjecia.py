"""Zmniejsza zdjęcia i usuwa z nich metadane (w tym lokalizację GPS).

Uruchamiane automatycznie przez GitHub Actions przy każdej zmianie strony.
Działa tylko na zdjęciach, które tego wymagają – pozostałe zostawia bez zmian.
Pomija logotypy (assets/img/logo, assets/img/partnerzy).
"""
import sys
from pathlib import Path
from PIL import Image, ImageOps

MAX_BOK = 1600          # dłuższy bok w pikselach
JAKOSC_JPG = 80
POMIN = {"logo", "partnerzy"}
ROZSZERZENIA = {".jpg", ".jpeg", ".png", ".webp"}


def wymaga_zmiany(im: Image.Image) -> bool:
    ma_metadane = bool(im.getexif()) or "exif" in im.info or "xmp" in im.info
    za_duze = max(im.size) > MAX_BOK
    return ma_metadane or za_duze


def przetworz(sciezka: Path) -> bool:
    with Image.open(sciezka) as im:
        if not wymaga_zmiany(im):
            return False
        fmt = im.format
        im = ImageOps.exif_transpose(im)          # poprawny obrót zdjęcia z telefonu
        if max(im.size) > MAX_BOK:
            im.thumbnail((MAX_BOK, MAX_BOK), Image.LANCZOS)
        # Zapis bez parametru exif/xmp/icc = plik bez metadanych (w tym bez GPS)
        if fmt == "JPEG":
            im.convert("RGB").save(sciezka, "JPEG", quality=JAKOSC_JPG, optimize=True, progressive=True)
        elif fmt == "WEBP":
            im.save(sciezka, "WEBP", quality=JAKOSC_JPG)
        else:
            im.save(sciezka, "PNG", optimize=True)
    return True


def main(katalog: str) -> None:
    zmienione = 0
    for p in sorted(Path(katalog).rglob("*")):
        if p.suffix.lower() not in ROZSZERZENIA or POMIN & set(p.parts):
            continue
        try:
            if przetworz(p):
                zmienione += 1
                print(f"poprawiono: {p}")
        except Exception as e:  # uszkodzony plik nie zatrzymuje publikacji
            print(f"pominięto {p}: {e}")
    print(f"Gotowe. Zmienione zdjęcia: {zmienione}")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "assets/img")
