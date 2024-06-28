class Animal():
    def __init__(self, especie: str, simbolo: str) -> None:
        self.__especie = especie
        self.__simbolo = simbolo
        self.pos_atual_x = 0
        self.pos_atual_y = 0

    # Getters

    def get_especie(self) -> str:
        return self.__especie

    def get_simbolo(self) -> str:
        return self.__simbolo

    def falar(self, mensagem:str) -> str:
        return f'{self.__especie}: {mensagem}'

    # Método para mover o animal para uma nova posição
    def andar(self, pos_y: int, pos_x: int) -> None:
        
        # Verifica se o destino é diferente da posição atual
        while self.pos_atual_x != pos_x or self.pos_atual_y != pos_y:
            
            # Move horizontalmente
            if self.pos_atual_x < pos_x:
                self.pos_atual_x += 1
            elif self.pos_atual_x > pos_x:
                self.pos_atual_x -= 1

            # Move verticalmente
            if self.pos_atual_y < pos_y:
                self.pos_atual_y += 1
            elif self.pos_atual_y > pos_y:
                self.pos_atual_y -= 1 