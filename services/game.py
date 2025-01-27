import pygame
from services.players.player_green import PlayerGreen 
from services.players.player_red import PlayerRed 
from services.renderer import Renderer  
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Два плеера")
background = pygame.image.load(r'C:\Users\Ruslan Ostrovsky\Desktop\praktika\services\fon\fon.png')
background = pygame.transform.scale(background, (800, 600))  
green_player = PlayerGreen(100, 100, screen)
red_player = PlayerRed(200, 200, screen)
background_x = 0  
background_speed = 2  
screen_width = screen.get_width()
screen_height = screen.get_height()
running = True
while running:
    keys = pygame.key.get_pressed()  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    green_player.move(keys, pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d)
    red_player.move(keys, pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT)  # 
    if green_player.x < 0:
        green_player.x = 0
    elif green_player.x + 50 > screen_width:  
        green_player.x = screen_width - 50
    if red_player.x < 0:
        red_player.x = 0
    elif red_player.x + 50 > screen_width:  
        red_player.x = screen_width - 50
    if green_player.y < 0:
        green_player.y = 0
    elif green_player.y + 50 > screen_height: 
        green_player.y = screen_height - 50
    if red_player.y < 0:
        red_player.y = 0
    elif red_player.y + 50 > screen_height: 
        red_player.y = screen_height - 50
    if green_player.x > screen_width - 100 or red_player.x > screen_width - 100:
        background_x -= background_speed
    if green_player.x < 100 or red_player.x < 100:
        background_x += background_speed
    if background_x <= -screen_width:
        background_x = 0
    elif background_x >= 0:
        background_x = -screen_width
    screen.blit(background, (background_x, 0))  
    screen.blit(background, (background_x + screen_width, 0))  
    Renderer.render_all()  
    pygame.display.flip()
    pygame.time.Clock().tick(60)
pygame.quit()
