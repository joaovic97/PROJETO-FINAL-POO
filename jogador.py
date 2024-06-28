from inventario import Inventario
from blocos import Bloco
from animal import Animal
from mapa import Mapa

class Jogador(Animal):
    def __init__(self, nome: str) -> None:
        super().__init__('Humano', '@')
        self.__nome = nome
        self.__vigor = 50
        self.__fome = 50

    def get_nome(self) -> str:
        return self.__nome
    
    def get_vigor(self) -> int:
        return self.__vigor
    
    def get_fome(self) -> int:
        return self.__fome
    
    def falar(self, mensagem) -> str:
        return f'{self.__nome}: {mensagem}'

    def muda_vigor(self, valor: int) -> None:
        self.__vigor += valor
        if self.__vigor > 50:
            self.__vigor = 50
    
    def muda_fome(self, valor: int) -> None:
        self.__fome += valor
        if self.__fome > 50:
            self.__fome = 50

    # Coloca o símbolo de uma semente na coordenada passada
    def plantar(self, pos_y: int, pos_x: int, inventario: Inventario, bloco: Bloco, mapa: Mapa, janela) -> None:
        # Teste se o jogador tem o item e se tem energia para realizar a ação
        if inventario.tem_item('Semente') and self.get_fome() >= 3:
                bloco.colocar_bloco(pos_y, pos_x, 'Semente', mapa)
                inventario.remover_item('Semente', 1, janela)
                self.muda_fome(-2)
        else:
            janela.clear()
            janela.addstr(1, 1, 'Voce nao tem sementes para plantar ou está com fome.')

    def comer(self, inventario: Inventario, janela) -> None:
        # Teste se o jogador tem o item
        if inventario.tem_item('Bergamota'):
            inventario.remover_item('Bergamota', 1, janela)
            self.muda_fome(10)
            self.muda_vigor(5)
        else:
            janela.clear()
            janela.addstr(1, 1, 'Voce nao possui nenhum alimento.')
    
    def construir(self, pos_y: int, pos_x: int, inventario: Inventario, bloco: Bloco, mapa:Mapa, janela) -> None:
        # Teste se o jogador tem o item e se tem energia para realizar a ação
        if inventario.tem_item('Madeira') and self.get_fome() >= 5:
            bloco.colocar_bloco(pos_y, pos_x, 'Madeira', mapa)
            inventario.remover_item('Madeira', 1, janela)
            self.muda_fome(-3)
        else:
            janela.clear()
            janela.addstr(1, 1, 'Voce nao tem madeira o suficiente ou está com fome.')
    
    def colher(self, pos_y: int, pos_x: int, inventario: Inventario, bloco: Bloco, mapa: Mapa) -> None:
        
        if mapa.mapa[f'{pos_y},{pos_x}'] == 'X':
                bloco.colocar_bloco(pos_y, pos_x, 'Grama')
                inventario.adicionar_item('Bergamota', 1)


    def cortar(self, pos_y: int, pos_x: int, inventario: Inventario, bloco: Bloco, mapa: Mapa) -> None:
        aux_y = pos_y - 1
        aux_x = pos_x - 1

        for i in range (3):
            for j in range (3):
                if mapa.mapa[f'{aux_y+j},{aux_x+i}'] in ['O', '#']:
                    bloco.colocar_bloco(aux_y, aux_x, 'Grama', mapa)
                    inventario.adicionar_item('Madeira', 1)
                else:
                    pass