import numpy as np
import random
import matplotlib.pyplot as plt

def create_unique_list(num_elements):
    # Überprüfen, ob die Anzahl der gewünschten Elemente nicht größer ist als der Bereich der möglichen Zahlen
    if num_elements > 10000:
        return "Die Anzahl der Elemente kann nicht größer als 10.000 sein, da keine Duplikate erlaubt sind."
    
    # Generiere eine Liste von eindeutigen zufälligen Zahlen von 1 bis 10000
    result_list = random.sample(range(1, 10001), num_elements)
    return result_list

def quick_sort(arr):
    counter = 0  # Schrittzähler initialisieren
    if len(arr) <= 1:
        return arr, 0  # Keine Schritte nötig, wenn Array 0 oder 1 Element hat
    else:
        pivot = arr[0]
        less = []
        greater = []
        for x in arr[1:]:
            counter += 1  # Jeder Vergleich zählt als ein Schritt
            if x <= pivot:
                less.append(x)
            else:
                greater.append(x)

        sorted_less, less_counter = quick_sort(less)
        sorted_greater, greater_counter = quick_sort(greater)

        # Summiere alle Schritte
        counter += less_counter + greater_counter
        return sorted_less + [pivot] + sorted_greater, counter


def merge_sort(arr):
    counter = 0
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        L, left_count = merge_sort(L)
        R, right_count = merge_sort(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            counter += 1  # Jeder Vergleich zählt als ein Schritt
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
            counter += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
            counter += 1

        counter += left_count + right_count
        return arr, counter
    return arr, counter


if __name__ == "__main__":
    
    list_sizes = [10, 100, 1000, 10000]
    quick_steps = []
    merge_steps = []
    sizes = []
    
    for size in list_sizes:
        for i in range(0,100): # jeweils 10 zufällige Listen pro Elementanzahl
            random_list = create_unique_list(size)
            _, quick_step_count = quick_sort(random_list.copy())
            _, merge_step_count = merge_sort(random_list.copy())
            
            quick_steps.append(quick_step_count)
            merge_steps.append(merge_step_count)
            sizes.append(size)
        
    
    # Werte für die Darstellung der Komplexitätskurven
    n_values = np.linspace(10, 10000, num=9000)
    n_log_n = n_values * np.log2(n_values)  # O(n log n) Komplexität
    n_squared = n_values**2  # O(n^2) Komplexität


    # Erstellen des Plots
    plt.rcParams.update({'font.family':'Comic Sans MS'})
    plt.rcParams.update({'font.size':'16'})
    plt.figure(figsize=(16, 9))
    plt.scatter(sizes, quick_steps, alpha=1, label='Quick Sort')
    plt.scatter(sizes, merge_steps, alpha=1, label='Merge Sort')
    plt.plot(n_values, n_log_n, '--', color = '#FF7F0E', alpha=0.5, label='O(n log n) Zeitkomplexität Merge Sort')
    plt.plot(n_values, n_squared, '--', color = '#1F77B4', alpha=0.5, label='O(n^2) Zeitkomplexität Quick Sort')
    plt.xscale('log')
    plt.yscale('log')
    plt.xlabel('Anzahl der Listenelemente')
    plt.ylabel('Anzahl der Vergleichsschritt')
    plt.title('Vergleich der Vergleichsschritt zwischen Quick Sort und Merge Sort')
    plt.legend()
    plt.grid(True)
    plt.show()



