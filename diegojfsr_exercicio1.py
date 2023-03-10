# -*- coding: utf-8 -*-
"""DiegoJfsr-Exercicio1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ORTSyJ9RGf66_REIx1yU-7PmEN5Ch3sQ
"""

### --------------------------------------------------------------------------------------

### Codigo 1

### --------------------------------------------------------------------------------------

import matrixInc

def creatematrix2():
    matrix = []
    matrix.append(["#","#", "#", "#", "#", "#", "#", "#"])
    matrix.append(["#"," ", " ", " ", " ", " ", " ", "#"])
    matrix.append(["#"," ", " ", " ", " ", " ", " ", "#"])
    matrix.append(["#","#", "#", "#", " ", " ", " ", "#"])
    matrix.append(["#"," ", " ", " ", " ", " ", " ", "#"])
    matrix.append(["#"," ", " ", " ", "#", " ", " ", "#"])
    matrix.append(["#"," ", " ", " ", "#", " ", " ", "#"])
    matrix.append(["#","#", "#", "#", "#", "#", "#", "#"])

    return matrix

def printmatrix(matrix, path=""):
    for x, pos in enumerate(matrix[0]):
        if pos == "O":
            start = x

    i = start
    j = 0
    pos = set()
    for move in path:
        if move == "L":
            i -= 1

        elif move == "R":
            i += 1

        elif move == "U":
            j -= 1

        elif move == "D":
            j += 1
        pos.add((j, i))
    
    for j, row in enumerate(matrix):
        for i, col in enumerate(row):
            if (j, i) in pos:
                print("+ ", end="")
            else:
                print(col + " ", end="")
        print()

def valid(matrix, moves):
    for x, pos in enumerate(matrix[0]):
        if pos == "O":
            start = x

    i = start
    j = 0
    for move in moves:
        if move == "L":
            i -= 1

        elif move == "R":
            i += 1

        elif move == "U":
            j -= 1

        elif move == "D":
            j += 1

        if not(0 <= i < len(matrix[0]) and 0 <= j < len(matrix)):
            return False
        elif (matrix[j][i] == "#"):
            return False

    return True

def findEnd(matrix, moves):
    for x, pos in enumerate(matrix[0]):
        if pos == "O":
            start = x

    i = start
    j = 0
    for move in moves:
        if move == "L":
            i -= 1

        elif move == "R":
            i += 1

        elif move == "U":
            j -= 1

        elif move == "D":
            j += 1

    if matrix[j][i] == "X":
        print("Found: " + moves)
        printmatrix(matrix, moves)
        return True

    return False

matrixInc

nums = matrixInc.MatrixInc()
nums.put("")
add = ""
matrix  = creatematrix2()

while not findEnd(matrix, add): 
    add = nums.get()


    for j in ["L", "R", "U", "D"]:
        put = add + j
        if valid(matrix, put):
            nums.put(put)

### --------------------------------------------------------------------------------------

##### Codigo 2

### --------------------------------------------------------------------------------------

import numpy as np
import time

class Grafo:

    def __init__(self, n):
        self.matriz_adj = np.zeros((n, n), dtype="int")
        self.n_vertices = n

    def imprimir(self):        
        print(self.matriz_adj)

    def inserir_vertice(self, origem, destino, direcao = 0):
        if (direcao == 0): 
            self.matriz_adj[origem, destino] = 1
            self.matriz_adj[destino, origem] = 1
        else:
            self.matriz_adj[origem, destino] = 1

    def retorna_vizinhos(self, v):
        vizinhos = []
        origem = 0
        while origem < self.n_vertices:
            if self.matriz_adj[origem][v] == 1:
                vizinhos.append(origem)
            origem += 1
        
        return vizinhos

    def conta_componentes(self):
        n_componentes = 0
        visitados = np.zeros(self.n_vertices, dtype="int")
        for v in range(self.n_vertices):
            for w in range(self.n_vertices):
                if self.matriz_adj[v][w] == 1:
                    if visitados[w] == 0:
                        n_componentes += 1
                        self.busca_profundidade(w, visitados)
        
        return n_componentes
                
    def busca_profundidade_grafo(self, v_inicial):
        visitados = np.zeros(self.n_vertices, dtype="int")
        print(visitados)
        self.busca_profundidade(v_inicial, visitados)

    def busca_profundidade(self, v_inicial, visitados):
        visitados[v_inicial] = -1 #Marca como visitado
        for w in range(self.n_vertices):
            valor = self.matriz_adj[v_inicial][w] 
            if (valor == 1): #Verifica se os v??rtices s??o vizinhos
                if visitados[w] == 0: #N??o visitado
                    print("v{}->w{}".format(v_inicial, w))
                    self.busca_profundidade(w, visitados)

    def verifica_caminho(self, origem, destino):
        linhaori  = origem[0]
        colunaori = origem[1]

        linhadest  = destino[0]
        colunadest = destino[1]

        mapa = self.matriz_adj

        if linhaori == linhadest and \
                colunaori == colunadest:
            mapa[linhaori][colunaori] = 1
            return True
        
        print(np.array(mapa))
        print()
        #tam_lin, tam_col = mapa.shape        
        tam_lin = len(mapa)
        tam_col = len(mapa[0])
        #time.sleep(1)
        
        if (mapa[linhaori][colunaori] == -1):
            #Marca na posi????o do mapa como visitado
            mapa[linhaori][colunaori] = 1
            
            if (self.verifica_caminho( (linhaori, max(0, colunaori-1) ), destino)):
                return True
            
            if (self.verifica_caminho( (max(0, linhaori-1), colunaori), destino) ):
                return True

            if (self.verifica_caminho( (linhaori, min(tam_col, colunaori+1) ), destino) ):
                return True

            if (self.verifica_caminho( ( min(tam_lin, linhaori+1), colunaori), destino)):
                return True

if __name__ == "__main__":
    grafo = Grafo(n=6)

    grafo.matriz_adj = [[0, 0, 0, 0, 0, 0, 0, 0], 
                        [0,-1,-1,-1,-1,-1,-1, 0],
                        [0,-1,-1,-1,-1,-1,-1, 0],
                        [0, 0, 0, 0,-1,-1,-1, 0],
                        [0,-1,-1,-1, 0,-1,-1, 0],
                        [0,-1,-1,-1, 0,-1,-1, 0],
                        [0,-1,-1,-1, 0,-1,-1, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0]    
                    ]
    grafo.verifica_caminho( (6,2) , (6,6) )

### --------------------------------------------------------------------------------------

### Codigo 3

### --------------------------------------------------------------------------------------



if __name__ == "__main__":
    grafo = Grafo(n=6)

    grafo.matriz_adj = [[0, 0, 0, 0, 0, 0, 0, 0], 
                        [0,-1,-1,-1, 0,-1,-1, 0],
                        [0,-1,-1,-1, 0,-1,-1, 0],
                        [0, 0, 0, 0, 0,-1,-1, 0],
                        [0,-1,-1,-1, 0,-1,-1, 0],
                        [0,-1,-1,-1, 0,-1,-1, 0],
                        [0,-1,-1,-1, 0,-1,-1, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0]    
                    ]
    grafo.verifica_caminho( (6,2) , (6,6) )

