from grafo import Grafo
from visualizador import visualizador

G = Grafo()
G.image_file('./dados/grafo_exemplo')
esta_conectado = G.esta_conectado()
pareador = G.pareador()
if (esta_conectado and pareador):
    G.ciclo_euleriano(0)

print("\n---------------------------------------------------")
print("Grafo conexo? %r" % esta_conectado)
print("Cada vertice tem número par de arestas? %r" % pareador)
print("Vértices %r" % G.captura_vertice())
print("Adjacentes %r" % G.captura_adjacentes())
print("Arestas %r" % G.captura_arestas())
if (esta_conectado and pareador):
    print("Ciclo Euleriano: %r" % G.captura_cicloeuleriano())
    print("Ciclo Euleriano (subciclos): %r" % G.captura_subvisi())
else:
    print("Grafo não possui ciclo Euleriano.")
print("---------------------------------------------------\n",)

visualizador(G)