from enum import Enum
import numpy as np

# Cognitive layers enumeration
class CognitiveLayer(Enum):
    P0 = 'P₀'
    R = 'R'
    I = 'I'
    A = 'A'
    Ø = 'Ø'

# Complete cognitive metric definition with explicit distances
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

    # Symmetric distance lookup
    distance = distances.get((layer1, layer2)) or distances.get((layer2, layer1))
    return distance if distance is not None else infinite

# Dynamic implementation of cognitive metric as cumulative distances
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

        distances = [1, 2, 3, infinite]  # distances between adjacent layers
        return sum(distances[idx1:idx2])
    except ValueError:
        return infinite

# Embedding function definition
def embedding_function(layer):
    embeddings = {
        CognitiveLayer.P0: np.array([0, 0, 0]),
        CognitiveLayer.R: np.array([1, 0, 0]),
        CognitiveLayer.I: np.array([1, 1, 0]),
        CognitiveLayer.A: np.array([1, 1, 1]),
        CognitiveLayer.Ø: np.array([np.nan, np.nan, np.inf]),
    }
    return embeddings[layer]

# Singular set Ø definition
class SingularSetØ:
    center = np.array([np.nan, np.nan, np.inf])
    description = "Geometric boundary of the system, metrically unattainable, locating the source of cognitive deformation."

# Example usage
if __name__ == "__main__":
    print("Complete Distance R ↔ A:", cognitive_metric_complete(CognitiveLayer.R, CognitiveLayer.A))
    print("Dynamic Distance P₀ ↔ A:", cognitive_metric_dynamic(CognitiveLayer.P0, CognitiveLayer.A))
    print("Embedding A:", embedding_function(CognitiveLayer.A))
    print("Singular Set Ø description:", SingularSetØ.description)
