import items

class Player:
    def __init__(self):
        self.mochila = [
            items.Pedra(),
            items.Faca(),
            'Balas',
            'Kit-médico'
        ]

    def print_mochila(self):
        print("Mochila: ")
        for item in self.mochila:
            print("* " + str(item))
        melhor_arma = self.arma_mais_poderosa()
        print("Sua melhor arma é a {} ".format(melhor_arma))

    def arma_mais_poderosa(self):
        dano_maximo = 0
        melhor_arma = None
        for item in self.mochila:
            try:
                if dano_maximo < item.dano:
                    melhor_arma = item
                    dano_maximo = item.dano

            except AttributeError:
                pass

        return melhor_arma
