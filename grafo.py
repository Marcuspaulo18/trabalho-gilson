import csv


class Grafo():
    def __init__(self):
        self.vertices = []
        self.file = ''
        self.adjacentes = []
        self.visivertices = []
        self.arestas = []
        self.visiarestas = []
        self.subrede = []
        self.cicloseulers = []

    def captura_vertice(self):
        return self.vertices

    def captura_adjacentes(self):
        return self.adjacentes

    def captura_arestas(self):
        return self.arestas

    def captura_cicloeuleriano(self):
        return self.cicloseulers

    def captura_subvisi(self):
        return self.subrede

    def captura_arquivos(self):
        return self.file

    def adiciona_vertices(self, val):
        self.vertices.append(val)
        self.adjacentes.append([])

    def adiciona_arestas(self, val1, val2):
        # Corrigido: não força ordem específica das arestas
        self.arestas.append([val1, val2])
        self.visiarestas.append(0)

    def cria_lista_vertice(self):
        for aresta in self.arestas:
            v1 = self.vertices.index(aresta[0])
            v2 = self.vertices.index(aresta[1])
            self.adjacentes[v1].append(aresta[1])
            self.adjacentes[v2].append(aresta[0])

    def image_file(self, file):
        self.file = file
        line = 0
        with open(file, newline='') as inputfile:
            for row in csv.reader(inputfile):
                line += 1
                if (line == 1):
                    for i in row:
                        self.adiciona_vertices(int(i))
                    self.visivertices = [0] * len(self.vertices)
                else:
                    self.adiciona_arestas(int(row[0]), int(row[1]))
        self.cria_lista_vertice()

    def bfs_conectividade(self, index):
        self.visivertices[index] = 1
        for adj in self.adjacentes[index]:
            position = self.vertices.index(adj)
            if (self.visivertices[position] == 0):
                self.bfs_conectividade(position)

    def esta_conectado(self):
        # Reset visited vertices before checking connectivity
        self.visivertices = [0] * len(self.vertices)
        self.bfs_conectividade(0)
        return (self.visivertices.count(0) == 0)

    def pareador(self):
        # Corrigido: verifica todos os vértices antes de retornar True
        for i in self.adjacentes:
            if (len(i) % 2 != 0):
                return False
        return True

    def acha_aresta(self, val1, val2):
        # Corrigido: busca nas duas direções possíveis
        for i, aresta in enumerate(self.arestas):
            if (aresta[0] == val1 and aresta[1] == val2) or (aresta[0] == val2 and aresta[1] == val1):
                return i
        return -1

    def aresta_visitada(self, val1, val2, mark=False):
        position = self.acha_aresta(val1, val2)
        if position == -1:
            return True  # Se não encontrou a aresta, considera como visitada
        visitado = self.visiarestas[position] == 1
        if mark:
            self.visiarestas[position] = 1
        return visitado

    def proximo_vertice(self, index):
        # Corrigido: garante que encontre o próximo vértice válido
        val1 = self.vertices[index]
        for val2 in self.adjacentes[index]:
            if not self.aresta_visitada(val1, val2, True):
                return self.vertices.index(val2)
        return -1

    def proximo_vertice_nao_visitado(self, find):
        # Corrigido: retorna o índice do vértice de origem que tem arestas não visitadas
        for i in find:
            position = self.vertices.index(i)
            for j in self.adjacentes[position]:
                if not self.aresta_visitada(i, j):
                    return position  # Retorna o índice do vértice de origem
        return -1

    def ciclo_euleriano(self, index=0):
        # Reset das estruturas de controle
        self.visiarestas = [0] * len(self.arestas)
        self.cicloseulers = []
        self.subrede = []

        rede = []
        subrede = []

        rede.append(self.vertices[index])
        self.cicloseulers.append(self.vertices[index])

        while True:
            # Corrigido: busca corretamente o próximo vértice com arestas não visitadas
            valatual = self.proximo_vertice_nao_visitado(rede)

            if valatual < 0:
                break

            valinicio = valatual
            subrede.append(self.vertices[valatual])

            while True:
                val = self.proximo_vertice(valatual)
                if val < 0:
                    break

                subrede.append(self.vertices[val])
                valatual = val

                if valinicio == valatual:
                    break

            # Corrigido: melhora a lógica de inserção do subciclo
            if subrede and subrede[0] in self.cicloseulers:
                position = self.cicloseulers.index(subrede[0])
                self.cicloseulers.pop(position)

                for item in subrede:
                    rede.append(item)
                    self.cicloseulers.insert(position, item)
                    position += 1

                self.subrede.append(subrede.copy())  # Corrigido: cria cópia da lista
                subrede = []
