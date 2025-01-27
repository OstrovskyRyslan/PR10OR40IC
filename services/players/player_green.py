from services.players.base_player import PlayerBase 
class PlayerGreen(PlayerBase):
    def __init__(self, x, y, screen):
        super().__init__(x, y, (0, 255, 0), screen)  
