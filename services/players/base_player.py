import pygame
from services.renderer import Renderer  
class PlayerBase:
    def __init__(self, x, y, color, screen):
        self.x = x
        self.y = y
        self.color = color
        self.screen = screen
        self.speed = 5  
        Renderer.add_object(self)  
    def move(self, keys, up, down, left, right):
        if keys[up]:
            self.y -= self.speed
        if keys[down]:
            self.y += self.speed
        if keys[left]:
            self.x -= self.speed
        if keys[right]:
            self.x += self.speed
    def draw_player(self):
        pygame.draw.rect(self.screen, self.color, (self.x, self.y, 50, 50))
