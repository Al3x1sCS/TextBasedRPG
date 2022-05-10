class Inimigos:
    def __init__(self):
        raise NotImplementedError("Crie uma classe não um objeto.")

    def __str__(self):
        return self.nome

    def vivo(self):
        return self.vida > 0

    def morto(self):
        return  self.vida <= 0


class Bandido(Inimigos):
    def __init__(self):
        self.nome = "Bandido"
        self.vida = 10
        self.dano = 10


class BandidoArmadurado(Inimigos):
    def __init__(self):
        self.nome = "Bandido armadurado."
        self.vida = 30
        self.dano = 10


class BandidoEmMotocicleta(Inimigos):
    def __init__(self):
        self.nome = "Um Bandido perigoso montado em uma motocicleta."
        self.vida = 100
        self.dano = 20


class LiderDeGange(Inimigos):
    def __init__(self):
        self.nome = "Um Bandido lider muito perigoso"
        self.vida = 100
        self.dano = 80
