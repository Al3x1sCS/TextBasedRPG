# Este jogo é uma aventura baseada em texto, que consiste em escapar de São Paulo.

def get_player_command():
    return input("Digite uma direção: ")


def play():
    print("Escape de São Paulo!")
    print("Ações validas: Norte [n], Sul [s], Este [e], Oeste [o].")
    action_input = get_player_command()
    if action_input in ["n", "N"]:
        print("Indo para o Norte!")
    elif action_input in ['s', 'S']:
        print("Indo para o Sul!")
    elif action_input in ['e', 'E']:
        print("Indo para o Este!")
    elif action_input in ['o', 'O']:
        print("Indo para o Oeste!")
    else:
        print("Direção invalida! Digite uma direção valida. ")


play()
