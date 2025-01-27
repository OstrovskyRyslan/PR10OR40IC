from services.players.base_player import PlayerBase  
class PlayerRed(PlayerBase):
    def __init__(self, x, y, screen):
        super().__init__(x, y, (255, 0, 0), screen) 
