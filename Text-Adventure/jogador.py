import itens
import mundo

class Jogador:
    def __init__(self):
        self.mochila = [
            itens.Pedra(),
            itens.Faca(),
            'Balas',
            'Kit-médico'
        ]
        self.x = 1
        self.y = 0

    def mover(self, coord_x, coord_y):
        self.x += coord_x
        self.y += coord_y

    def moverNorte(self):
        self.mover(coord_x=0, coord_y=-1)

    def moverSul(self):
        self.mover(coord_x=0, coord_y=1)

    def moverEste(self):
        self.mover(coord_x=1, coord_y=0)

    def moverOeste(self):
        self.mover(coord_x=-1, coord_y=0)


    def armaMaisPoderosa(self):
        danoMaximo = 0
        melhorArma = None
        for item in self.mochila:
            try:
                if danoMaximo < item.dano:
                    melhorArma = item
                    danoMaximo = item.dano

            except AttributeError:
                pass

        return melhorArma

    def verMochila(self):
        print("Mochila: ")
        for item in self.mochila:
            print("* " + str(item))
