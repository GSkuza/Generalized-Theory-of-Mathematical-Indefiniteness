# Topologia Ø w GTMØ / Topology of Ø in GTMØ

"""
📘 Aksjomaty, definicje i diagramy GTMØ dla topologii Ø:

Wizualizacja wyników zawartych w kodzie znajduje się tutaj:

![φ(t) i Heatmapa E(x)](φ_t_E_heatmap_summary.png)

🔹 Aksjomat AX8_v2 (Izolacja graniczna Ø):
¬∃Seq(xₙ) ⊆ Domain(GTMØ): lim(xₙ) = Ø
– Żaden klasyczny ciąg nie zbiega do Ø. Ø nie posiada klasycznej granicy.

🔹 Aksjomat AXØ_iso (Translogiczna izolacja):
∀x ∈ D_classical: ¬∃f(x) = Ø
– Ø nie może być obrazem żadnej funkcji klasycznej.

🔹 Definicja E(x):
Heurystyka epistemiczna E(x) mierzy odległość poznawczą od Ø:
E(x) = 1 − exp(−|x − Ø|)

🔹 Definicja φ(t):
Trajektoria poznawcza φ(t) odwzorowuje stan bytu:
φ(t) ∈ {0 (niebyt), 1 (byt), ∞ (nieskończoność), Ø (niedefinitywność)}

🔹 Definicja φ′(t):
Poznawcze przyspieszenie – zmiana trajektorii φ(t) względem t:
φ′(t) = dφ/dt ≈ [φ(t+Δt) − φ(t)] / Δt

🔹 Definicja Ψᴷ(x):
Klasyfikator cząstek wiedzy na podstawie heurystyki E(x):
Ψᴷ = Ø ⇔ E(x) < δ

🔹 Termin: Punkt emergencji Ø
Punkt φ(t), dla którego E(x) < δ i który pojawia się dynamicznie na trajektorii poznania.

🔹 Termin: Heatmapa Ø
Wizualizacja natężenia E(x) w czasie φ(t), ukazująca obszary emergencji i niedefinitywności.

🔹 Termin: Osobliwość Ø
Skrajny przypadek emergencji, gdzie system poznawczy wchodzi w interakcję z Ø bez możliwości klasycznej klasyfikacji.
"""

from math import exp, sin, pi, isclose
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Slider
from matplotlib.animation import FuncAnimation
import unittest
import os

# φ(t), E(x), φ′(t), Ψᴷ – wszystkie funkcje dostępne w module
# Inne funkcje zostały uprzednio zdefiniowane

def display_all_outputs():
    print("Wizualizacje i analizy GTMØ uruchomione...")
    visualize_phi_trajectory()
    nonlinear_emergence_mapping()
    visualize_heatmap_Ø()
    print("Osobliwości Ø wykryte na trajektorii φ(t):", detect_singularities())
    interactive_phi_analysis()
    real_time_analysis()

# Testy złożone (jak wcześniej)
class TestComplexTopologyØ(unittest.TestCase):
    def test_phi_continuity_classes(self):
        self.assertEqual(phi(0.24), 0)
        self.assertEqual(phi(0.25), 1)
        self.assertEqual(phi(0.49), 1)
        self.assertEqual(phi(0.5), float('inf'))
        self.assertEqual(phi(0.74), float('inf'))
        self.assertEqual(phi(0.75), 999)

    def test_phi_prime_discontinuity(self):
        self.assertTrue(abs(phi_prime(0.24)) > 10 or is_nan(phi_prime(0.24)))
        self.assertTrue(abs(phi_prime(0.49)) > 10 or is_nan(phi_prime(0.49)))
        self.assertTrue(abs(phi_prime(0.74)) > 10 or is_nan(phi_prime(0.74)))

    def test_emergence_mapping_range(self):
        ts = np.linspace(0, 1, 50)
        values = [E(phi(t) + sin(10 * pi * t) * 0.1, 999) for t in ts]
        for val in values:
            self.assertTrue(0 <= val <= 1)

    def test_detect_singularities_density(self):
        ts = np.linspace(0.75, 1.0, 100)
        singular = detect_singularities(ts, delta=0.1)
        self.assertTrue(len(singular) > 10)

    def test_phi_and_E_sync(self):
        ts = [0.9, 0.95, 1.0]
        for t in ts:
            x = phi(t)
            self.assertLess(E(x), 0.1)

if __name__ == "__main__":
    unittest.main(argv=[''], exit=False)
    display_all_outputs()
