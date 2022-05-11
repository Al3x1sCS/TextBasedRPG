# Este jogo é uma aventura baseada em texto, que consiste em escapar de São Paulo.
from jogador import Jogador
import mundo

def comandoJogador():
    return input("Digite uma ação: ")

def play():
    jogador = Jogador()
    # LOOP PRINCIPAL DO JOGO
    while True:
        sala = mundo.blocoLocal(jogador.x, jogador.y)
        print(sala.texto())
        acao = comandoJogador()
        sala.modificaJogador(jogador)


        if acao in ["w", "W"]:
            print("Viajar para o Norte!")
            jogador.moverNorte()
        elif acao in ['s', 'S']:
            print("Viajar para o Sul!")
            jogador.moverSul()
        elif acao in ['d', 'D']:
            print("Viajar para o Leste!")
            jogador.moverEste()
        elif acao in ['a', 'A']:
            print("Viajar para o Oeste!")
            jogador.moverOeste()
        elif acao in ['i', 'I']:
            print("Mochila:\n")
            jogador.verMochila()
        elif acao in ['e', 'E']:
            print("Sua melhor arma é a {} ".format(jogador.armaMaisPoderosa()))
        elif acao in ['q', 'Q']:
            jogador.ataque()
        else:
            print("Ação invalida! Digite uma direção valida. ")

play()
