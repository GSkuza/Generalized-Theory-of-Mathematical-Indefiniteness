import math
import unittest

# Autor: Grzegorz Skuza (Poland)

# Definicja kategorii ontologicznych (Definition of Ontological Categories)
def OntoCat():
    return {'0': 'niebyt', '1': 'byt', '∞': 'nieskończoność', 'Ø': 'niedefinitywność', 'N': 'niedefiniowalność'}

# Aksjomat 1: Ontologiczna Niedefinitywność (Axiom 1: Ontological Indefiniteness)
def axiom_ontological_indefiniteness(category):
    return category not in ['0', '1', '∞', 'N']

# Aksjomat 2: Niedefiniowalność (Axiom 2: Non-definability)
def axiom_non_definability(category):
    return category == 'N'

# Aksjomat 3: Epistemiczna Osobliwość (Axiom 3: Epistemic Singularity)
def axiom_epistemic_singularity(system_knowledge):
    for knowledge_fragment in system_knowledge:
        if isinstance(knowledge_fragment, dict) and 'Ø' in knowledge_fragment.get('concepts', []):
            return False
    return True

# Aksjomat 6: Ekstremum Heurystyczne (Axiom 6: Heuristic Extremum)
def axiom_heuristic_extremum(entropy_values):
    return min(entropy_values.values()) == entropy_values['Ø']

# Aksjomat 7: Meta-zamknięcie (Axiom 7: Meta-closure)
def meta_closure(system_states):
    return system_states.get('Ø', False) and system_states.get('self_evaluation', False)

# Ramy świadomości (Consciousness framework)
def consciousness_framework(agent, system_knowledge):
    if axiom_ontological_indefiniteness('Ø') and axiom_epistemic_singularity(system_knowledge):
        return {'agent': agent, 'state': 'Ø'}
    return None

# Operator przejścia tożsamości (Ø → 1) (Identity transition operator (Ø → 1))
def identity_transition(phi, t_c, threshold):
    return 1 if phi(t_c) >= threshold else 'Ø'

# Trajektoria poznawcza φ(t) (Cognitive trajectory φ(t))
def phi(t):
    return 1 / (1 + math.exp(- (t - 5)))

# Prędkość poznawcza φ'(t) (Cognitive speed φ'(t))
def phi_prime(t, dt=0.01):
    return (phi(t + dt) - phi(t - dt)) / (2 * dt)

# Przyspieszenie poznawcze φ''(t) (Cognitive acceleration φ''(t))
def phi_double_prime(t, dt=0.01):
    return (phi_prime(t + dt) - phi_prime(t - dt)) / (2 * dt)

# Próg poznawczy (Cognitive threshold)
def cognitive_threshold(phi_value, threshold=0.8):
    return phi_value >= threshold

# Entropia poznawcza (Cognitive entropy)
def cognitive_entropy(x):
    if x == 'Ø':
        return 0
    parts = [0.6, 0.25, 0.15]
    return -sum([p * math.log2(p) for p in parts if p > 0])

# Adaptacyjna aktualizacja progów poznawczych (Adaptive cognitive threshold update)
def adaptive_threshold_update(scores, current_threshold):
    mean_score = sum(scores) / len(scores)
    adjusted_threshold = current_threshold + (mean_score - current_threshold) * 0.1
    return max(0.0, min(adjusted_threshold, 1.0))

# Analiza stabilności poznawczej (Cognitive stability analysis)
def cognitive_stability_analysis(phi_values):
    mean_phi = sum(phi_values) / len(phi_values)
    variance = sum((x - mean_phi) ** 2 for x in phi_values) / len(phi_values)
    stability_score = 1 / (1 + variance)
    return stability_score

# Unit tests
class TestGTMO(unittest.TestCase):

    def test_axiom_epistemic_singularity(self):
        system_with_Ø = [{'concepts': ['0', '1', 'Ø']}]
        system_without_Ø = [{'concepts': ['0', '1', '∞']}]
        self.assertFalse(axiom_epistemic_singularity(system_with_Ø))
        self.assertTrue(axiom_epistemic_singularity(system_without_Ø))

    def test_consciousness_framework(self):
        system = [{'concepts': ['0', '1', '∞']}]
        result = consciousness_framework('agent_alpha', system)
        self.assertEqual(result, {'agent': 'agent_alpha', 'state': 'Ø'})

    def test_meta_closure(self):
        self.assertTrue(meta_closure({'Ø': True, 'self_evaluation': True}))
        self.assertFalse(meta_closure({'Ø': False, 'self_evaluation': True}))

# Explicitly load and run tests to ensure execution in all environments
def run_tests():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestGTMO)
    unittest.TextTestRunner(verbosity=2).run(suite)

run_tests()
