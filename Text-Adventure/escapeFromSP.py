# Este jogo é uma aventura baseada em texto, que consiste em escapar de São Paulo.
from collections import OrderedDict
from jogador import Jogador
import mundo


def play():
    jogador = Jogador()
    # LOOP PRINCIPAL DO JOGO
    while True:
        sala = mundo.blocoLocal(jogador.x, jogador.y)
        print(sala.texto())
        sala.modificaJogador(jogador)
        escolhaJogador(sala, jogador)


def adicionarAcao(dicionarioAcoes, tecla, acao, nome):
    dicionarioAcoes[tecla.lower()] = acao
    dicionarioAcoes[tecla.upper()] = acao
    print("{}: {}".format(tecla, nome))

def pegarAcaoValida(sala, jogador):
    acao = OrderedDict()
    print("Escolha uma ação: ")
    if jogador.mochila:
        adicionarAcao(acao, 'i', jogador.verMochila, "Ver mochila")
    if isinstance(sala, mundo.BlocoInimigos) and sala.inimigo.vivo():
        adicionarAcao(acao, 'q', jogador.ataque, 'Ataque')
    if jogador.vida < 100:
        adicionarAcao(acao, 'c', jogador.cura, 'Curar-se')
    else:
        if mundo.blocoLocal(sala.x, sala.y - 1):
            adicionarAcao(acao, 'w', jogador.moverNorte, 'Viajando para o Norte')
        if mundo.blocoLocal(sala.x, sala.y + 1):
            adicionarAcao(acao, 's', jogador.moverSul, 'Viajando para o Sul')
        if mundo.blocoLocal(sala.x + 1, sala.y):
            adicionarAcao(acao, 'd', jogador.moverLeste, 'Viajando para o Leste')
        if mundo.blocoLocal(sala.x - 1, sala.y):
            adicionarAcao(acao, 'a', jogador.moverOeste(), 'Viajando para o Oeste')

    return acao

def escolhaJogador(sala, jogador):
    acao = None
    while not acao:
        acaoValida = pegarAcaoValida(sala, jogador)
        entrada = input("Ação: ")
        acao = acaoValida.get(entrada)
        if acao:
            acao()
        else:
            print("Ação invalida!")

play()
