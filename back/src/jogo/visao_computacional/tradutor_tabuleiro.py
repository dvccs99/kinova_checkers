import os

class PosicaoTabuleiro:
    def __init__(self, num_robot):
        self.delta_x = 0
        self.delta_y = 0
        self.num_robot = num_robot
        self.bank_pixels = self.create_bank_pixel()

    def create_bank_pixel(self):
        #Robô da parede:
        if self.num_robot == 1:
            self.delta_x = 40
            self.delta_y = 40
            return {
                'DAMA1': [580, 180],
                'DAMA2': [580, 303],
                'DAMA3': [575, 417],
                'DAMA4': [575, 545],
                'DAMA5': [131, 155],
                'DAMA6': [127, 217],
                'DAMA7': [118, 333],
                'DAMA8': [116, 445],
                'A1': [506, 124],
                'A3': [415, 122],
                'A5': [331, 120],
                'A7': [245, 113],
                'B2': [459, 182],
                'B4': [370, 176],
                'B6': [286, 174],
                'B8': [203, 166],
                'C1': [503, 241],
                'C3': [414, 235],
                'C5': [326, 231],
                'C7': [240, 224],
                'D2': [455, 296],
                'D4': [367, 289],
                'D6': [279, 283],
                'D8': [198, 281],
                'E1': [500, 355],
                'E3': [409, 350],
                'E5': [322, 346],
                'E7': [231, 337],
                'F2': [450, 411],
                'F4': [467, 407],
                'F6': [276, 397],
                'F8': [190, 393],
                'G1': [500, 477],
                'G3': [406, 467],
                'G5': [318, 461],
                'G7': [231, 455],
                'H2': [448, 534],
                'H4': [361, 525],
                'H6': [273, 518],
                'H8': [185, 511],
            }
        #Robô da janela
        elif self.num_robot == 2:
            self.delta_x = 40
            self.delta_y = 40
            return {
                'DAMA1': [536, 183],
                'DAMA2': [541, 312],
                'DAMA3': [544, 438],
                'DAMA4': [539, 565],
                'DAMA5': [104, 196],
                'DAMA6': [100, 258],
                'DAMA7': [100, 375],
                'DAMA8': [93, 498],
                'A1': [560, 138],
                'A3': [370, 141],
                'A5': [285, 141],
                'A7': [198, 141],
                'B2': [414, 195],
                'B4': [328, 196],
                'B6': [243, 195],
                'B8': [156, 200],
                'C1': [159, 255],
                'C3': [370, 255],
                'C5': [285, 257],
                'C7': [198, 254],
                'D2': [414, 314],
                'D4': [328, 314],
                'D6': [242, 314],
                'D8': [157, 312],
                'E1': [461, 374],
                'E3': [372, 368],
                'E5': [285, 372],
                'E7': [200, 368],
                'F2': [415, 428],
                'F4': [328, 431],
                'F6': [242, 429],
                'F8': [154, 429],
                'G1': [461, 489],
                'G3': [373, 489],
                'G5': [284, 488],
                'G7': [198, 490],
                'H2': [417, 553],
                'H4': [328, 554],
                'H6': [240, 549],
                'H8': [152, 546],
            }
        
        else:
            return {}

    def nomeCasa(self, pos_x, pos_y):
        x_desnorm = 640 * pos_x
        y_desnorm = 640 * pos_y
        for loc_tab, val_pixel in self.bank_pixels.items():
            if (val_pixel[0] - self.delta_x <= x_desnorm <= val_pixel[0] + self.delta_x) and (val_pixel[1] - self.delta_y <= y_desnorm <= val_pixel[1] + self.delta_y):
                return loc_tab
        return None

    def lerArquivo(nome_arq, posicao_tabuleiro):
        pecas_dict = {}
        try:
            with open(nome_arq + '.txt', 'r') as arq_label:
                for obj in arq_label:
                    linha = obj.split()
                    rotulo = int(linha[0])
                    x_norm = float(linha[1])
                    y_norm = float(linha[2])
                    peca = rotulo

                    if rotulo == 0:
                        peca = 'dama roxa'
                    elif rotulo == 1:
                        peca = 'dama verde'
                    elif rotulo == 2:
                        peca = 'peão roxo'
                    elif rotulo == 3:
                        peca = 'peão verde'
                    else:
                        peca = 'desconhecido'
                    pecas_dict[posicao_tabuleiro.nomeCasa(x_norm, y_norm)] = peca
            os.remove('src/jogo/visao_computacional/predict/labels/FotoTabuleiro.txt')
            return pecas_dict
        except FileNotFoundError:
            print(f"Arquivo {nome_arq}.txt não encontrado.")
        except Exception as e:
            print(f"Ocorreu um erro: {e}")

## Testando
# teste = PosicaoTabuleiro(1)
# print(PosicaoTabuleiro.lerArquivo('src/jogo/visao_computacional/predict/labels/FotoTabuleiro', teste))

