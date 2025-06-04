# Istniejące importy
from enum import Enum
import numpy as np
from typing import Union, Tuple, List, Any # Dodano dla type hinting

# --- CZĘŚĆ GEOMETRYCZNA ---

# Cognitive layers enumeration
class CognitiveLayer(Enum):
    P0 = 'P₀'
    R = 'R'
    I = 'I'
    A = 'A'
    O_SLASH = 'Ø' # Używamy O_SLASH, ponieważ Ø nie jest prawidłowym identyfikatorem Python
                  # Wartość enuma to nadal 'Ø'
    
    def __str__(self):
        return self.value

# Pełna definicja metryki poznawczej z wyraźnymi odległościami między warstwami
# Complete definition of cognitive metric with explicit distances between layers
def cognitive_metric_complete(layer1: CognitiveLayer, layer2: CognitiveLayer) -> float:
    infinite = float('inf')
    # Słownik przechowujący odległości między bezpośrednio połączonymi warstwami
    # oraz niektóre predefiniowane sumy dla wygody.
    distances = {
        (CognitiveLayer.P0, CognitiveLayer.R): 1.0,
        (CognitiveLayer.R, CognitiveLayer.I): 2.0,
        (CognitiveLayer.I, CognitiveLayer.A): 3.0,
        (CognitiveLayer.A, CognitiveLayer.O_SLASH): infinite,
        # Predefiniowane sumy dla często używanych ścieżek
        (CognitiveLayer.P0, CognitiveLayer.I): 3.0,  # P0 -> R (1) + R -> I (2)
        (CognitiveLayer.P0, CognitiveLayer.A): 6.0,  # P0 -> R (1) + R -> I (2) + I -> A (3)
        (CognitiveLayer.R, CognitiveLayer.A): 5.0,   # R -> I (2) + I -> A (3)
        # Odległości do O_SLASH z innych warstw (poza A) również są nieskończone
        (CognitiveLayer.P0, CognitiveLayer.O_SLASH): infinite,
        (CognitiveLayer.R, CognitiveLayer.O_SLASH): infinite,
        (CognitiveLayer.I, CognitiveLayer.O_SLASH): infinite,
    }

    if layer1 == layer2:
        return 0.0

    # Sprawdzenie dla O_SLASH jako jednego z argumentów
    is_A_OSlash_pair = (layer1 == CognitiveLayer.A and layer2 == CognitiveLayer.O_SLASH) or \
                       (layer1 == CognitiveLayer.O_SLASH and layer2 == CognitiveLayer.A)

    if (layer1 == CognitiveLayer.O_SLASH or layer2 == CognitiveLayer.O_SLASH) and not is_A_OSlash_pair:
        return infinite

    # Pobranie odległości, uwzględniając symetrię
    distance = distances.get((layer1, layer2)) or distances.get((layer2, layer1))
    
    return distance if distance is not None else infinite


# Dynamiczna implementacja metryki poznawczej jako sumy odległości pośrednich (NAPRAWIONA/UPROSZCZONA)
def cognitive_metric_dynamic(layer1: CognitiveLayer, layer2: CognitiveLayer) -> float:
    infinite = float('inf')
    # Definicja uporządkowanej ścieżki warstw poznawczych
    path_order: List[CognitiveLayer] = [CognitiveLayer.P0, CognitiveLayer.R, CognitiveLayer.I, CognitiveLayer.A, CognitiveLayer.O_SLASH]
    
    if layer1 == layer2:
        return 0.0
    
    try:
        # Znalezienie indeksów warstw w uporządkowanej ścieżce
        idx1 = path_order.index(layer1)
        idx2 = path_order.index(layer2)
        
        # Zapewnienie, że idx1 jest mniejszy lub równy idx2
        if idx1 > idx2:
            idx1, idx2 = idx2, idx1 # Zamiana miejscami

        # Odległości między sąsiednimi warstwami w zdefiniowanej ścieżce
        # P0->R (1), R->I (2), I->A (3), A->Ø (inf)
        distances_between_adjacent = [1.0, 2.0, 3.0, infinite]
        
        current_sum = 0.0
        # Iteracja przez segmenty ścieżki
        for i in range(idx1, idx2):
            # Sprawdzenie, czy indeks i jest prawidłowy dla distances_between_adjacent
            if i < len(distances_between_adjacent):
                current_sum += distances_between_adjacent[i]
            else:
                # To nie powinno się zdarzyć, jeśli path_order i distances_between_adjacent są spójne
                return infinite 
            
            # Optymalizacja: jeśli suma już jest nieskończona, nie ma potrzeby dalej sumować
            if current_sum == infinite:
                break
        return current_sum

    except ValueError:
        # Jeśli warstwa nie znajduje się w path_order (nie powinno się zdarzyć dla CognitiveLayer)
        return infinite

# Funkcja osadzania (Embedding function definition)
def embedding_function(layer: CognitiveLayer) -> np.ndarray:
    # Słownik mapujący warstwy poznawcze na ich reprezentacje wektorowe w przestrzeni ℝ³
    embeddings = {
        CognitiveLayer.P0: np.array([0, 0, 0]),
        CognitiveLayer.R: np.array([1, 0, 0]),
        CognitiveLayer.I: np.array([1, 1, 0]),
        CognitiveLayer.A: np.array([1, 1, 1]),
        CognitiveLayer.O_SLASH: np.array([np.nan, np.nan, np.inf]), # Reprezentacja Ø jako punktu osobliwego
    }
    return embeddings[layer]

# Definicja zbioru singularnego Ø (Singular set Ø definition)
class SingularSetOSlash: # Zmieniono nazwę klasy, aby uniknąć konfliktu z elementem enum
    center = np.array([np.nan, np.nan, np.inf]) # Centrum geometryczne osobliwości
    description = (
        "Granica geometryczna systemu, metrycznie nieosiągalna, lokalizująca źródło deformacji poznawczej."
        "Geometric boundary of the system, metrically unattainable, locating the source of cognitive deformation."
    )

# --- ALGEBRA SYMBOLICZNA SYSTEMU ŁØ (NOWA CZĘŚĆ) ---

# Definicja specjalnego stanu ∅ (nihil-stan, pustka)
class NihilStateClass:
    """
    Reprezentuje stan ∅ (pustka, nihil-stan) w algebrze Systemu ŁØ.
    Jest to całkowity brak treści poznawczej, "wymazana kartka".
    """
    def __repr__(self):
        return "∅"

NIHIL = NihilStateClass() # Singleton reprezentujący ∅

# Typ dla wyników operacji, które mogą zwrócić warstwę lub nihil-stan
AlgebraicResult = Union[CognitiveLayer, NihilStateClass, int] # int dla operatora granicznego

# 1. Zbiór K i relacja ≤
PATH_ORDER: List[CognitiveLayer] = [CognitiveLayer.P0, CognitiveLayer.R, CognitiveLayer.I, CognitiveLayer.A, CognitiveLayer.O_SLASH] # POPRAWKA TUTAJ

def relacja_zlozonosci(k1: CognitiveLayer, k2: CognitiveLayer) -> bool:
    """
    Implementacja relacji poznawczej złożoności (≤).
    P₀ ≤ R ≤ I ≤ A ≤ Ø
    """
    try:
        return PATH_ORDER.index(k1) <= PATH_ORDER.index(k2)
    except ValueError:
        return False # Jeśli któraś warstwa nie jest w PATH_ORDER (nie powinno się zdarzyć)

# 2. Operatory Algebry Symbolicznej

def fuzja_poznawcza(k1: Union[CognitiveLayer, NihilStateClass], k2: Union[CognitiveLayer, NihilStateClass]) -> AlgebraicResult:
    """
    Operator fuzji poznawczej (⊕). (NAPRAWIONY)
    Reguły:
    • x ⊕ x = x (dodano)
    • P₀ ⊕ R = R
    • R ⊕ I = I
    • I ⊕ A = A
    • x ⊕ Ø = A  (gdzie Ø to CognitiveLayer.O_SLASH)
    • Ø ⊕ Ø = Ø
    • Dodatkowa reguła z przykładu: ∅ ⊕ R = R (NIHIL ⊕ R = R)
    """
    # Obsługa NIHIL (∅)
    if k1 == NIHIL:
        return k2 if isinstance(k2, CognitiveLayer) else NIHIL 
    if k2 == NIHIL:
        return k1 if isinstance(k1, CognitiveLayer) else NIHIL

    if not isinstance(k1, CognitiveLayer) or not isinstance(k2, CognitiveLayer):
        raise TypeError(f"Niewspierane typy dla fuzji: {type(k1)}, {type(k2)}")

    # Reguły z Ø (CognitiveLayer.O_SLASH)
    if k1 == CognitiveLayer.O_SLASH and k2 == CognitiveLayer.O_SLASH:
        return CognitiveLayer.O_SLASH
    if k1 == CognitiveLayer.O_SLASH or k2 == CognitiveLayer.O_SLASH:
        return CognitiveLayer.A
    
    # Reguła x ⊕ x = x (dla przypadków niebędących O_SLASH)
    if k1 == k2:
        return k1

    # Reguły podstawowe (zakładając przemienność dla uproszczenia definicji)
    pairs = {
        frozenset({CognitiveLayer.P0, CognitiveLayer.R}): CognitiveLayer.R,
        frozenset({CognitiveLayer.R, CognitiveLayer.I}): CognitiveLayer.I,
        frozenset({CognitiveLayer.I, CognitiveLayer.A}): CognitiveLayer.A,
    }
    
    result = pairs.get(frozenset({k1, k2}))
    if result is not None:
        return result
    
    raise ValueError(f"Niezdefiniowana fuzja poznawcza dla pary: ({k1}, {k2})")


def sprzezenie_pojeciowe(k1: CognitiveLayer, k2: CognitiveLayer) -> CognitiveLayer:
    """
    Operator sprzężenia pojęciowego (⊗). (NAPRAWIONY - dodano symetrię dla R)
    Reguły:
    • x ⊗ x = x
    • P₀ ⊗ R = P₀  (i R ⊗ P₀ = P₀)
    • I ⊗ R = R    (i R ⊗ I = R)
    • A ⊗ R = R    (i R ⊗ A = R)
    • Ø ⊗ x = Ø (gdzie Ø to CognitiveLayer.O_SLASH)
    """
    # Reguła Ø ⊗ x = Ø
    if k1 == CognitiveLayer.O_SLASH or k2 == CognitiveLayer.O_SLASH: 
        return CognitiveLayer.O_SLASH
    
    # Reguła x ⊗ x = x
    if k1 == k2:
        return k1

    # Reguły specyficzne z uwzględnieniem symetrii dla par z R
    if (k1 == CognitiveLayer.P0 and k2 == CognitiveLayer.R) or \
       (k1 == CognitiveLayer.R and k2 == CognitiveLayer.P0):
        return CognitiveLayer.P0
       
    if (k1 == CognitiveLayer.I and k2 == CognitiveLayer.R) or \
       (k1 == CognitiveLayer.R and k2 == CognitiveLayer.I):
        return CognitiveLayer.R
       
    if (k1 == CognitiveLayer.A and k2 == CognitiveLayer.R) or \
       (k1 == CognitiveLayer.R and k2 == CognitiveLayer.A):
        return CognitiveLayer.R
           
    raise ValueError(f"Niezdefiniowane sprzężenie pojęciowe dla pary: ({k1}, {k2})")


def negacja_metaontologiczna(k: CognitiveLayer) -> CognitiveLayer:
    """
    Operator negacji metaontologicznej (¬).
    Reguły:
    • ¬P₀ = A
    • ¬R = A
    • ¬I = P₀
    • ¬A = P₀
    • ¬Ø = Ø
    """
    if k == CognitiveLayer.P0: return CognitiveLayer.A
    if k == CognitiveLayer.R: return CognitiveLayer.A
    if k == CognitiveLayer.I: return CognitiveLayer.P0
    if k == CognitiveLayer.A: return CognitiveLayer.P0
    if k == CognitiveLayer.O_SLASH: return CognitiveLayer.O_SLASH
    raise ValueError(f"Niezdefiniowana negacja metaontologiczna dla: {k}")


def metaoperator_deformacji(k: CognitiveLayer) -> AlgebraicResult:
    """
    Metaoperator Ø (deformacja poznania). Nazwa funkcji zmieniona, by uniknąć kolizji.
    Reguły:
    • Ø(P₀) = ∅ (NIHIL)
    • Ø(R) = ∅ (NIHIL)
    • Ø(I) = ∅ (NIHIL)
    • Ø(A) = Ø (CognitiveLayer.O_SLASH)
    • Ø(Ø) = Ø (CognitiveLayer.O_SLASH)
    """
    if k == CognitiveLayer.P0: return NIHIL
    if k == CognitiveLayer.R: return NIHIL
    if k == CognitiveLayer.I: return NIHIL
    if k == CognitiveLayer.A: return CognitiveLayer.O_SLASH
    if k == CognitiveLayer.O_SLASH: return CognitiveLayer.O_SLASH
    raise ValueError(f"Niezdefiniowana operacja metaoperatora deformacji dla: {k}")


def samoswiadomosc_refleksja(k: CognitiveLayer) -> CognitiveLayer:
    """
    Operator samoświadomości / refleksji (Ψ).
    Reguły:
    • Ψ(P₀) = R
    • Ψ(R) = I
    • Ψ(I) = A
    • Ψ(A) = Ø (CognitiveLayer.O_SLASH)
    • Ψ(Ø) = Ø (CognitiveLayer.O_SLASH)
    """
    if k == CognitiveLayer.P0: return CognitiveLayer.R
    if k == CognitiveLayer.R: return CognitiveLayer.I
    if k == CognitiveLayer.I: return CognitiveLayer.A
    if k == CognitiveLayer.A: return CognitiveLayer.O_SLASH
    if k == CognitiveLayer.O_SLASH: return CognitiveLayer.O_SLASH
    raise ValueError(f"Niezdefiniowana operacja samoświadomości/refleksji dla: {k}")

def operator_graniczny(k: CognitiveLayer) -> AlgebraicResult:
    """
    Operator graniczny (∂).
    Reguły:
    • ∂(P₀) = 0
    • ∂(R) = 0
    • ∂(I) = 1
    • ∂(A) = Ø (CognitiveLayer.O_SLASH)
    • ∂(Ø) = Ø (CognitiveLayer.O_SLASH)
    """
    if k == CognitiveLayer.P0: return 0
    if k == CognitiveLayer.R: return 0
    if k == CognitiveLayer.I: return 1
    if k == CognitiveLayer.A: return CognitiveLayer.O_SLASH
    if k == CognitiveLayer.O_SLASH: return CognitiveLayer.O_SLASH
    raise ValueError(f"Niezdefiniowana operacja operatora granicznego dla: {k}")


def inicjalizacja_swiadomosci() -> CognitiveLayer:
    """
    Operator inicjalizacji świadomości (I).
    Reguła: I() = P₀
    Zakładamy, że operator I nie przyjmuje argumentów (lub przyjmuje ∅, co jest tu pominięte).
    """
    return CognitiveLayer.P0


# --- PRZYKŁADY UŻYCIA ---
if __name__ == "__main__":
    print("--- CZĘŚĆ GEOMETRYCZNA ---")
    # Przykłady dla metryki
    print(f"Odległość (complete) R ↔ A: {cognitive_metric_complete(CognitiveLayer.R, CognitiveLayer.A)}")
    print(f"Odległość (dynamic) P₀ ↔ A: {cognitive_metric_dynamic(CognitiveLayer.P0, CognitiveLayer.A)}") # Oczekiwane 6.0
    print(f"Odległość (dynamic) R ↔ A: {cognitive_metric_dynamic(CognitiveLayer.R, CognitiveLayer.A)}") # Oczekiwane 5.0
    print(f"Odległość (dynamic) I ↔ O_SLASH: {cognitive_metric_dynamic(CognitiveLayer.I, CognitiveLayer.O_SLASH)}") # Oczekiwane inf
    print(f"Odległość (dynamic) A ↔ O_SLASH: {cognitive_metric_dynamic(CognitiveLayer.A, CognitiveLayer.O_SLASH)}") # Oczekiwane inf
    print(f"Odległość (dynamic) P₀ ↔ O_SLASH: {cognitive_metric_dynamic(CognitiveLayer.P0, CognitiveLayer.O_SLASH)}") # Oczekiwane inf


    # Przykład dla funkcji osadzania
    print(f"Osadzenie warstwy A: {embedding_function(CognitiveLayer.A)}")
    print(f"Osadzenie warstwy O_SLASH: {embedding_function(CognitiveLayer.O_SLASH)}")

    # Przykład dla zbioru singularnego
    print(f"Opis zbioru singularnego Ø: {SingularSetOSlash.description}")

    print("\n--- ALGEBRA SYMBOLICZNA SYSTEMU ŁØ ---")
    
    # Przykłady użycia operatorów algebry symbolicznej
    print(f"P₀: {CognitiveLayer.P0}")
    print(f"R: {CognitiveLayer.R}")
    print(f"I: {CognitiveLayer.I}")
    print(f"A: {CognitiveLayer.A}")
    print(f"Ø (element): {CognitiveLayer.O_SLASH}")
    print(f"∅ (nihil-stan): {NIHIL}")

    print("\nPrzykłady relacji złożoności (≤):")
    print(f"P₀ ≤ R: {relacja_zlozonosci(CognitiveLayer.P0, CognitiveLayer.R)}") # True
    print(f"R ≤ P₀: {relacja_zlozonosci(CognitiveLayer.R, CognitiveLayer.P0)}") # False
    print(f"A ≤ O_SLASH: {relacja_zlozonosci(CognitiveLayer.A, CognitiveLayer.O_SLASH)}") # True
    print(f"P₀ ≤ O_SLASH: {relacja_zlozonosci(CognitiveLayer.P0, CognitiveLayer.O_SLASH)}") # True

    print("\nPrzykłady fuzji poznawczej (⊕):")
    print(f"P₀ ⊕ P₀ = {fuzja_poznawcza(CognitiveLayer.P0, CognitiveLayer.P0)}") # Oczekiwane: P₀
    print(f"P₀ ⊕ R = {fuzja_poznawcza(CognitiveLayer.P0, CognitiveLayer.R)}") # Oczekiwane: R
    print(f"R ⊕ I = {fuzja_poznawcza(CognitiveLayer.R, CognitiveLayer.I)}")   # Oczekiwane: I
    print(f"I ⊕ A = {fuzja_poznawcza(CognitiveLayer.I, CognitiveLayer.A)}")   # Oczekiwane: A
    print(f"P₀ ⊕ Ø = {fuzja_poznawcza(CognitiveLayer.P0, CognitiveLayer.O_SLASH)}") # Oczekiwane: A
    print(f"Ø ⊕ Ø = {fuzja_poznawcza(CognitiveLayer.O_SLASH, CognitiveLayer.O_SLASH)}") # Oczekiwane: Ø
    print(f"∅ ⊕ R = {fuzja_poznawcza(NIHIL, CognitiveLayer.R)}") # Oczekiwane: R
    print(f"A ⊕ ∅ = {fuzja_poznawcza(CognitiveLayer.A, NIHIL)}") # Oczekiwane: A
    
    print("\nPrzykłady sprzężenia pojęciowego (⊗):")
    print(f"R ⊗ R = {sprzezenie_pojeciowe(CognitiveLayer.R, CognitiveLayer.R)}") # Oczekiwane: R
    print(f"P₀ ⊗ R = {sprzezenie_pojeciowe(CognitiveLayer.P0, CognitiveLayer.R)}") # Oczekiwane: P₀
    print(f"R ⊗ P₀ = {sprzezenie_pojeciowe(CognitiveLayer.R, CognitiveLayer.P0)}") # Oczekiwane: P₀ (symetria)
    print(f"I ⊗ R = {sprzezenie_pojeciowe(CognitiveLayer.I, CognitiveLayer.R)}")   # Oczekiwane: R
    print(f"R ⊗ I = {sprzezenie_pojeciowe(CognitiveLayer.R, CognitiveLayer.I)}")   # Oczekiwane: R (symetria)
    print(f"A ⊗ R = {sprzezenie_pojeciowe(CognitiveLayer.A, CognitiveLayer.R)}")   # Oczekiwane: R
    print(f"R ⊗ A = {sprzezenie_pojeciowe(CognitiveLayer.R, CognitiveLayer.A)}")   # Oczekiwane: R (symetria)
    print(f"Ø ⊗ P₀ = {sprzezenie_pojeciowe(CognitiveLayer.O_SLASH, CognitiveLayer.P0)}") # Oczekiwane: Ø
    print(f"R ⊗ Ø = {sprzezenie_pojeciowe(CognitiveLayer.R, CognitiveLayer.O_SLASH)}") # Oczekiwane: Ø

    print("\nPrzykłady negacji metaontologicznej (¬):")
    print(f"¬P₀ = {negacja_metaontologiczna(CognitiveLayer.P0)}") # Oczekiwane: A
    print(f"¬R = {negacja_metaontologiczna(CognitiveLayer.R)}")   # Oczekiwane: A
    print(f"¬I = {negacja_metaontologiczna(CognitiveLayer.I)}")   # Oczekiwane: P₀
    print(f"¬A = {negacja_metaontologiczna(CognitiveLayer.A)}")   # Oczekiwane: P₀
    print(f"¬Ø = {negacja_metaontologiczna(CognitiveLayer.O_SLASH)}") # Oczekiwane: Ø

    print("\nPrzykłady metaoperatora deformacji (Ø(...)):")
    print(f"Ø(P₀) = {metaoperator_deformacji(CognitiveLayer.P0)}") # Oczekiwane: ∅ (NIHIL)
    print(f"Ø(R) = {metaoperator_deformacji(CognitiveLayer.R)}")   # Oczekiwane: ∅ (NIHIL)
    print(f"Ø(I) = {metaoperator_deformacji(CognitiveLayer.I)}")   # Oczekiwane: ∅ (NIHIL)
    print(f"Ø(A) = {metaoperator_deformacji(CognitiveLayer.A)}")   # Oczekiwane: Ø
    print(f"Ø(Ø) = {metaoperator_deformacji(CognitiveLayer.O_SLASH)}") # Oczekiwane: Ø

    print("\nPrzykłady samoświadomości/refleksji (Ψ):")
    print(f"Ψ(P₀) = {samoswiadomosc_refleksja(CognitiveLayer.P0)}") # Oczekiwane: R
    print(f"Ψ(R) = {samoswiadomosc_refleksja(CognitiveLayer.R)}")   # Oczekiwane: I
    print(f"Ψ(I) = {samoswiadomosc_refleksja(CognitiveLayer.I)}")   # Oczekiwane: A
    print(f"Ψ(A) = {samoswiadomosc_refleksja(CognitiveLayer.A)}")   # Oczekiwane: Ø
    print(f"Ψ(Ø) = {samoswiadomosc_refleksja(CognitiveLayer.O_SLASH)}") # Oczekiwane: Ø

    print("\nPrzykłady operatora granicznego (∂):")
    print(f"∂(P₀) = {operator_graniczny(CognitiveLayer.P0)}") # Oczekiwane: 0
    print(f"∂(R) = {operator_graniczny(CognitiveLayer.R)}")   # Oczekiwane: 0
    print(f"∂(I) = {operator_graniczny(CognitiveLayer.I)}")   # Oczekiwane: 1
    print(f"∂(A) = {operator_graniczny(CognitiveLayer.A)}")   # Oczekiwane: Ø
    print(f"∂(Ø) = {operator_graniczny(CognitiveLayer.O_SLASH)}") # Oczekiwane: Ø

    print("\nPrzykład inicjalizacji świadomości (I()):")
    print(f"I() = {inicjalizacja_swiadomosci()}") # Oczekiwane: P₀

    print("\n--- PRZYKŁADOWE RÓWNANIA Z ALGEBRY ---")
    # Ψ(Ψ(R)) = A
    psi_R = samoswiadomosc_refleksja(CognitiveLayer.R) # Wynik: I
    wynik_psi_psi_R = samoswiadomosc_refleksja(psi_R)   # Wynik: A
    print(f"Ψ(Ψ(R)) = Ψ({psi_R}) = {wynik_psi_psi_R} (Oczekiwane: A)")

    # P₀ ⊕ R ⊕ I = I
    p0_plus_r = fuzja_poznawcza(CognitiveLayer.P0, CognitiveLayer.R) # Wynik: R
    wynik_p0_r_i = fuzja_poznawcza(p0_plus_r, CognitiveLayer.I)      # Wynik: I
    print(f"(P₀ ⊕ R) ⊕ I = ({p0_plus_r}) ⊕ I = {wynik_p0_r_i} (Oczekiwane: I)")

    # Ø(P₀) ⊕ R = R
    meta_p0 = metaoperator_deformacji(CognitiveLayer.P0) # Wynik: NIHIL (∅)
    # Zakładamy, że ∅ ⊕ R = R, co jest obsłużone w fuzja_poznawcza
    wynik_meta_p0_plus_r = fuzja_poznawcza(meta_p0, CognitiveLayer.R) # Wynik: R
    print(f"Ø(P₀) ⊕ R = {meta_p0} ⊕ R = {wynik_meta_p0_plus_r} (Oczekiwane: R)")
    
    # Ø(A) = Ø
    wynik_meta_A = metaoperator_deformacji(CognitiveLayer.A) # Wynik: CognitiveLayer.O_SLASH (Ø)
    print(f"Ø(A) = {wynik_meta_A} (Oczekiwane: Ø)")
