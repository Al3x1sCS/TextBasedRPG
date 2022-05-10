# Armas

class Arma:
    def __init__(self):
        raise NotImplementedError("Não crie um objeto novo, crie uma classe com herança")

    def __str__(self):
        return self.nome

class Faca(Arma):
    def __init__(self):
        self.nome = "Faca"
        self.descricao = "Uma faca cerrilhada meio amolada simples."
        self.dano = 10

class Pedra(Arma):
    def __init__(self):
        self.nome = "Pedra"
        self.descricao = "Uma pedra um pouco maior que uma bola de tenis, ideal para arremeçar."
        self.dano = 5

class Revolver38mm(Arma):
    def __init__(self):
        self.nome = "Revolver 38mm"
        self.descricao = "Um revolver relativamente antigo utilizado por alguns Polícias militares."
        self.dano = 50

class Espingarda(Arma):
    def __init__(self):
        self.nome = "Escopeta 12mm"
        self.descricao = "Uma espingarda calibre 12mm, normalmente usada por policiais militares."
        self.dano = 70

class Carabina(Arma):
    def __init__(self):
        self.nome = "Escopeta 12mm"
        self.descricao = "Carabina é uma arma de fogo mais curta que o fuzil, tendo entre 1,0 e 1,2 \n" \
                         "metro de comprimento muito usada em caça e tiro desportivo podendo ser de \n" \
                         "diversos calibres."
        self.dano = 5
        self.especial = "Pode ser acoplada uma lente de precisão a Carabina de até x8."

class Frigideira(Arma):
    def __init__(self):
        self.nome = "Frigideira"
        self.descricao = "Um utensílio usado na cozinha para fritar alimentos."
        self.dano = 7
        self.especial = "Faz um barulho engraçado quando bate na cabeça do inimigo."
