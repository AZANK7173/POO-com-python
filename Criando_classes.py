# CRIANDO UMA CLASSE

class MinhaClasse:
    pass 

# Instanciando um objeto dessa classe 

obj = MinhaClasse()

print('type do objeto: ' + str(type(obj)))

print('o objeto: ')
print(obj)






# ADICIONANDO ATRIBUTOS

# é possível adicionar atributos aleatoriamente
obj.x=10
obj.cor='vermelho'
obj.nome='tais'







# DEFININDO MÉTODOS

class Carro:

    def __init__(self, aceleration=0, estado='parado'):
        self.aceleration=aceleration
        self.estado= estado


    def acelerar(self):
         self.aceleration = 5
         self.estado = 'se movendo'



#criando
car=Carro()
print('situação inicial')
print(car.aceleration,car.estado)



#utilizando método de acelerar
car.acelerar()
print('acelerar')
print(car.aceleration,car.estado)

#OBS: Parâmetros opcionais devem vir DEPOIS dos obrigatórios