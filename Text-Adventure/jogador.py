import itens
import mundo
import inimigos


class Jogador:
    def __init__(self):
        self.mochila = [
            itens.Pedra(),
            itens.Faca(),
            'Balas',
            itens.KitMedico()
        ]
        self.x = 1
        self.y = 0
        self.vida = 100

    def verMochila(self):
        print("Mochila: ")
        for item in self.mochila:
            print("* " + str(item))

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

    def mover(self, coord_x, coord_y):
        self.x += coord_x
        self.y += coord_y

    def moverNorte(self):
        self.mover(coord_x=0, coord_y=-1)

    def moverSul(self):
        self.mover(coord_x=0, coord_y=1)

    def moverLeste(self):
        self.mover(coord_x=1, coord_y=0)

    def moverOeste(self):
        self.mover(coord_x=-1, coord_y=0)

    def ataque(self):
        melhorArma = self.armaMaisPoderosa()
        sala = mundo.blocoLocal(self.x, self.y)
        inimigo = sala.inimigo
        print("Voce usa o(a) {} contra o(a) {}".format(melhorArma, inimigo.nome))
        inimigo.vida -= melhorArma.dano
        if inimigo.morto():
            print("Você matou o(a) {}.".format(inimigo.nome))
        else:
            print("{} Vida: {}".format(inimigo.nome, inimigo.vida))

    def cura(self):
        consumivel = [item for item in self.mochila if isinstance(item, itens.Consumivel)]
        if not consumivel:
            print("Você não tem itens consumíveis para curar-se")
            return
        for i, item in enumerate(consumivel, 1):
            print("Escolha um item para cura: ")
            print("{}, {}".format(i, item))

        valido = False
        while not valido:
            escolha = input("")
            try:
                consumir = consumivel[int(escolha) -1]
                self.vida = min(100, self.vida + consumir.valorDeCura)
                self.mochila.remove(consumir)
                print("VIDA ATUAL: {}".format(self.vida))
                valido = True
            except (ValueError, IndexError):
                print("Escolha errada, tende de novo.")