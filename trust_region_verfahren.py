from scipy.optimize import minimize, Bounds, LinearConstraint
import numpy as np
import matplotlib.pyplot as plt

# Definieren der Grenzen für jede Variable
bounds = Bounds([0, 0], [10.0, 10.0])

# Definieren der linearen Nebenbedingungen
# Jede Zeile der Matrix definiert eine lineare Nebenbedingung
linear_constraint = LinearConstraint(
    [[6, 4], [1, 2], [-1, 1], [0, 1]],  # Koeffizienten der Nebenbedingungen
    -np.inf,  # keine unteren Schranken
    np.array([24, 6, 1, 2])  # oberen Schranken
)

# Zielfunktion, die minimiert werden soll (Maximierung durch Negierung)
def target_func(x):
    return -1 * (5 * x[0] + 4 * x[1])

# Anfangsvermutung für die Variablen
x0 = [0, 0]

# Listen zum Speichern des Fortschritts
iterations = []
values_progress = []
x_progress = []
# Callback-Funktion zur Speicherung der Iterationen und Zielfunktionswerte
def callback(xk, state):
    iterations.append(len(iterations))  # Anzahl der Iterationen
    values_progress.append(-target_func(xk))  # Aktueller Wert der Zielfunktion (ohne Negierung)
    x_progress.append(xk)
# Lösen des Optimierungsproblems mit der Methode 'trust-constr'
result = minimize(
    target_func,  # Zielfunktion
    x0,  # Anfangsvermutung
    method='trust-constr',  # Optimierungsmethode
    bounds=bounds,  # Variablen-Grenzen
    constraints=[linear_constraint],  # Nebenbedingungen
    callback=callback  # Callback-Funktion
)

# Ergebnisvariablen
selected_items = result.x  # Optimale Werte der Variablen
max_value = -result.fun  # Maximierter Wert der Zielfunktion

# Plotten des Fortschritts der Optimierung
plt.figure(figsize=(10, 5))
plt.plot(iterations, values_progress, 'bo-', label='Maximaler Wert')
plt.xlabel('Iteration')
plt.ylabel('Wert')
plt.title('Fortschritt der Optimierung')
plt.legend()
plt.grid(True)
plt.show()

# Rückgabe der Ergebnisse
selected_items, max_value



