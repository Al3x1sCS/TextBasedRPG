import inimigos
import random


class Mundo:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def texto(self):
        raise NotImplementedError("Crie uma classe!")

    def modificaJogador(self, jogador):
        pass


class BlocoInicial(Mundo):
    def texto(self):
        return '''Escape de São Paulo!        
            A terra entrou no que parece ser uma terceira guerra-mundial.
        Satélites foram destruídos, a internet foi sabotada e os meios de
        comunicação silenciados.
            Ataques com bombas eletromagnéticas destruíram grande parte
        do país e deixaram os sobreviventes as cegas, sem comunicação, nem
        informações de qualquer tipo, espalhando o caos e destruição por
        toda cidade.
        
    Ações validas:    
    [W] Ir para o Norte  [S] Ir para o Sul  [D] Ir para o Leste
    [A] Ir para o Oeste  [I] Ver Mochila    [E] Ver melhor arma
    [C] Curar Feridas
        '''


class BlocoVazio(Mundo):
    def texto(self):
        return '''
        Este caminho está bloqueado.
        Você não pode ir por este lugar.
        '''


class BlocoPilhagem(Mundo):
    def texto(self):
        return '''
        Parece que este local tem itens valiosos.
        '''
        # Criar função para adicionar itens ao inventário


class BlocoInimigos(Mundo):
    def __init__(self, x, y):
        r = random.random()
        if r < 0.40:
            self.inimigo = inimigos.Bandido()
            self.textoVivo = '''
            Um bandido salta de trás de um carro quebrado e aponta uma faca afiada em sua direção.
            '''
            self.textoMorto = '''
            O corpo morto do bandido se encontra estendido no chão.
            '''
        elif r < 0.70:
            self.inimigo = inimigos.BandidoArmadurado()
            self.textoVivo = '''
            O que é isso?! Um bandido blindado apareceu do nada e vocês engajam em combate.
            '''
            self.textoMorto = '''
            Um bandido blindado morto faz você se lembrar da luta que teve
            contra a armadura resistente que você possui agora.
            '''
        elif r < 0.90:
            self.inimigo = inimigos.LiderDeGange()
            self.textoVivo = '''
            Um bandido incomum aparece na sua frente, ele parece ser perigoso e
            muito mais inteligente que os outros.
            '''
            self.textoMorto = '''
            Um bandido morto faz você se lembrar da luta trabalhosa que teve
            contra o lidar da gangue local.
            '''
        else:
            self.inimigo = inimigos.BandidoEmMotocicleta()
            self.textoVivo = '''
            Você ouve o que parece ser rosnados monstruosos, mas na verdade
            são os berros da gangue de motociclistas que o cercou.
            '''
            self.textoMorto = '''
            Vários motoqueiros mortos no chão, após a luta que aconteceu aqui.
            '''
        super().__init__(x, y)

    def texto(self):
        txt = self.textoVivo if self.inimigo.vivo() else self.textoMorto
        return txt

    def modificaJogador(self, jogador):
        if self.inimigo.vivo():
            jogador.vida = jogador.vida - self.inimigo.dano
            print("O inimigo deu {} de dano, você tem {} de vida.".format(self.inimigo.dano, jogador.vida))


class BlocoVitoria(Mundo):
    def texto(self):
        return '''
        Há um Helicóptero na distância...
        ...você consegue ouvi-lo quando chega perto, parece que é a sua saida desse lixo.
        
        a VITÓRIA foi obtida, você escapou de SP com sucesso!
        
        CONTINUA...
        '''


mapa = [
    [BlocoInimigos(0, 0), BlocoInicial(1, 0), BlocoInimigos(2, 0)],
    [BlocoInimigos(0, 1), BlocoVazio(1, 1), BlocoInimigos(2, 1)],
    [BlocoVazio(0, 2), BlocoPilhagem(1, 2), BlocoVazio(2, 2)],
    [BlocoInimigos(0, 3), BlocoVitoria(1, 3), BlocoInimigos(2, 3)]
]


def blocoLocal(x, y):
    if x < 0 or y < 0:
        return None
    try:
        return mapa[y][x]
    except IndexError:
        return None
