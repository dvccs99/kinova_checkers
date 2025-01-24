from src.robo.bank_moviments import *
from src.robo.abstract_robot import AbstractRobot
from rria_api.robot_object import RobotObject
from rria_api.robot_enum import RobotEnum

class RealRobot(AbstractRobot):

    ajuste_int = 0.05
    tempo_garra = 0.6

    def __init__(self, num_int):
        self.robot = RobotObject('192.168.2.10', RobotEnum.GEN3_LITE)
        self.BANK_MOVEMENT = create_bank_movement(num_int)

    @property
    def conectar(self) -> None:
        self.robot.connect_robot()
        self.robot.open_gripper()
        pos = self.robot.get_cartesian()
        self.fechar_garra(1.3)
        self.robot.move_cartesian(*pos)
        self.robot.move_cartesian(*self.BANK_MOVEMENT.get('POS_FOTO'))
        print("Kinova está conectado!\n")
    
    @property
    def desconectar(self) -> None: 
        # array_movement = self.BANK_MOVEMENT.get('HOME')
        # self.robot.move_joints(*array_movement)
        self.robot.safe_disconnect()
        print('Kinova está desconectado!\n')
    
    #Recebe a posicao da peça para ser retirada e colocada no depósito.
    def remover_peca(self, posicao_TB: str):
        ajuste = 0.01
        #assumindo que ele estará na posição intermediária do tabuleiro antes de pegar qualquer peça:
        j1, j2, j3, j4, j5, j6 = self.BANK_MOVEMENT[posicao_TB]
        self.robot.move_cartesian(j1+ajuste, j2, j3+self.ajuste_int, j4, j5, j6) #em cima da peça a ser retirada
        self.robot.move_cartesian(j1+ajuste, j2, j3, j4, j5, j6) #desce para a peça que ele quer pegar
        self.fechar_garra()
        self.robot.move_cartesian(j1+ajuste, j2, j3+self.ajuste_int, j4, j5, j6) #sobe novamente para cima da peça a ser retirada
        self.robot.move_cartesian(*self.BANK_MOVEMENT.get('POS_FOTO')) #vai para a posição de foto que funciona como intermediária
        self.robot.move_joints(*self.BANK_MOVEMENT.get('DEPOSITO')) #vai para o local do depósito
        self.abrir_garra() #solta a peça
        self.robot.move_joints(*self.BANK_MOVEMENT.get('POS_FOTO_JUNTAS')) #retorna para o tabuleiro

    #Recebe a posição da peça a ser movida e um array de posições que ele irá usar para se movimentar
    def mov_caminho(self, posicao_peca, array_caminho) -> None:
        array_movement1 = self.BANK_MOVEMENT.get(posicao_peca)
        mov1_int2 = array_movement1.copy()
        mov1_int2[0]+=0.005
        mov1_int = mov1_int2.copy()
        mov1_int[2]+=self.ajuste_int
        self.robot.move_cartesian(*mov1_int)
        self.robot.move_cartesian(*mov1_int2)
        self.fechar_garra()
        self.robot.move_cartesian(*mov1_int)
        for i in range(len(array_caminho)):
            pos = array_caminho[i]
            print(pos)
            pos_movement = self.BANK_MOVEMENT.get(pos)
            pos_int2 = pos_movement.copy()
            pos_int2[0]+=0.005
            pos_int = pos_int2.copy()
            pos_int[2]+=self.ajuste_int
            self.robot.move_cartesian(*pos_int)
            self.robot.move_cartesian(*pos_int2)
            if i == len(array_caminho)-1:
                self.abrir_garra()
                self.robot.move_cartesian(*pos_int)
                self.robot.move_cartesian(*self.BANK_MOVEMENT.get('POS_FOTO'))
            else:
                self.robot.move_cartesian(*pos_int2)
                self.robot.move_cartesian(*pos_int)

    @property
    def posicao_foto(self):
        self.robot.move_cartesian(*self.BANK_MOVEMENT.get('POS_FOTO'))

    def abrir_garra(self):
        self.robot.open_gripper(self.tempo_garra)

    def fechar_garra(self,tempo=tempo_garra):
        self.robot.close_gripper(tempo)