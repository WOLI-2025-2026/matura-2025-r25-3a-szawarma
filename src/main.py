#!/usr/bin/env python3
# Wczytuje plik z symbolami, znajduje wszystkie kwadraty 3x3 z identycznymi symbolami
# i zapisuje wynik (liczba kwadratów oraz współrzędne środków) do pliku wynik_2_2.txt

from pathlib import Path

INPUT = Path(__file__).resolve().parents[1] / "zalaczniki-2025" / "symbole.txt"
OUTPUT = Path(__file__).resolve().parents[1] / "wynik_2_2.txt"


def find_3x3_squares(lines):
    """Zwraca listę par (row, col) - współrzędne środków kwadratów 3x3.
    Współrzędne liczone od 1 (tak jak w zadaniu).
    """
    if not lines:
        return []
    n = len(lines)
    m = len(lines[0])
    centers = []
    for i in range(n - 2):  # top row of 3x3
        for j in range(m - 2):  # left col of 3x3
            ch = lines[i][j]
            ok = True
            for di in range(3):
                # szybkie skrócenie pętli porównując całe kawałki
                if lines[i + di][j:j + 3] != ch * 3:
                    ok = False
                    break
            if ok:
                # center is (i+1, j+1) in 0-based -> +1 for 1-based center = i+2, j+2
                centers.append((i + 2, j + 2))
    return centers


def main():
    if not INPUT.exists():
        print(f"Plik wejściowy nie istnieje: {INPUT}")
        return

    with INPUT.open(encoding='utf-8') as f:
        lines = [line.rstrip('\n') for line in f]

    centers = find_3x3_squares(lines)

    # Format wyjścia: najpierw liczba kwadratów, potem pary (wiersz kolumna) środków.
    # Wszystko w jednej linii rozdzielone spacjami (zgodnie z przykładem: "1 6 3").
    parts = [str(len(centers))]
    for r, c in centers:
        parts.append(str(r))
        parts.append(str(c))
    out_line = " ".join(parts)

    # Zapis do pliku
    with OUTPUT.open('w', encoding='utf-8') as fw:
        fw.write(out_line + "\n")

    # Wypisz też na stdout
    print(out_line)


if __name__ == '__main__':
    main()
