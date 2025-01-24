from src.jogo.peca import *
from src.jogo.aux_funcs import *

class Tabuleiro():
    def __init__(self,modo):
        self.posicoes = {
            'A1': '', 'A3': '', 'A5': '', 'A7': '', 'B2': '', 'B4': '', 'B6': '', 'B8': '',
            'C1': '', 'C3': '', 'C5': '', 'C7': '', 'D2': '', 'D4': '', 'D6': '', 'D8': '',
            'E1': '', 'E3': '', 'E5': '', 'E7': '', 'F2': '', 'F4': '', 'F6': '', 'F8': '',
            'G1': '', 'G3': '', 'G5': '', 'G7': '', 'H2': '', 'H4': '', 'H6': '', 'H8': ''
            }
        
        self.lado1 = ['A1', 'A3', 'A5', 'A7', 'B2', 'B4', 'B6', 'B8', 'C1', 'C3', 'C5', 'C7']
        self.lado2 = ['F2', 'F4', 'F6', 'F8', 'G1', 'G3', 'G5', 'G7', 'H2', 'H4', 'H6', 'H8']

        if modo == 'roxo':
            for posicao in self.lado2:
                self.posicoes[posicao] = Peca('verde', posicao)
            for posicao in self.lado1:
                self.posicoes[posicao] = Peca('roxo', posicao)
        elif modo == 'verde':
            for posicao in self.lado2:
                self.posicoes[posicao] = Peca('roxo', posicao)
            for posicao in self.lado1:
                self.posicoes[posicao] = Peca('verde', posicao)
        elif modo == 'vazio':
            pass
