import time

from src.robo.bank_moviments import *
from src.robo.abstract_robot import AbstractRobot
from src.jogo.peca import *


class TestRobot(AbstractRobot):

    ajuste_int = 0.05
    tempo_garra = 0.6

    def __init__(self):
        self.posicao_cartesiana = ""
        self.posicao_juntas = ""
        self.connected = False

    def conectar(self):
        print("O Robo conectou")
        self.connected = True
        return True

    def desconectar(self):
        self.connected = False
        print("\nO Robo foi desconectado\n")

    def remover_peca(self, peca):
        print(f"\nPeça da posição {peca.pos} retirada\n")

    def movimentar_peca(self, peca, posicao):
        print(f"\nPeça movida da posição {peca.pos} para a posição {posicao}\n")

    def mov_caminho(self, peca, array_caminho):
        print(f"\nPeça em {peca.pos} se movimentou para {array_caminho}\n")

    def abrir_garra(self):
        print("\nO Robo abriu a garra\n")
        time.sleep(0.1)

    def fechar_garra(self,tempo):
        print(f"\nO Robo fechou a garra por {tempo} segundos\n")
        time.sleep(0.1)