from src.jogo.damas import Damas
from src.jogo.visao_computacional import *
import random

system = True
jogador = None
cor_peca = None
num_robot = None

while system:

    print("****MENU ESCOLHA ROBÔ****\n"
            "[1] Robô KNova (ao lado do Denso)\n" 
            "[2] Robô Kinova (ao lado da janela)\n"
            "Para sair digite uma letra:\n")
    
    choice = input()

    if choice.isnumeric():
        num_robot = int(choice)

        print(f'Quem vai começar?\n'
            '[1] Equipe X\n'
            '[2] Equipe 5\n'
            '[3] Aleatório\n')
    
        choice = input()

        if choice.isnumeric():
            choice = int(choice)
            if choice == 1:
                jogador = 'humano'
            elif choice == 2:
                jogador = 'robot'

            else:
                jogador = random.randint(1,2)

            print(f'Vamos começar por {jogador}')
        
        else:
            jogador = random.randint(1,2)
            print(f'Vamos começar aleatoriamente por {jogador}')
        
        print("****MENU ESCOLHA COR DA EQUIPE 5****\n"
            "[1] ROXO\n"
            "[2] VERDE\n")
        choice = input()
        if choice.isnumeric():
            choice = int(choice)
            if choice == 1:
                cor_peca =  'roxo'
            else:
                cor_peca = 'verde'

        jogo = Damas(cor_peca, num_robot)

        while jogo.estado=='jogando':
            print(f'Peças Roxas: {jogo.qntPecas[0]}\n'
                  f'Peças Verdes: {jogo.qntPecas[1]}')
            if jogador == 'humano':
                print("SUA VEZ DE JOGAR.\n"
                      "Ao finalizar a jogada, digite uma letra e ENTER.\n")
                humano_jogou = input()
                if humano_jogou != '':
                    jogo.atualizar_tabuleiro
                    jogador = 'robot'
                            
            else:
                print("VEZ DO ROBÔ")
                jogo.roboJogar()
                jogo.atualizar_tabuleiro
                jogador = 'humano'
        
        if jogo.estado == 'empatado':
            print('EMPATE!!')

        elif jogo.estado == 'finalizado':
            print(f'O vencedor foi o {jogo.vencedor}')
    
    else:
        system = False