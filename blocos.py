import random
from mapa import Mapa

class Bloco():
    def __init__(self) -> None:
        self.blocos = {
            'Grama' : ['~', ';', ','],
            'Arvore' : 'O',
            'Madeira' : '#',
            'Semente' : 'x',
            'Bergamota' : 'X'
        }    

    # Muda o caractere da posição passada como parâmetro
    def colocar_bloco(self, pos_y: int, pos_x: int, bloco: str, mapa: Mapa) -> None:
        mapa.atualizar_mapa(pos_y, pos_x, self.blocos[bloco])