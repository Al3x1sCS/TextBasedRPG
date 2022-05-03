# Este jogo é uma aventura baseada em texto, que consiste em escapar de São Paulo.

def get_player_command():
    return input("Digite uma ação: ")


def play():
    print("Escape de São Paulo!")
    print('''Ações validas:
    Ir para o Norte [n ou N]
    Ir para o Sul   [s ou S]
    Ir para o Este  [e ou E]
    Ir para o Oeste [o ou O]
    Ver Inventário  [i ou I]
    Procurar na area [p ou P]\n''')

    action_input = get_player_command()
    inventory = [
        'Mochila',
        'Revolver 38mm',
        'Corda 10m',
        'Rações para viagem',
        'Cantil com agua',
        'Óculos quebrado'
    ]
    items = [
        'Balas de 38',
        'Comida estragada',
        'lente de óculos'
    ]

    if action_input in ["n", "N"]:
        print("Viajar para o Norte!")
    elif action_input in ['s', 'S']:
        print("Viajar para o Sul!")
    elif action_input in ['e', 'E']:
        print("Viajar para o Este!")
    elif action_input in ['o', 'O']:
        print("Viajar para o Oeste!")
    elif action_input in ['i', 'I']:
        print("Inventário:\n")
        print(inventory)
    elif action_input in ['p', 'P']:
        print("Itens encontrados:\n")
        print(items)
        # precisa terminar
        inventory.append('Balas de 38')
    else:
        print("Direção invalida! Digite uma direção valida. ")


play()
