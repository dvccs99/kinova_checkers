from src.robo.bank_moviments import *
from src.robo.real_robot import RealRobot
from src.robo.test_robot import TestRobot
from src.jogo.damas import *

system = True
robot = None
while system:
    if robot is None:
        print("****MENU ESCOLHA ROBÔ****\n"
              "[1] Robô real\n"
              "[2] Robô de teste\n"
              "Para sair digite uma letra:\n")
        
        choice = input()

        if choice.isnumeric():
            choice = int(choice)
            if choice == 1:
                num_int = int(input("Digite 1 para o Knova (do lado do Denso) e 2 para o Kinova (perto da janela): "))
                robot = RealRobot(num_int)
            elif choice == 2:
                robot = TestRobot()
            else:
                print('Escolha invalida')
        else:
            print('Saindo do Simulador')
            system = False

    else:
        print("****MENU CONTROLE DO ROBÔ****\n"
              "[1] Conectar robô\n"
              "[2] Mover uma peça do tabuleiro\n"
              "[3] Remover uma peça do tabuleiro\n"
              "[4] Colocar uma dama no tabuleiro\n"
              "OBS: As posicões no tabuleiro são representadas com letras e números em ordem crescente a partir do referencial do operador do robô. e.g: a1, B2, c3, D4\n"
              "OBS2: Para mover uma peça passando por diversas posições vazias, quando pedido para digitar um destino digite a sequência de posições separadas por espaço.\n"
              "Para sair digite uma letra:")

        choice = input()
        
        if choice.isnumeric():
            choice = int(choice)
            
            if choice == 1:
                robot.conectar()
                pos = robot.robot.get_cartesian()
                robot.fechar_garra(1.3)
                robot.robot.move_cartesian(*pos)
                print('Robo conectado\n')

            elif choice == 2:
                posicao_peca = input("Digite a posição da peça a ser movida: ").upper()
                posicao_vaga_input = input("Digite a(s) posição vaga(s) para mover a peça: ").upper()
                posicao_vaga = posicao_vaga_input.split()
                robot.mov_caminho(posicao_peca, posicao_vaga)

                
            elif choice == 3:
                # posicao_TB = input("Digite a posição da peça a ser removida: ").upper()
                # robot.remover_peca(posicao_TB)
                jogo = Damas('jog1','jog2','vazio')
                print(jogo.tb.posicoes)
                jogo.atualizar_tabuleiro
                print(jogo.tb.posicoes)
                
            elif choice == 4:
                posicao_dama = input("Digite a posição de uma dama. OBS: DAMA1, DAMA2, etc...: ").upper()
                posicao_vaga = input("Digite a posição vaga para colocar a dama: ").upper()
                robot.mov_caminho(posicao_dama, posicao_vaga)
                
            else:
                print('Escolha inválida')
        else:
            robot.desconectar()
            print('Saindo do controle do robô\n')
            robot = None