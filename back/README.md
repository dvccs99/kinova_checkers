# Equipe5-back
Este repositório contém os arquivos de back-end da equipe 5 do último projeto da disciplina de Fábrica de Software 2, da residência em inteligência artificial e robótica do CIn/UFPE.
O projeto consiste em programar um robô Kinova Gen3 Lite equipado com uma câmera para jogar damas. 

# Primeira sprint

Para rodar os entregáveis da primeira sprint, basta rodar o arquivo main.py. As posições do tabuleiro foram marcadas utilizando letras nas linhas e números nas colunas em ordem crescente a partir da posição do operador do robô. Ou seja, estando sentado na cadeira com o controle, a posição mais a direita e mais em cima é H8 e a mais a esquerda e mais em baixo é A1.  

# Segunda sprint

Na segunda sprint, acrescentamos um arquivo camera com a classe Captura. Ao rodar este arquivo, a câmera do robô será acionada e a foto será salva com o nome FotoTabuleiro.png.
Também foi acrescentado o arquivo yolov8_script que recebe uma imagem de tabuleiro e devolve a imagem com as boundbox na pasta runs\detect\predict conforme treinamento. Para utilizar o script YOLO, é preciso baixar os pesos da rede que estão em 'runs/detect/train3/weights/best.pt'.
No momento, a câmera ainda não está vinculada com o Yolo.

# Terceira sprint

Na terceira sprint, integramos a visão computacional a lógica de jogo e fizemos um programa para rodar o jogo.
Dessa forma, para rodar o jogo pelo terminal, rode o arquivo Main.

# Instalação das bibliotecas
- pip install -r requirements.txt
- pip install ultralytics

# Modelo gerado
- o modelo encontrase na pasta 'src\runs\weights\best.pt' arquivo com a extensão .pt



