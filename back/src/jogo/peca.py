from src.jogo.tabuleiro import *
from src.jogo.aux_funcs import *



class Peca:
    def __init__(self, cor, pos):
        self.cor = cor
        self.pos = pos
        self.pos_init = pos
        self.isdama = False
        self.diag_local = diagonais(self.pos,1,0)
        self.diag_local_capt = diagonais(self.pos,1,1)
        self.diag_global = diagonais(self.pos,7,0)
        self.alvo = self.diag_local_capt

    @property
    def virar_dama(self):
        self.isdama = True
        self.alvo = self.diag_global

    @property
    def att_diags(self):
        self.diag_local = diagonais(self.pos,1,0)
        self.diag_global = diagonais(self.pos,7,0)
        if self.isdama == False:
            self.alvo = self.diag_local
        elif self.isdama == True:
            self.alvo = self.diag_global

    def __str__(self):
        if self.isdama == True:
            return f"Dama, cor: {self.cor}, pos: {self.pos}"
        else:
            return f"Peça, cor: {self.cor}, pos: {self.pos}"

    
