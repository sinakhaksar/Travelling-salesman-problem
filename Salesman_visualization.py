import networkx as nx
import matplotlib.pyplot as plt

def traveling_salesman(graph, start_node):
    unvisited_nodes = set(graph.keys())
    unvisited_nodes.remove(start_node)

    current_node = start_node
    path = [current_node]
    total_weight = 0

    while unvisited_nodes:
        nearest_neighbor = min(unvisited_nodes, key=lambda node: graph[current_node][node]['weight'])
        total_weight += graph[current_node][nearest_neighbor]['weight']
        current_node = nearest_neighbor
        path.append(current_node)
        unvisited_nodes.remove(current_node)

    # Return to the starting node to complete the cycle
    total_weight += graph[current_node][start_node]['weight']
    path.append(start_node)

    return path, total_weight

def plot_graph(graph, path):
    G = nx.Graph()
    
    for node in graph:
        for neighbor, attr in graph[node].items():
            G.add_edge(node, neighbor, weight=attr['weight'])
    
    pos = nx.circular_layout(G)  # You can choose a different layout if needed

    nx.draw_networkx_nodes(G, pos, node_size=700)
    nx.draw_networkx_labels(G, pos, font_size=12)

    for edge in G.edges():
        nx.draw_networkx_edges(G, pos, edgelist=[edge], width=2, alpha=0.5)

    # Draw the optimal path with arrows and edge weights
    edge_labels = {(node1, node2): graph[node1][node2]['weight'] for node1, node2 in G.edges()}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')
    
    for i in range(len(path) - 1):
        edge = (path[i], path[i + 1])
        nx.draw_networkx_edges(G, pos, edgelist=[edge], width=2, edge_color='red', arrows=True, connectionstyle='arc3,rad=0.1', arrowstyle='->')

    plt.show()

def display_result(path, weight):
    print("Optimal Path:", " -> ".join(path))
    print("Total Weight:", weight)

def main():
    graph = {
        'A': {'B': {'weight': 14}, 'C': {'weight': 12}, 'D': {'weight': 7}, 'E': {'weight': 15}},
        'B': {'A': {'weight': 14}, 'C': {'weight': 9}, 'E': {'weight': 5}, 'D': {'weight': 13}},
        'C': {'A': {'weight': 12}, 'B': {'weight': 9}, 'D': {'weight': 6}, 'E': {'weight': 8}},
        'D': {'A': {'weight': 7}, 'B': {'weight': 13}, 'C': {'weight': 6}, 'E': {'weight': 11}},
        'E': {'A': {'weight': 15}, 'C': {'weight': 8}, 'B': {'weight': 5}, 'D': {'weight': 11}},
    }

    print("Choose from A B C D E")
    start_node = input("Enter the starting node: ").upper()

    if start_node not in graph:
        print("Invalid starting node.")
    else:
        optimal_path, total_weight = traveling_salesman(graph, start_node)
        display_result(optimal_path, total_weight)
        plot_graph(graph, optimal_path)

if __name__ == "__main__":
    main()
