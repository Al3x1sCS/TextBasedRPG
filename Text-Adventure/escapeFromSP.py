# Este jogo é uma aventura baseada em texto, que consiste em escapar de São Paulo.
from player import Player
import world

def play():
    print("Escape from São Paulo!")
    print('''Ações validas:
    [n ou N] Ir para o Norte
    [s ou S] Ir para o Sul
    [e ou E] Ir para o Este
    [o ou O] Ir para o Oeste
    [i ou I] Ver Mochila
    [m ou M] Ver melhor arma
    \n''')
    player = Player()
    # GAME LOOP
    while True:
        room = world.tile_at(player.x, player.y)
        print(room.intro_text())
        action_input = get_player_command()

        if action_input in ["n", "N"]:
            print("Viajar para o Norte!")
            player.moverNorte()

        elif action_input in ['s', 'S']:
            print("Viajar para o Sul!")
            player.moverSul()
        elif action_input in ['e', 'E']:
            print("Viajar para o Este!")
            player.moverEste()
        elif action_input in ['o', 'O']:
            print("Viajar para o Oeste!")
            player.moverOeste()
        elif action_input in ['i', 'I']:
            print("Mochila:\n")
            player.print_mochila()
        elif action_input in ['m', 'M']:
            print(player.arma_mais_poderosa())
        else:
            print("Ação invalida! Digite uma direção valida. ")

def get_player_command():
    return input("Digite uma ação: ")

play()
