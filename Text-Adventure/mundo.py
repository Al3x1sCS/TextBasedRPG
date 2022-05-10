class Mundo:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def texto(self):
        raise NotImplementedError("Crie uma classe!")


class BlocoInicial(Mundo):
    def texto(self):
        return '''Escape de São Paulo!        
            A terra entrou no que parece ser uma terceira gerra-mundial.
        Satélites foram destruídos, a internet foi sabotada e os meios de
        comunicação silenciados.
            Ataques com bombas eletromagnéticas destruíram grande parte
        do país e deixaram os sobreviventes as cegas, sem comunicação, nem
        informações de qualquer tipo, espalhando o caos e destruição por
        toda cidade.
        
    Ações validas:    
    [W] Ir para o Norte  [S] Ir para o Sul  [D] Ir para o Este
    [A] Ir para o Oeste  [Q] Ver Mochila    [E] Ver melhor arma 
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


class BlocoVitoria(Mundo):
    def texto(self):
        return '''
        Há um Helicóptero na distância...
        ...você consegue ouvi-lo quando chega perto, parece que é a sua saida desse lixo.
        
        a VITÓRIA foi obtida, você escapou de SP com sucesso!
        
        CONTINUA...
        '''


mapa = [
    [None, BlocoInicial(1, 0), None],
    [None, BlocoVazio(1, 1), None],
    [BlocoVazio(0, 2), BlocoPilhagem(1, 2), BlocoVazio(2, 2)],
    [None, BlocoVitoria(1, 3), None]
]


def blocoLocal(x, y):
    if x < 0 or y < 0:
        return None
    try:
        return mapa[y][x]
    except IndexError:
        return None
