# GTMØ Formalization of Consciousness and Identity with Axioms and Algorithms (Formalizacja GTMØ: Świadomość i Tożsamość z Aksjomatami i Algorytmami)

import numpy as np
import matplotlib.pyplot as plt
import unittest

# Ontological Categories Definition (Definicja kategorii ontologicznych)
def OntoCat():
    return {'0': 'niebyt', '1': 'byt', '∞': 'nieskończoność', 'Ø': 'niedefiniowalność'}

# Axiom 1: Ontological Indefiniteness (Aksjomat 1: Ontologiczna Niedefiniowalność)
def axiom_ontological_indefiniteness(category):
    return category not in ['0', '1', '∞']

# Axiom 3: Epistemic Singularity (Aksjomat 3: Epistemiczna Osobliwość)
def axiom_epistemic_singularity(system):
    return 'Ø' not in system

# Axiom 6: Heuristic Extremum (Aksjomat 6: Ekstremum Heurystyczne)
def axiom_heuristic_extremum(entropy_values):
    return min(entropy_values.values()) == entropy_values['Ø']

# Axiom 7: Meta-closure (Aksjomat 7: Meta-zamknięcie)
def meta_closure(system_states):
    return 'Ø' in system_states and system_states.get('self_evaluation', False)

# Consciousness framework
def consciousness_framework(agent, system):
    if axiom_ontological_indefiniteness('Ø') and axiom_epistemic_singularity(system):
        return {'agent': agent, 'state': 'Ø'}
    return None

# Identity transition operator (Ø → 1)
def identity_transition(phi, t_c, threshold):
    return 1 if phi(t_c) >= threshold else 'Ø'

# Cognitive trajectory φ(t)
def phi(t):
    return 1 / (1 + np.exp(- (t - 5)))

# Cognitive speed φ'(t)
def phi_prime(t, dt=0.01):
    return (phi(t + dt) - phi(t - dt)) / (2 * dt)

# Cognitive acceleration φ''(t)
def phi_double_prime(t, dt=0.01):
    return (phi_prime(t + dt) - phi_prime(t - dt)) / (2 * dt)

# Cognitive threshold
def cognitive_threshold(phi_value, threshold=0.8):
    return phi_value >= threshold

# Cognitive entropy
def cognitive_entropy(x):
    if x == 'Ø':
        return 0
    return -np.sum([p * np.log2(p) for p in np.array([0.6, 0.25, 0.15]) if p > 0])

# Simulation algorithm
def cognitive_simulation(time_range, threshold=0.8):
    results = []
    for t in time_range:
        state = identity_transition(phi, t, threshold)
        entropy = cognitive_entropy(state)
        results.append((t, phi(t), phi_prime(t), phi_double_prime(t), state, entropy))
    return results

# Visualization algorithm
def plot_cognitive_trajectory(t_values, threshold=0.8):
    plt.figure(figsize=(12, 8))
    plt.plot(t_values, phi(t_values), label='φ(t) – trajektoria poznawcza', linewidth=2)
    plt.plot(t_values, phi_prime(t_values), label="φ'(t) – prędkość poznawcza", linestyle='--')
    plt.plot(t_values, phi_double_prime(t_values), label="φ''(t) – przyspieszenie poznawcze", linestyle=':')
    plt.axhline(y=threshold, color='r', linestyle='-', label=f'φ_threshold (próg) = {threshold}')
    plt.xlabel('Czas (t)')
    plt.ylabel('φ(t)')
    plt.legend()
    plt.title('Analiza trajektorii poznawczej φ(t) w GTMØ')
    plt.grid(True)
    plt.show()

# Testy jednostkowe
class TestGTMØ(unittest.TestCase):

    def test_axioms(self):
        self.assertTrue(axiom_ontological_indefiniteness('Ø'))
        self.assertTrue(axiom_epistemic_singularity(['0', '1', '∞']))
        entropy_values = {'Ø': 0, '1': 1.5}
        self.assertTrue(axiom_heuristic_extremum(entropy_values))
        self.assertTrue(meta_closure({'Ø': True, 'self_evaluation': True}))

    def test_consciousness_framework(self):
        system = ['0', '1', '∞']
        result = consciousness_framework('agent_alpha', system)
        self.assertEqual(result, {'agent': 'agent_alpha', 'state': 'Ø'})

    def test_identity_transition(self):
        t_dynamic = 5  # dynamiczny punkt obserwacji
        threshold_dynamic = phi(t_dynamic) - 0.1
        self.assertEqual(identity_transition(phi, t_dynamic, threshold_dynamic), 1)
        self.assertEqual(identity_transition(phi, t_dynamic, threshold_dynamic + 0.2), 'Ø')

    def test_phi_functions(self):
        self.assertAlmostEqual(phi(5), 0.5, places=2)
        self.assertAlmostEqual(phi_prime(5), 0.25, places=2)
        self.assertAlmostEqual(phi_double_prime(5), 0, places=2)

    def test_cognitive_threshold(self):
        self.assertTrue(cognitive_threshold(0.9))
        self.assertFalse(cognitive_threshold(0.7))

    def test_cognitive_entropy(self):
        self.assertEqual(cognitive_entropy('Ø'), 0)
        self.assertGreater(cognitive_entropy('1'), 0)

if __name__ == '__main__':
    unittest.main()
