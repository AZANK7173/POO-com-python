#HERANÇA

class Classe(int):
	"""int herda caracterÃ­sticas e mÃ©todos para a nova classe (subclasse ou derivada)"""

	pass


class Pessoas:
    
    def __init__(self, nome, idade,x=None):
        self.nome = nome 
        self.idade = idade
        self.__x = x  #atributo privado 
    
    def aniversario(self):
        self.idade += 1
        print(self.nome,"fez aniversário!")
    

class Trabalhador(Pessoas):
    
    def __init__(self, cargo, nome, idade,x):
        super().__init__(nome,idade)
        # Pessoas.__init__(self, nome, idade,x) --> equivalente à linha acima
        self.cargo=cargo

john=Trabalhador('gerente','john',23,30)

print(john.idade)

john.aniversario()

print(john.idade)



#HERANÇA MÚLTIPLA: uma classe pode puxar atributos de várias classes


class Pessoa:
    def __init__(self, nome, idade, altura, bracos=2):
        self.nome=nome
        self.idade=idade
        self.altura=altura
        
    def crescer(self):
        self.altura += 0.5
    
    def aniversario(self):
        self.idade += 1
        
    def __str__(self):
        return f"Essa pessoa se chama {self.nome}, tem {self.idade} anos e {self.altura} metros de altura"
        

class Aranha:
    
    def __init__(self,nome, cor, pulo, membros=8):
        self.nome=nome
        self.cor=cor
        self.pulo=pulo
        self.membros=membros
    
    def escalar(self):
        return f"{self.nome} escalou pela parede"
    
    def pular(self):
        return f"{self.nome} consegue pular {self.pulo} metros"
    
    def __str__(self):
        return f"a dona {self.nome} subiu pela parede, veio a chuva forte, e a derrubou"



class HomemAranha(Pessoa,Aranha):
    def __init__(self, nome, idade, altura, cor, pulo):
        Pessoa.__init__(self, nome, idade, altura)
        Aranha.__init__(self,nome, cor, pulo)
        
    def __str__(self):
        return Pessoa.__str__(self) + ' , ' + Aranha.__str__(self)
    
    def heroi(self):
        return "I was bitten by a radioactive spider and for ten years I’ve been the one and only Spider-Man. I’m pretty sure you know the rest."
    
    
miles=HomemAranha('Miles Morales',15,1.65,'vermelho e preto',10)

print(miles)


print(miles.pular())


print(miles.heroi())
    
    
    
    