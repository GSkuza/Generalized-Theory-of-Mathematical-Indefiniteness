from enum import Enum
import numpy as np

# Cognitive layers enumeration
class CognitiveLayer(Enum):
    P0 = 'P₀'
    R = 'R'
    I = 'I'
    A = 'A'
    Ø = 'Ø'

# Pełna definicja metryki poznawczej z wyraźnymi odległościami między warstwami
# Complete definition of cognitive metric with explicit distances between layers
# Bezpośrednio odnosi się do definicji warstw poznawczych w:
# Directly refers to cognitive layer definitions in:
# https://github.com/GSkuza/Generalized-Theory-of-Mathematical-Indefiniteness/tree/main

def cognitive_metric_complete(layer1, layer2):
    infinite = float('inf')
    distances = {
        (CognitiveLayer.P0, CognitiveLayer.R): 1,
        (CognitiveLayer.R, CognitiveLayer.I): 2,
        (CognitiveLayer.I, CognitiveLayer.A): 3,
        (CognitiveLayer.A, CognitiveLayer.Ø): infinite,
        (CognitiveLayer.P0, CognitiveLayer.I): 3,  # 1 + 2
        (CognitiveLayer.P0, CognitiveLayer.A): 6,  # 1 + 2 + 3
        (CognitiveLayer.R, CognitiveLayer.A): 5,   # 2 + 3
        (CognitiveLayer.P0, CognitiveLayer.Ø): infinite,
        (CognitiveLayer.R, CognitiveLayer.Ø): infinite,
        (CognitiveLayer.I, CognitiveLayer.Ø): infinite,
    }

    if layer1 == layer2:
        return 0

    if CognitiveLayer.Ø in (layer1, layer2):
        return infinite

    distance = distances.get((layer1, layer2)) or distances.get((layer2, layer1))
    return distance if distance is not None else infinite

# Dowody formalne dotyczące metryki poznawczej
# Formal proofs regarding cognitive metric

# Dowód 1: Symetria metryki poznawczej (Metric symmetry)
# Metryka poznawcza jest symetryczna: d(x,y) = d(y,x)
# The cognitive metric is symmetric: d(x,y) = d(y,x)

# Dowód 2: Nieskończona odległość do osobliwości Ø (Infinite distance to Ø singularity)
# Odległość do warstwy Ø jest nieskończona dla każdej innej warstwy.
# Distance to layer Ø is infinite for any other layer.

# Dowód 3: Kompletność metryki poznawczej (Completeness of cognitive metric)
# Metryka została uzupełniona o wszystkie możliwe kombinacje par warstw.
# Metric has been completed with all possible layer pairs combinations.

# Dynamiczna implementacja metryki poznawczej jako sumy odległości pośrednich
# Dynamic implementation of cognitive metric as sum of intermediate distances

def cognitive_metric_dynamic(layer1, layer2):
    infinite = float('inf')
    path_order = [CognitiveLayer.P0, CognitiveLayer.R, CognitiveLayer.I, CognitiveLayer.A, CognitiveLayer.Ø]
    
    if layer1 == layer2:
        return 0
    
    if CognitiveLayer.Ø in (layer1, layer2):
        return infinite

    try:
        idx1, idx2 = path_order.index(layer1), path_order.index(layer2)
        if idx1 > idx2:
            idx1, idx2 = idx2, idx1

        distances = [1, 2, 3, infinite]  # odległości między sąsiednimi warstwami (adjacent layers distances)
        return sum(distances[idx1:idx2])
    except ValueError:
        return infinite

# Funkcja osadzania (Embedding function definition)
def embedding_function(layer):
    embeddings = {
        CognitiveLayer.P0: np.array([0, 0, 0]),
        CognitiveLayer.R: np.array([1, 0, 0]),
        CognitiveLayer.I: np.array([1, 1, 0]),
        CognitiveLayer.A: np.array([1, 1, 1]),
        CognitiveLayer.Ø: np.array([np.nan, np.nan, np.inf]),
    }
    return embeddings[layer]

# Definicja zbioru singularnego Ø (Singular set Ø definition)
class SingularSetØ:
    center = np.array([np.nan, np.nan, np.inf])
    description = (
        "Granica geometryczna systemu, metrycznie nieosiągalna, lokalizująca źródło deformacji poznawczej."
        "Geometric boundary of the system, metrically unattainable, locating the source of cognitive deformation."
    )

# Przykład użycia (Example usage)
if __name__ == "__main__":
    print("Complete Distance R ↔ A:", cognitive_metric_complete(CognitiveLayer.R, CognitiveLayer.A))
    print("Dynamic Distance P₀ ↔ A:", cognitive_metric_dynamic(CognitiveLayer.P0, CognitiveLayer.A))
    print("Embedding A:", embedding_function(CognitiveLayer.A))
    print("Singular Set Ø description:", SingularSetØ.description)
