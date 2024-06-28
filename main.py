#main com todo o código da tela no main
import curses
from curses import wrapper
from art import text2art
from jogador import Jogador
from inventario import Inventario
from blocos import Bloco
from mapa import Mapa
from animal import Animal

def tela_jogo(stdscr):

    k = 0 # Variável que armazena a última tecla pressionada
    max_y, max_x = stdscr.getmaxyx() # Dimensões da tela
    mapa_y = max_y - 10 # Dimensões do mapa
    mapa_x = max_x - 31
    jogador_y = int(mapa_y / 2) # Posição y do cursor
    jogador_x = int(mapa_x / 2) # Posição x do cursor
    y_inventario = int(max_y*0.4) # Definição do tamanho do inventário em relação à janela

    mapa = Mapa()

    stdscr.clear()
    stdscr.refresh()

    # Definicao de cores presentes no jogo
    # Primeira cor: fonte, segunda cor: fundo

    curses.start_color()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_WHITE)
    curses.init_pair(4, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(5, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
    curses.init_pair(6, curses.COLOR_CYAN, curses.COLOR_BLACK)

    curses.curs_set(0) # Deixa o cursor invisível
    curses.noecho() # Impede que as teclas apertadas sejam impressas na tela
    # stdscr.nodelay(1) # Faz com que o refresh não dependa de apertar alguma tecla mas faz a tela apresentar ruídos

    while True:

        stdscr.keypad(True) # Habilita a interpretação pelo curses de outras teclas para além das de caracteres 
        stdscr.clear()

        jogador = Jogador('Jogador')
        inventario = Inventario()
        bloco = Bloco()
        rato = Animal('Rato', 'r')
        gato = Animal('Gato', 'g')
        cachorro = Animal('Cachorro', 'c')

        # Arte do menu inicial
        art = text2art('''    
                    
                    Projeto Final
                                
                                POO   ''', font='3-d')
        curses.curs_set(0)
        stdscr.addstr(art, curses.color_pair(1)) # Escreve o texto nas coordenadas passadas por parâmetro
        stdscr.addstr(45, 70, 'Enter', curses.color_pair(6))
        stdscr.addstr(45, 77, 'Novo Jogo')
        stdscr.addstr(47, 70, 'Esc', curses.color_pair(6))
        stdscr.addstr(47, 77, 'Sair')
        stdscr.border() # Desenha uma borda na janela
        stdscr.refresh() # Atualiza a tela e aplica todas as modificações feitas até essa linha

        if k == 10: # Tecla Enter

            mapa.criar_mapa(max_y, max_x)

            while k != 8: # Tecla Backspace
                
                curses.curs_set(0)

                # Código do movimento do jogador
                new_y, new_x = jogador_y, jogador_x

                if k == curses.KEY_DOWN:
                    new_y = jogador_y + 1
                elif k == curses.KEY_UP:
                    new_y = jogador_y - 1
                elif k == curses.KEY_RIGHT:
                    new_x = jogador_x + 1
                elif k == curses.KEY_LEFT:
                    new_x = jogador_x - 1

                # Código que verifica se o jogador pode pisar no bloco que está na direção que ele deseja andar    
                new_x = max(1, min(mapa_x - 1, new_x))
                new_y = max(1, min(mapa_y - 1, new_y))

                if f'{new_y},{new_x}' in mapa.mapa and mapa.mapa[f'{new_y},{new_x}'] not in ['#', 'O']:
                    jogador_y, jogador_x = new_y, new_x

                for i in range (mapa_x):
                    for j in range (mapa_y):
                        if mapa.mapa[f'{j},{i}'] in bloco.blocos['Grama']:
                            stdscr.addstr(j, i, mapa.mapa[f'{j},{i}'], curses.color_pair(1))
                        elif mapa.mapa[f'{j},{i}'] == bloco.blocos['Arvore']:
                            stdscr.addstr(j, i, mapa.mapa[f'{j},{i}'], curses.color_pair(5))
                        elif mapa.mapa[f'{j},{i}'] == bloco.blocos['Madeira']:
                            stdscr.addstr(j, i, mapa.mapa[f'{j},{i}'], curses.color_pair(3))
                        elif mapa.mapa[f'{j},{i}'] == bloco.blocos['Semente']:
                            stdscr.addstr(j, i, mapa.mapa[f'{j},{i}'], curses.color_pair(4))
                        elif mapa.mapa[f'{j},{i}'] == bloco.blocos['Bergamota']:
                            stdscr.addstr(j, i, mapa.mapa[f'{j},{i}'], curses.color_pair(4))
                
                stdscr.addstr(jogador_y, jogador_x, jogador.get_simbolo())
                stdscr.border()
                
                # Mostra informações sobre o jogador no topo da janela
                stdscr.addstr(0, 1, f' {jogador.get_nome()} | Vigor: {jogador.get_vigor()} | Fome: {jogador.get_fome()}')
                stdscr.addstr(0, mapa_x - 11, f'y: {jogador_y}, x:{jogador_x}')
                stdscr.refresh()

                # Daqui para baixo o código diz respeito às janelas de informação

                # Cria janela inferior para log de mensagens
                janela_log = curses.newwin(max_y - mapa_y, mapa_x, mapa_y, 0)
                janela_log.border()
                janela_log.refresh()
                
                # Cria janela lateral com informações de comando e inventário
                janela_info = curses.newwin(max_y, max_x - mapa_x, 0, mapa_x )
                janela_info.border()
                janela_info.addstr(1, 1, 'p', curses.color_pair(6))
                janela_info.addstr(1, 7, 'Plantar Semente')
                janela_info.addstr(2, 1, 'c', curses.color_pair(6))
                janela_info.addstr(2, 7, 'Cortar Arvore')
                janela_info.addstr(3, 1, 'b', curses.color_pair(6))
                janela_info.addstr(3, 7, 'Construir Casa')
                janela_info.addstr(4, 1, 'h', curses.color_pair(6))
                janela_info.addstr(4, 7, 'Colher Plantacao')
                janela_info.addstr(5, 1, 'e', curses.color_pair(6))
                janela_info.addstr(5, 7, 'Comer')
                janela_info.addstr(5, 1, 's', curses.color_pair(6))
                janela_info.addstr(5, 7, 'Salvar')
                janela_info.addstr(6, 1, 'Bksp', curses.color_pair(6))
                janela_info.addstr(6, 7, 'Sair')

                linha = y_inventario 
                janela_info.addstr(y_inventario - 2, 1, 'Inventario:')
                for item, quantidade in inventario.itens.items():
                    janela_info.addstr(linha, 1, f'x{quantidade}')
                    janela_info.addstr(linha, 5, f'{item}')
                    linha += 1

                janela_info.refresh()

                # Realiza funções a partir das teclas pressionadas
                if k == ord('p') or k == ord('P'):
                    jogador.plantar(jogador_y, jogador_x, inventario, bloco, mapa, janela_log)

                if k == ord('b') or k == ord('B'):
                    jogador.construir(jogador_y, jogador_x, inventario, bloco, mapa, janela_log)

                if k == ord('c') or k == ord('C'):
                    jogador.cortar(jogador_y, jogador_x, inventario, bloco, mapa)
                    
                if k == ord('h') or k == ord('H'):
                    jogador.colher(jogador_y, jogador_x, inventario, bloco, mapa)

                if k == ord('e') or k == ord('E'):
                    jogador.comer(inventario, janela_log)

                k = stdscr.getch()

        elif k == 27: # Tecla Esc
            break

        k = stdscr.getch()

def main():
    curses.wrapper(tela_jogo) # Função que vai manipular a tela sendo passada como parâmetro

if __name__ == "__main__":
    main()