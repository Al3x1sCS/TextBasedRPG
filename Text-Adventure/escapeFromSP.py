# Este jogo é uma aventura baseada em texto, que consiste em escapar de São Paulo.


class Faca:
    def __int__(self):
        self.nome = "Faca"
        self.descricao = "Uma faca cerrilhada meio amolada simples."
        self.dano = 10
    def __str__(self):
        return self.nome

class Pedra:
    def __int__(self):
        self.nome = "Pedra"
        self.descricao = "Uma pedra um pouco maior que uma bola de tenis, ideal para arremeçar."
        self.dano = 5
    def __str__(self):
        return self.nome

class Espingarda:
    def __int__(self):
        self.nome = "Escopeta 12mm"
        self.descricao = "Uma espingarda calibre 12mm, normalmente usada por policiais militares."
        self.dano = 70
    def __str__(self):
        return self.nome

class Carabina:
    def __int__(self):
        self.nome = "Escopeta 12mm"
        self.descricao = "Carabina é uma arma de fogo mais curta que o fuzil, tendo entre 1,0 e 1,2 \n" \
                         "metro de comprimento muito usada em caça e tiro desportivo podendo ser de \n" \
                         "diversos calibres."
        self.dano = 5
        self.especial = "Pode ser acoplada uma lente de precisão a Carabina de até x8."
    def __str__(self):
        return self.nome

class Frigideira:
    def __int__(self):
        self.nome = "Frigideira"
        self.descricao = "Um utensílio usado na cozinha para fritar alimentos."
        self.dano = 7
        self.especial = "Faz um barulho engraçado quando bate na cabeça do inimigo."
    def __str__(self):
        return self.nome

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
        'lente de óculos',
        'Kit primeiros-socorros'
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
