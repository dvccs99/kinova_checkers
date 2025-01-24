from src.jogo.damas import Damas
from src.jogo.visao_computacional import *
from src.jogo.peca import Peca
import random

jogo = Damas('vazio',3)
jogo.cor_robo = 'verde'
jogo.tb.posicoes['A1'] = Peca('verde','A1')
print(jogo.roboJogadas)
