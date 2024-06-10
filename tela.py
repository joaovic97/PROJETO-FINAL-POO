import curses
from curses import wrapper

#As dimensoes da tela do jogo foram pensadas para rodar no prompt de comando no meu notebook de 15,6"
#Para isso defini que Xmax=150 e Ymax=50

class Tela:



    def atualizar_mapa():
        pass

    def atualizar_lateral():
        pass


def main(stdscr):

    max_y, max_x = stdscr.getmaxyx()

    stdscr.clear()
    stdscr.refresh()

    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLUE)
    
    y, x = stdscr.getmaxyx()

    #Janela lateral que contera informacoes de status e inventario
    tela_status = curses.newwin(y, 30, 0, x-30)
    tela_status.clear()
    tela_status.border("|", "|", "-", "-", "*", "*", "*", "*")
    tela_status.addstr(1, 1, "João Pipi", curses.color_pair(1))
    tela_status.addstr(3, 1, "Vida:")
    tela_status.addstr(3, 27, "50")
    tela_status.addstr(4, 1, "Vigor:")
    tela_status.addstr(4, 27, "50")
    tela_status.addstr(5, 1, "Fome:")
    tela_status.addstr(5, 27, "50")
    tela_status.refresh()
    
    #Pad vai representar a visao do jogador
    tela_jogador = curses.newpad(50, 50)
    stdscr.refresh()
    for i in range(49):
        for j in range(26):
            char = chr(65+j)
            tela_jogador.addstr(char)
    
    tela_jogador.refresh(0, 0, 1, 1, 11, 11)

    stdscr.addstr(f"{x} e {y}")

    stdscr.getch()
    stdscr.clear()

wrapper(main)