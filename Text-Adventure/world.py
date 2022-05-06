class MapTile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def intro_text(self):
        raise NotImplementedError("Crie uma classe!")


class StartTile(MapTile):
    def intro_text(self):
        return '''
            A terra entrou no que parece ser uma terceira gerra-mundial.
        Satélites foram destruídos, a internet foi sabotada e os meios de
        comunicação silenciados.
            Ataques com bombas eletromagnéticas destruíram grande parte
        do país e deixaram os sobreviventes as cegas, sem comunicação, nem
        informações de qualquer tipo, espalhando o caos e destruição por
        toda cidade.\n
        '''


class EmptyTile(MapTile):
    def intro_text(self):
        return '''
        Este caminho está bloqueado.
        Você não pode ir por este lugar.
        '''


class LootTile(MapTile):
    def intro_text(self):
        return '''
        Parece que este local tem itens valiosos.
        '''
        # Criar função para adicionar itens ao inventário


class VictoryTile(MapTile):
    def intro_text(self):
        return '''
        Há um Helicóptero na distância...
        ...você consegue ouvi-lo quando chega perto, parece que é a sua saida desse lixo.
        
        a VITÓRIA foi obtida, você escapou de SP com sucesso!
        
        CONTINUA...
        '''


mapa_do_mundo = [
    [None, VictoryTile(1, 0), None],
    [None, EmptyTile(1, 1), None],
    [EmptyTile(0, 2), StartTile(1, 2), EmptyTile(2, 2)],
    [None, EmptyTile(1, 3), None]
]


def tile_at(x, y):
    if x < 0 or y < 0:
        return None

        try:
            return mapa_do_mundo[y][x]
        except IndexError:
            return None
