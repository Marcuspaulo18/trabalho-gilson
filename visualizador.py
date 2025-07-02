from matplotlib import pyplot as plt
import networkx as nx

def visualizador(graph):
    G = nx.Graph()
    G.add_nodes_from(graph.captura_vertice())
    G.add_edges_from(graph.captura_arestas())

    nx.draw(G, node_size=800, node_color="blue", with_labels=True)
    plt.savefig('grafo.png')  # Save with fixed filename
    plt.show()