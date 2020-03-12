#MÓDULOS E PACOTES

# Módulo --> arquivo .py que carrega classes determinadas 

# Palvra mágica = IMPORT

import math #módulo q ja vem por padrão

# importando o arquivo "Criando_classes.py" 

from Criando_classes import Carro #classe em específico
#ou 
from Criando_classes import * #import universa (melhor não fazer)

fusca=Carro()

print(fusca.aceleration,fusca.estado)



fusca.acelerar()

print(fusca.aceleration,fusca.estado)



''' 
Pacotes --> junção de módulos (pasta/diretório com arquivos 
.py que possúi um file vazio com o nome __init__.py) 

Como importar:

from pacote.file import classe1,classe2
'''


