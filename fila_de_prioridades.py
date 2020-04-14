# implementando uma fila de prioridade

import heapq

class Fila:
    
    def __init__(self):
        self.fila = []
        self.indice = 0
    
    def push(self, item, prioridade):
        heapq.heappush(self.fila, (-prioridade, self.indice, item))
        self.indice += 1
    
    def pop(self):
        return heapq.heappop(self.fila)[-1]

class Item:
    def __init__(self,nome):
        self.nome =  nome
    
    def __repr__(self):
        return self.nome
    

fila = Fila()
fila.push(Item('USA'),30)
fila.push(Item('Brasil'),34)
fila.push(Item('Italia'),56)

print(fila.pop())
print(fila.pop())
print(fila.pop())

