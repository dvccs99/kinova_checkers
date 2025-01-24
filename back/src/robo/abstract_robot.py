from abc import ABC, abstractmethod

class AbstractRobot():


    @abstractmethod
    def conectar(self) -> bool:
        ...
    
    @abstractmethod
    def desconectar(self) -> bool:
        ...
    
    @abstractmethod
    def remover_peca(self, posicao_TB) -> None:
        ...

    @abstractmethod
    def movimentar_peca(self, posicao_peca, posicao_vaga) -> None:
        ...

    @abstractmethod
    def mov_caminho(self, posicao_peca, array_caminho) -> None:
        ...

    @abstractmethod
    def abrir_garra(self) -> None:
        ...
    

    @abstractmethod
    def fechar_garra(self) -> None:
        ...