# Topologia Ø w GTMØ / Topology of Ø in GTMØ

"""
Polska wersja:
Topologia Ø jako składnik metapoznawczy teorii GTMØ

Założenia:
1. Ø nie jest punktem granicznym żadnej sekwencji klasycznej:
   AX8_v2: ¬∃Seq(xₙ) ⊆ Domain(GTMØ): lim(xₙ) = Ø

2. Ø-punkty są izolowane translogicznie i epistemicznie.
3. Nie istnieje klasyczna ciągłość przejścia do Ø.
4. Otoczenia Ø definiowane są poprzez heurystykę E(x).
5. Ø stanowi przestrzeń emergencji – źródło nowych cząstek Ψᴷ.
6. Trajektoria φ(t) odwzorowuje przejścia poznawcze przez punkty Ø.
7. Klasyfikator Ψᴷ wykorzystuje odległość topologiczną od Ø.

English version:
Topology of Ø as a metacognitive component of GTMØ

Assumptions:
1. Ø is not a classical limit point of any sequence:
   AX8_v2: ¬∃Seq(xₙ) ⊆ Domain(GTMØ): lim(xₙ) = Ø

2. Ø-points are translogically and epistemically isolated.
3. Classical continuity does not apply to Ø transitions.
4. Ø neighborhoods are defined via the E(x) heuristic.
5. Ø is an emergence space — source of new Ψᴷ particles.
6. The φ(t) trajectory maps cognitive transitions through Ø.
7. The Ψᴷ classifier uses topological distance from Ø.
"""

from math import exp, sin, pi
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Slider

# Heurystyka epistemiczna E(x) – Epistemic Heuristic E(x)
def E(x, Ø_value=999):
    return exp(-abs(x - Ø_value))

# Funkcja trajektorii φ(t) – Cognitive trajectory function φ(t)
def phi(t, domain=[0, 1, float('inf'), 999]):
    if t < 0.25:
        return domain[0]  # 0
    elif t < 0.5:
        return domain[1]  # 1
    elif t < 0.75:
        return domain[2]  # ∞
    else:
        return domain[3]  # Ø

# Klasyfikator Ψᴷ oparty o odległość od Ø – Ψᴷ classifier based on E(x)
def classify_PsiK(x, Ø_value=999, delta=0.05):
    distance = E(x, Ø_value)
    if distance < delta:
        return "Ψᴷ = Ø (niedefinitywność)"
    else:
        return "Ψᴷ = klasyczne (0/1/∞)"

# Przykład detekcji emergencji
for t in [0.1, 0.4, 0.6, 0.9]:
    x = phi(t)
    print(f"t = {t}, φ(t) = {x}, klasyfikacja Ψᴷ: {classify_PsiK(x)}")

# Funkcja adaptatywnej wizualizacji trajektorii φ(t)
def visualize_phi_trajectory():
    ts = np.linspace(0, 1, 100)
    ys = [phi(t) for t in ts]
    colors = ['blue' if y == 0 else 'green' if y == 1 else 'orange' if y == float('inf') else 'red' for y in ys]
    plt.figure(figsize=(10, 2))
    plt.scatter(ts, ys, c=colors, label='φ(t)', alpha=0.7)
    plt.xlabel('t')
    plt.ylabel('φ(t)')
    plt.title('Adaptatywna wizualizacja trajektorii φ(t)')
    plt.grid(True)
    plt.show()

# Funkcja nieliniowego mapowania punktów emergencji

def nonlinear_emergence_mapping(n=100, Ø_value=999):
    ts = np.linspace(0, 1, n)
    emergence_points = []
    for t in ts:
        x = phi(t)
        noise = sin(10 * pi * t) * 0.1
        emergent = E(x + noise, Ø_value)
        emergence_points.append(emergent)
    plt.figure(figsize=(10, 2))
    plt.plot(ts, emergence_points, color='purple', label='Emergencja')
    plt.xlabel('t')
    plt.ylabel('Heurystyka E(x + noise)')
    plt.title('Nieliniowa mapa emergencji')
    plt.legend()
    plt.grid(True)
    plt.show()

# Detektor osobliwości Ø oparty o trajektorię φ(t)
def detect_singularities(ts=np.linspace(0, 1, 100), Ø_value=999, delta=0.05):
    singularities = []
    for t in ts:
        x = phi(t)
        if E(x, Ø_value) < delta:
            singularities.append((t, x))
    return singularities

# Interaktywna analiza trajektorii poznawczej φ(t)
def interactive_phi_analysis():
    fig, ax = plt.subplots()
    plt.subplots_adjust(bottom=0.25)
    t_init = 0.0
    x_init = phi(t_init)
    line, = plt.plot([t_init], [x_init], 'ro', label='φ(t)')
    ax.set_xlim(0, 1)
    ax.set_ylim(-10, 1000)
    ax.set_xlabel('t')
    ax.set_ylabel('φ(t)')
    ax.set_title('Interaktywna analiza trajektorii φ(t)')
    ax.grid(True)

    ax_slider = plt.axes([0.2, 0.1, 0.65, 0.03])
    t_slider = Slider(ax_slider, 't', 0.0, 1.0, valinit=t_init)

    def update(val):
        t = t_slider.val
        x = phi(t)
        line.set_data([t], [x])
        fig.canvas.draw_idle()

    t_slider.on_changed(update)
    plt.legend()
    plt.show()

# Wywołania wizualizacji i analizy
visualize_phi_trajectory()
nonlinear_emergence_mapping()
print("Osobliwości Ø wykryte na trajektorii φ(t):", detect_singularities())
interactive_phi_analysis()
