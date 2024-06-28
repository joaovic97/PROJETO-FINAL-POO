import csv

class Inventario():
    def __init__(self):
        
        # Dicionário para armazenar itens com o nome do item como chave
        self.itens = {
            'Madeira': 20,
            'Semente': 10,
            'Bergamota': 30
        }
        self.__arquivo = 'inventario.csv'

    def adicionar_item(self, nome: str, quantidade: int) -> None:
        if nome in self.itens:
            self.itens[nome] += quantidade
        else:
            self.itens[nome] = quantidade
        self.salvar_inventario()

    def remover_item(self, nome: str, quantidade: int, janela) -> None:
        if nome in self.itens:
            if quantidade > self.itens[nome]:
                janela.clear()
                janela.addstr(1, 1, 'GM: Voce nao tem itens suficiente.')
            else:
                self.itens[nome] -= quantidade
        self.salvar_inventario()

    def tem_item(self, nome: str) -> bool:
        if self.itens[nome] > 0:
            return True
        else:
            return False

    def salvar_inventario(self) -> None:
        with open(self.__arquivo, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Item", "Total"])
            for i in self.itens:
                writer.writerow([i, self.itens[i]])

    def carregar_inventario(self) -> None:
        with open(self.__arquivo, mode='r') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                nome, total = row
                self.adicionar_item(nome, total)

    def limpar_inventario(self) -> None:
        self.itens.clear()

    def limpar_csv(self) -> None:
        open(self.arquivo, mode='w').close()