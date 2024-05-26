import networkx as nx
import random
import matplotlib.pyplot as plt

    
# Funktion zum Zeichnen des Graphen
def draw_graph(G, pos, title, visited_edges):
    # Definition des Schriftstils für die Beschriftungen
    font = {'family': 'Comic Sans MS',
            'color':  'black',
            'weight': 'normal',
            'size': 16,
           }
    
    # Erstellung der Plotfigur mit festgelegter Größe
    plt.figure(figsize=(9, 12))
    
    # Zeichne alle Kanten des Graphen (unbesucht) in Schwarz mit gestrichelten Linien
    nx.draw_networkx_edges(G, pos, edge_color='black', width=4, style='dotted')
    
    # Zeichne die besuchten Kanten in Rot
    nx.draw_networkx_edges(G, pos, edgelist=visited_edges, edge_color='red', width=4)
    
    # Zeichne alle Knoten im Graphen
    nx.draw_networkx_nodes(G, pos, node_size=2400, node_color='white', edgecolors='black',linewidths= 4)
    
    # Beschrifte die Knoten
    nx.draw_networkx_labels(G, pos, font_size=24, font_family = 'Comic Sans MS', font_color='black')
    
    # Setze den Titel des Plots
    plt.title(title)
    
    #edge_labels = nx.get_edge_attributes(G, "weight")
    #nx.draw_networkx_edge_labels(G, pos, edge_labels, font_size=24, font_family = 'Comic Sans MS')
    
    # Deaktiviere die Achsenbeschriftungen
    plt.axis('off')
    
    # Zeige den Graphen
    plt.show()
    
def path_to_edges(path):
    edges = []
    for i in range(len(path) - 1):
        # Sortiere die Knoten in aufsteigender Reihenfolge
        edge = tuple(sorted([path[i], path[i+1]]))
        edges.append(edge)
    return edges

# Funktion zum Finden des Eulerpfads
def find_eulerian_path(G, pos):
    # Finde Knoten mit ungeradem Grad (odd_degree_nodes)
    odd_degree_nodes = [v for v, d in G.degree() if d % 2 == 1]
    
    # Überprüfe, ob die Anzahl der Knoten mit ungeradem Grad entweder 0 oder 2 ist
    if len(odd_degree_nodes) not in [0, 2]:
        return None
    
    # Wähle einen Startknoten (falls vorhanden)
    start_node = odd_degree_nodes[0] if odd_degree_nodes else list(G.nodes())[0]

    path = []  # Initialisierung des Pfads
    stack = [start_node]  # Initialisierung des Stacks mit dem Startknoten
    visited_edges = []  # Initialisierung der Liste besuchter Kanten
    
    # Verwendung eines Dictionarys, um besuchte Kanten zu markieren und ihre Anzahl zu zählen
    edge_count = {}
    for node in G.nodes():
        edge_count[node] = {neighbor: G.number_of_edges(node, neighbor) for neighbor in G[node]}

    # Hauptalgorithmus-Schleife
    while stack:
        u = stack[-1]  # Aktueller Knoten im Stack
        if all(value == 0 for value in edge_count[u].values()):  # Wenn alle Kanten von u besucht wurden
            path.append(u)  # Füge u zum Pfad hinzu
            stack.pop()  # Entferne u aus dem Stack
        else:
            # Durchlaufe die Nachbarknoten von u
            for v in G[u]:
                if edge_count[u][v] > 0:  # Wenn die Kante (u, v) noch nicht besucht wurde
                    stack.append(v)  # Füge v zum Stack hinzu
                    edge_count[u][v] -= 1  # Reduziere die Anzahl der unbesuchten Kanten zwischen u und v
                    edge_count[v][u] -= 1  # Da der Graph ungerichtet ist, reduziere auch die Anzahl für (v, u)
                    visited_edges.append((u, v))  # Markiere die Kante (u, v) als besucht
                    # Zeichne den aktuellen Schritt
                    draw_graph(G, pos, f'Schritt: Besuch von Kante {u, v}', visited_edges)
                    break  # Beende die Schleife, um nur eine Kante zu besuchen

    return path  # Rückgabe des Eulerpfads

if __name__ == "__main__":
    # Hauptteil des Programms
    G = nx.Graph()  # Erstellen eines leeren Graphen
    # Hinzufügen von Kanten zum Graphen
    edges = [('1', '2'), ('2', '3'), ('3', '4'), ('4', '5'), ('5', '1'), ('3', '5'), ('2', '5'), ('1', '3')]
    G.add_edges_from(edges)
    
    G.edges['1','2']['weight'] = 2
    G.edges['2','3']['weight'] = 12
    G.edges['3','4']['weight'] = 2 
    G.edges['4','5']['weight'] = 5
    G.edges['5','1']['weight'] = 20
    G.edges['3','5']['weight'] = 1
    G.edges['2','5']['weight'] = 7
    G.edges['1','3']['weight'] = 15
    
    # Positionen der Knoten für das Zeichnen des Graphen
    pos = {'1': (2, 0), '2': (0, 0), '3': (0, 2), '4': (1, 4), '5': (2, 2)}
    
    # Eulerpfad
    eulerian_path = find_eulerian_path(G,pos)
    
    # Pfadsuche -  Dijkstra-Algorithmus
    approx_tour = nx.shortest_path(G, source="4", target="1", weight='weight', method='dijkstra')
    
    # Cliquenproblem - Bron-Kerbosch-Algorithmus:
    cliques = max(nx.find_cliques(G), key=len)
    
    # Konvertiere den Pfad in eine Liste von Kanten
    visited_edges = path_to_edges(approx_tour)
    cliques_edges = [('1', '2'), ('2', '3'), ('5', '1'), ('3', '5'), ('2', '5'), ('1', '3')]
    
    
    counter = 0
    edges = []
    draw_graph(G, pos, f"Initial", edges)
    for edge in visited_edges:
        edges.append(edge)
        print(edges)
        draw_graph(G, pos, f"Iteration {counter}", edges)
        counter += 1 
        
    counter = 0
    edges = []
    draw_graph(G, pos, f"Initial", edges)
    for edge in cliques_edges:
        edges.append(edge)
        print(edges)
        draw_graph(G, pos, f"Iteration {counter}", edges)
        counter += 1
    
    
        