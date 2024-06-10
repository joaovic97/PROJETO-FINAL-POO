import curses
from curses import wrapper

#As dimensoes da tela do jogo foram pensadas para rodar no prompt de comando no meu notebook de 15,6"
#Para isso defini que Xmax=150 e Ymax=50


def main(stdscr):

    max_y, max_x = stdscr.getmaxyx()

    stdscr.clear()
    stdscr.refresh()

    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLUE)
    
    y, x = stdscr.getmaxyx()

    #Janela lateral que contera informacoes de status e inventario
    tela_status = curses.newwin(y, 30, 0, x-30)
    tela_status.clear()
    tela_status.addstr(0, 0, "Teste apenas", curses.color_pair(1))
    tela_status.refresh()
    
    #Pad vai representar a visao do jogador
    tela_jogador = curses.newpad(50, 50)
    stdscr.refresh()
    for i in range(20):
        for j in range(20):
            char = chr(65+j)
            tela_jogador.addstr(char)
    
    tela_jogador.refresh(0, 0, 1, 1, 11, 11)

    stdscr.addstr(f"{x} e {y}")

    stdscr.getch()
    stdscr.clear()

wrapper(main)