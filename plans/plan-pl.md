# Plan projektu: Klasyfikacja tekstu (człowiek vs AI) — POLSKI

Ten dokument opisuje pełny proces realizacji projektu klasyfikacji tekstu – od analizy danych wejściowych po interpretację wyników. Plan został przygotowany w sposób przejrzysty, tak aby czytelnik mógł zrozumieć **jak projekt był tworzony i jakie decyzje zostały podjęte**.

---

## 1. Definicja problemu

- Określić problem badawczy: rozpoznanie, czy dany tekst został napisany przez człowieka czy wygenerowany przez system AI.
- Traktować zadanie jako problem binarnej klasyfikacji tekstu.
- Jasno zaznaczyć zakres projektu: celem jest analiza różnic pomiędzy tekstami, a nie stworzenie uniwersalnego detektora AI.

---

## 2. Zapoznanie się ze zbiorem danych

- Przeanalizować źródło danych oraz ich ogólną charakterystykę.
- Sprawdzić:
  - strukturę danych,
  - dostępne etykiety,
  - język tekstów.
- Zidentyfikować potencjalne ograniczenia zbioru danych.

---

## 3. Wczytanie i wstępna inspekcja danych

- Wczytać dane do środowiska analitycznego.
- Sprawdzić:
  - liczbę rekordów,
  - nazwy i typy kolumn,
  - brakujące lub niepoprawne wartości.
- Przygotować dane do dalszej analizy.

---

## 4. Eksploracyjna analiza danych (EDA)

### 4.1 Analiza rozkładu klas
- Sprawdzić liczebność próbek w każdej klasie.
- Ocenić, czy występuje niezbalansowanie klas.

### 4.2 Analiza długości tekstu
- Przeanalizować długość tekstów:
  - w znakach,
  - w słowach,
  - w zdaniach.
- Porównać rozkłady długości pomiędzy klasami.
- Ocenić, czy długość tekstu może wpływać na wyniki klasyfikacji.

### 4.3 Analiza leksykalna
- Zbadać częstość występowania słów i wyrażeń.
- Porównać słownictwo obu klas.
- Ocenić różnorodność leksykalną tekstów.

### 4.4 Podsumowanie statystyczne
- Obliczyć podstawowe statystyki opisowe.
- Przedstawić wyniki w tabelach i na wykresach.

---

## 5. Czyszczenie i przygotowanie tekstów

- Ujednolicić format tekstu:
  - normalizacja zapisu,
  - usunięcie artefaktów technicznych.
- Zachować elementy istotne dla analizy stylu.
- Upewnić się, że wszystkie teksty są w tym samym języku.

---

## 6. Ujednolicenie zbioru danych

- Sprawdzić, czy teksty różnych klas są porównywalne pod względem długości i struktury.
- W razie potrzeby:
  - odfiltrować skrajne przypadki,
  - doprowadzić rozkłady do bardziej porównywalnej postaci.
- Udokumentować wszystkie zmiany wprowadzone w danych.

---

## 7. Ekstrakcja cech

### 7.1 Reprezentacja tekstu
- Przekształcić tekst do postaci numerycznej możliwej do wykorzystania przez modele.
- Opisać i uzasadnić wybraną metodę reprezentacji.

### 7.2 Cechy stylometryczne i statystyczne
- Obliczyć cechy opisujące styl i strukturę tekstu.
- Ocenić ich potencjalną wartość rozróżniającą klasy.

### 7.3 Przygotowanie cech
- Ujednolicić skalę cech numerycznych.
- Połączyć różne grupy cech w jedną reprezentację.

---

## 8. Budowa modeli klasyfikacyjnych

- Wybrać model bazowy do klasyfikacji.
- Zaimplementować spójny proces uczenia obejmujący przetwarzanie danych.
- Traktować model bazowy jako punkt odniesienia.

---

## 9. Porównanie modeli i strojenie

- Przetestować alternatywne modele.
- Porównać ich wyniki z modelem bazowym.
- Zbadać wpływ parametrów na jakość klasyfikacji.

---

## 10. Ocena jakości modeli

- Zastosować standardowe metryki klasyfikacyjne.
- Przeanalizować wyniki osobno dla każdej klasy.
- Zwizualizować błędy i poprawne predykcje.

---

## 11. Analiza błędów

- Przejrzeć błędnie sklasyfikowane przykłady.
- Spróbować wyjaśnić przyczyny błędów.
- Opisać ograniczenia zastosowanego podejścia.

---

## 12. Eksperymenty i porównania

- Porównać różne warianty przygotowania danych i cech.
- Ocenić wpływ poszczególnych decyzji projektowych.
- Sformułować wnioski z przeprowadzonych eksperymentów.

---

## 13. Testowanie i stabilność rozwiązania

- Sprawdzić poprawność kluczowych etapów przetwarzania.
- Upewnić się, że cały pipeline działa stabilnie.
- Zabezpieczyć podstawowe elementy testami.

---

## 14. Organizacja projektu

- Uporządkować strukturę kodu.
- Rozdzielić odpowiedzialności pomiędzy moduły.
- Dokumentować rozwój projektu za pomocą systemu kontroli wersji.

---

## 15. Wnioski końcowe

- Podsumować wykonane prace.
- Opisać zaobserwowane różnice pomiędzy tekstami.
- Wskazać mocne i słabe strony rozwiązania.
- Zaproponować możliwe kierunki dalszego rozwoju.

---

## 16. Dokumentacja i przejrzystość

- Przygotować dokumentację dostępną dla czytelnika zewnętrznego.
- Wyjaśnić zastosowane metody i decyzje projektowe.
- Zapewnić powtarzalność i czytelność projektu.
