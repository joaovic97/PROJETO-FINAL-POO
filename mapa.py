import csv
import time
import random

class Mapa:
    def __init__(self) -> None:
        self.mapa = {}
        self.__arquivo = 'mapa.csv'

    # Cria mapa aleatório e salva no arquivo .csv
    def criar_mapa(self, max_y: int, max_x: int) -> None:
        random.seed(time.time())
        for j in range(max_y):
            for i in range(max_x):
                if random.randint(1, 100) <= 5:
                   self.mapa[f'{j},{i}'] = 'O'
                else:
                    self.mapa[f'{j},{i}'] = random.choice([',', ';', '~'])
        self.salvar_csv()

    # Aplica as muidanças no dict que armazena as informações do mapa e salva no .csv em seguida
    def atualizar_mapa(self, pos_y: int, pos_x: int, simbolo: str) -> None:
        self.mapa[f'{pos_y},{pos_x}'] = simbolo
        self.salvar_csv

    def salvar_csv(self) -> None:
        with open(self.__arquivo, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['y', 'x', 'Simbolo'])
            for coord in self.mapa:
                y, x = coord.split(',')
                writer.writerow([y, x, self.mapa[coord]])

    def carregar_csv(self) -> None:
        with open(self.__arquivo, mode='r') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                y, x, simbolo = row
                coord = ','.join(y, x)
                self.mapa[coord] = simbolo

    def limpar_csv(self) -> None:
        open(self.__arquivo, mode='w').close()