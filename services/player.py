class Player:
    def __init__(self, pygame, screen, color, x, y, move_keys):
        self.pygame = pygame
        self.screen = screen
        self.color = color
        self.x = x
        self.y = y
        self.move_keys = move_keys
        self.speed = 5
    def move_left(self):
        self.x -= self.speed
    def move_right(self):
        self.x += self.speed
    def move_up(self):
        self.y -= self.speed
    def move_down(self):
        self.y += self.speed
    def move(self):
        keys = self.pygame.key.get_pressed()
        if keys[self.move_keys["left"]]:
            self.move_left()
        if keys[self.move_keys["right"]]:
            self.move_right()
        if keys[self.move_keys["up"]]:
            self.move_up()
        if keys[self.move_keys["down"]]:
            self.move_down()
    def draw_player(self):
        self.pygame.draw.rect(self.screen, self.color, (self.x, self.y, 50, 50))
