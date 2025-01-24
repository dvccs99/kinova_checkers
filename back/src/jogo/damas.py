from src.jogo.tabuleiro import *
from src.jogo.visao_computacional.yolo_camera import *
from src.jogo.peca import *
from src.jogo.aux_funcs import *
from src.jogo.visao_computacional.tradutor_tabuleiro import *
from src.robo.real_robot import *
from src.robo.test_robot import *
import random

class Damas:
    def __init__(self, modo,num_robot):
        self.tb = Tabuleiro(modo)
        self.num_robot = num_robot
        self.leitura = PosicaoTabuleiro(num_robot)
        self.estado = 'jogando'
        self.vencedor = None
        if num_robot == 1 or num_robot == 2:
            self.robo = RealRobot(num_robot)
        elif num_robot == 3:
            self.robo = TestRobot()
        if modo == 'verde':   
            self.cor_robo = 'roxo'
        elif modo == 'roxo':
            self.cor_robo = 'verde'

        self.robo.conectar
        
    @property
    def atualizar_tabuleiro(self):
        if self.num_robot != 3:
            self.robo.posicao_foto
            visao = ImagePredictor()
            visao.capture_image()
            visao.predict_image()
            new_tb = PosicaoTabuleiro.lerArquivo('src/jogo/visao_computacional/predict/labels/FotoTabuleiro', self.leitura)
            for chave in self.tb.posicoes:
                if chave in new_tb:
                    if new_tb[chave] == 'peão verde':
                        self.tb.posicoes[chave] = Peca('verde',chave)
                    if new_tb[chave] == 'peão roxo':
                        self.tb.posicoes[chave] = Peca('roxo',chave)
                    if new_tb[chave] == 'dama verde':
                        self.tb.posicoes[chave] = Peca('verde',chave)
                        self.tb.posicoes[chave].virar_dama
                    if new_tb[chave] == 'dama roxa':
                        self.tb.posicoes[chave] = Peca('roxo',chave)
                        self.tb.posicoes[chave].virar_dama
                else:
                    self.tb.posicoes[chave] = ''


    def capturavel(self,peca1,peca2):
            if peca1.cor == peca2.cor:
                return [False]
            else:  
                if peca2.pos in peca1.diag_local:
                    interseccao = [x for x in peca1.diag_global if x in peca2.diag_local]
                    if interseccao == []:
                        return [False]
                    else:
                        for posicao in interseccao:
                            if self.tb.posicoes[posicao] == '' and posicao not in diagonais(peca1.pos,distancia(peca1,peca2),0):
                                return [True,posicao]
                        return [False]
                else:
                    return [False]

    count = 0
    def movimentarPeca(self, peca, pos):
        if peca.isdama == True:
            interseccao = [x for x in peca.alvo if x in diagonais(pos,7,0)]            
            for x in interseccao:
                if self.tb.posicoes[x] != '':
                    print("Não é possível realizar a movimentação - 1")
                    return 0
        if pos in peca.alvo and self.tb.posicoes[pos] == '':
            self.robo.mov_caminho(peca.pos,[pos])
            self.tb.posicoes[pos] = peca
            self.tb.posicoes[peca.pos] = ''
            peca.pos = pos
            peca.att_diags
            if peca.pos_init in self.tb.lado1:
                if peca.pos in ['H2', 'H4','H6','H8']:
                    if count<3:
                        self.robo.remover_peca(peca.pos)
                        count+=1
                        count= count%4
                        damas = ['DAMA5','DAMA6','DAMA7','DAMA8']
                        self.robo.mov_caminho(damas[count],peca.pos)
                        peca.isdama = True
                    else:
                        print('cabou dama')
            elif peca.pos_init in self.tb.lado2:
                if peca.pos in ['A1','A3','A5','A7']:
                    if count<3:
                        self.robo.remover_peca(peca.pos)
                        count+=1
                        count= count%4
                        damas = ['DAMA5','DAMA6','DAMA7','DAMA8']
                        self.robo.mov_caminho(damas[count],[peca.pos])
                        peca.isdama = True
                    else:
                        print('cabou dama')
        else:
            print("Não é possível realizar a movimentação - 2")
            return 0

        
    def capturarPeca(self, peca1, peca2):
        if self.capturavel(peca1,peca2)[0]:
            self.robo.mov_caminho(peca1.pos, [self.capturavel(peca1,peca2)[1]])
            self.robo.remover_peca(peca2.pos)
            new_pos1 = self.capturavel(peca1,peca2)[1]
            self.tb.posicoes[peca1.pos] = ''
            peca1.pos = new_pos1
            self.tb.posicoes[new_pos1] = peca1
            self.tb.posicoes[peca2.pos] = ''
            peca2.pos = 'capturada'
        else:
            return print("Não é possível realizar captura")
             
    @property
    def damaDisponivel(self):
        dama_l1 = True
        dama_l2 = True
        dama_l1_qtd = 4
        dama_l2_qtd = 4
        damas_humano = ['DAMA1', 'DAMA2', 'DAMA3', 'DAMA4']
        damas_robo = ['DAMA5', 'DAMA6', 'DAMA7', 'DAMA8']

        for casa in damas_humano:
            if self.tb.posicoes[casa]== '':
                damas_humano.remove(casa)
                dama_l1_qtd -= 1
            
        for casa in damas_robo:
            if self.tb.posicoes[casa] == '':
                damas_robo.remove(casa)
                dama_l2_qtd -= 1
        
        if dama_l1_qtd == 0:
            dama_l1 = False
        
        if dama_l2_qtd == 0:
            dama_l2 = False

        return(damas_robo,dama_l2, dama_l1,damas_humano)

    def colocarDama(self,pos):
        if self.damaDisponivel[1] == True:
            self.robo.mov_caminho(self.damaDisponivel[0], [pos])
    
    @property
    def qntPecas(self):
            count_v = 0
            count_r = 0
            for casa in self.tb.posicoes:
                if self.tb.posicoes[casa] == '':
                    pass
                else:
                    if self.tb.posicoes[casa].cor == 'verde':
                        count_v+=1
                    elif (self.tb.posicoes[casa]).cor == 'roxo':
                        count_r+=1
            
            return (count_r, count_v)
    
    # def roboJogar(self):
    #     robo_movs = self.roboJogadas[0]
    #     robo_capts = self.roboJogadas[1]
    #     if robo_capts != []:
    #         self.capturarPeca(*random.choice(robo_capts))
    #     else:
    #         self.movimentarPeca(*random.choice(robo_movs))

    def roboJogar(self):
        robo_movs = self.roboJogadas[0]
        robo_capts = self.roboJogadas[1]
        raldo = random.randint(1,2)
        aux = True
        while aux == True:
            if raldo == 1:
                if robo_movs == []:
                    raldo = 2
                else:
                    play = random.choice(robo_movs)
                    self.movimentarPeca(*play)
                    aux = False
            elif raldo == 2:
                if robo_capts == []:
                    raldo = 1
                else:
                    self.capturarPeca(*random.choice(robo_capts))
                    aux = False

    @property
    def roboJogadas(self):
        robo_movs = []
        robo_capts = []
        robo_pecas = []
        for pos in self.tb.posicoes:
            peca = self.tb.posicoes[pos]
            if peca!= '' and peca.cor == self.cor_robo:
                robo_pecas.append(peca)
                for pos2 in peca.alvo:
                    peca2 = self.tb.posicoes[pos2]
                    if peca2 != '' and peca2.cor != self.cor_robo and self.capturavel(peca, peca2)[0]:
                        robo_capts.append((peca,peca2))
                    if peca2 == '':
                        robo_movs.append((peca,pos2))
        return [robo_movs,robo_capts,robo_pecas]







    



#TESTE CAPTURA
# jogo.tb.posicoes['G5'] = Peca('verde','G5')
# jogo.tb.posicoes['E3'] = Peca('roxo','E3')
# jogo.tb.posicoes['E3'].virar_dama
# print(jogo.tb.posicoes)
# jogo.capturar_peca(jogo.tb.posicoes['E3'], jogo.tb.posicoes['G5'])
# print(jogo.tb.posicoes)

#TESTE CAPTURAVEL
# jogo.tb.posicoes['G5'] = Peca('verde','G5')
# jogo.tb.posicoes['G5'].isdama = False
# jogo.tb.posicoes['E3'] = Peca('roxo','E3')
# jogo.tb.posicoes['E3'].virar_dama
# # jogo.tb.posicoes['D2'] = Peca('roxo','D2')
# print(jogo.capturavel(jogo.tb.posicoes['E3'],jogo.tb.posicoes['G5']))
# jogo.tb.posicoes['A1'] = Peca('verde','A1')
# jogo.tb.posicoes['B2'] = Peca('roxo','B2')
# jogo.tb.posicoes['A3'] = Peca('verde','A3')
# jogo.tb.posicoes['B4'] = Peca('verde','B4')
# # print(jogo.tb.posicoes)
# print(jogo.capturavel(jogo.tb.posicoes['A1'],jogo.tb.posicoes['B2']))
# # print(jogo.tb.posicoes['B2'].diag_local)
# # print(jogo.tb.posicoes['A1'].diag_local)
# print(jogo.capturavel(jogo.tb.posicoes['B2'],jogo.tb.posicoes['A1']))
# print(jogo.capturavel(jogo.tb.posicoes['A3'],jogo.tb.posicoes['B2']))
# print(jogo.capturavel(jogo.tb.posicoes['A3'],jogo.tb.posicoes['B4']))


#TESTE MOVIMENTO
# jogo = Damas('verde',3)
# print(jogo.tb.posicoes)
# print('===============================================================================')
# jogo.movimentarPeca('C1', 'D2')
# print(jogo.tb.posicoes)
