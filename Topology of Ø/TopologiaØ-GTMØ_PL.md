# Topologia Ø w GTMØ – Dokumentacja

Ten plik stanowi implementację topologii Ø jako kluczowego składnika metapoznawczego systemu GTMØ (Generalized Theory of Mathematical Indefiniteness).

## 🔹 Zawartość i funkcjonalności

### 1. Trajektoria φ(t)
- Funkcja `phi(t)` odwzorowuje stany poznawcze:
  - `0` – niebyt
  - `1` – byt
  - `∞` – nieskończoność
  - `Ø` – niedefinitywność

### 2. Heurystyka E(x)
- Funkcja `E(x)` mierzy odległość epistemiczną od Ø.
- Definicja: `E(x) = 1 - exp(-abs(x - Ø))`
- Wartość `E(Ø) = 0`, im dalej od Ø, tym bliżej 1.

### 3. Operator φ′(t)
- Różniczka trajektorii poznawczej: `φ′(t) ≈ [φ(t + Δt) − φ(t)] / Δt`

### 4. Klasyfikator Ψᴷ
- Funkcja `classify_PsiK(x)` dzieli punkty poznania:
  - `Ψᴷ = Ø` jeśli `E(x) < δ`
  - `Ψᴷ = klasyczne` w przeciwnym wypadku

## 🔹 Wizualizacje
- `visualize_phi_trajectory()`
- `nonlinear_emergence_mapping()`
- `visualize_heatmap_Ø()`
- `interactive_phi_analysis()`
- `real_time_analysis()`

## 🔹 Testy jednostkowe
- Podstawowe testy: poprawność E(x), φ(t), klasyfikacja Ψᴷ
- Złożone testy: φ′(t), zakres emergencji, zgodność E(x) z Ø, osobliwości

## 📂 Plik źródłowy
- Nazwa: `Topologiaø-gtmø.py`
- Format: Python 3 + Matplotlib + NumPy
