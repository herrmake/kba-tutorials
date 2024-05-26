import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.optimize import minimize

# Einstellen des Schriftstils und der Schriftgröße
plt.rcParams.update({'font.family': 'Comic Sans MS', 'font.size': 16})

# Werte für x1 und x2 generieren
x1 = np.linspace(-6, 6, 100)
x2 = np.linspace(-6, 6, 100)
X1, X2 = np.meshgrid(x1, x2)

# Funktion berechnen
F = X1**2 + X2**2

#Zielfunktion
def f(x1,x2):
    return x1**2 + x2**2


# Listen zum Speichern des Fortschritts
iterations = []
values_progress = []
x_progress = []

# Callback-Funktion zur Speicherung der Iterationen und Zielfunktionswerte
def callback(xk):
    iterations.append(len(iterations))  # Anzahl der Iterationen
    values_progress.append(f(xk))  # Aktueller Wert der Zielfunktion (ohne Negierung)
    x_progress.append(xk)

# Startpunkt
x0 = [5, 5]

# Optimierung mit dem Gradientenverfahren (BFGS ist eine Annäherung an das Newton-Verfahren)
res_bfgs = minimize(f, x0, method='BFGS', callback = callback)

# Optimierung mit dem Simplex-Algorithmus (Nelder-Mead)
res_nm = minimize(f, x0, method='Nelder-Mead', callback = callback)

#res_bfgs, res_nm

# Suchweg
x = [i[0] for i in x_progress] 
y = [i[1] for i in x_progress] 

# Plot erstellen
fig = plt.figure(figsize=(12, 9))
ax = fig.add_subplot(111, projection='3d')
surface = ax.plot_surface(X1, X2, F, alpha = 0.5, cmap='viridis')
ax.plot(x,y,values_progress, "bo--", ms=10)

# Titel und Achsenbeschriftungen
#ax.set_title('Plot von $f(x_1, x_2) = x_1^2 + x_2^2$')
ax.set_xlabel('$x_1$')
ax.set_ylabel('$x_2$')
ax.set_zlabel('$f(x_1, x_2)$')

# Farblegende hinzufügen
fig.colorbar(surface, ax=ax, shrink=0.5, aspect=10)

# Plot anzeigen
plt.show()