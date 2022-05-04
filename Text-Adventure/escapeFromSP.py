# Este jogo é uma aventura baseada em texto, que consiste em escapar de São Paulo.
# A terra entrou no que parece uma terceira gerra-mundial.
# Satelites foram destruidos, a internet foi sabotada, os meios de comunicação silenciados.
# Ataques com bombas eletromagneticas destruiram grande parte do pais e deixaram os sobreviventes as cegas.
# Sem comunicação, nem informações de qualquer tipo, espalhando o caos e destruição por toda cidade.
# Você se encontra no centro de São Paulo, em um dos predios ao redor da Igreja da Consolação.
# O panorama se encontra irreconhecível, você mal acredita que o predio está em pé.
# Os gritos nas ruas se tornaram parte do som ambiente, onde antes eram passaros.
# É possivel enchergar predios com chamas que permanecem eternas.
# Você está sobrevivendo a varias semanas com comida estocada, nada mudou,
# nenhuma ajuda veio, nem sinal dos militares.
# militares esses que desfilaram na Praça, exibindo suas tropas, armamentos e tankes de jatos d'água,
# que mais pareciam ser feitos para controlar a população em caso de uma guerra civil, do que na propria guerra.
#




def get_player_command():
    return input("Digite uma ação: ")


def play():
    print("Escape from São Paulo!")
    print('''Ações validas:
    Ir para o Norte [n ou N]
    Ir para o Sul   [s ou S]
    Ir para o Este  [e ou E]
    Ir para o Oeste [o ou O]
    Ver Inventário  [i ou I]
    Procurar na area [b ou B]\n''')

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
        'Balas 38mm',
        'Comida estragada',
        'lente de óculos'
    ]
# MARK: GAME LOOP
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
    elif action_input in ['b', 'B']:
        print("Basculhando a área...\n\n")
        print("Itens encontrados:\n")
        print(items)
        for i in items:
            inventory.append(i)
    else:
        print("Ação invalida! Digite uma direção valida. ")


play()
