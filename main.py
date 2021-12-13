# Setup Python ----------------------------------------------- #
import pygame
import sys
import os
from settings import *
from game import Game
from menu import Menu




# Setup pygame/window --------------------------------------------- #
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (100,32) # windows position
pygame.init()
pygame.display.set_caption(WINDOW_NAME)
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT),0,32)

mainClock = pygame.time.Clock()

# Fonts ----------------------------------------------------------- #
fps_font = pygame.font.SysFont("coopbl", 22)

# Music ----------------------------------------------------------- #
#pygame.mixer.music.load("Assets/Sounds/Komiku_-_12_-_Bicycle.mp3")
#pygame.mixer.music.set_volume(MUSIC_VOLUME)
#pygame.mixer.music.play(-1)
# Variables ------------------------------------------------------- #
state = "menu"

# Creation -------------------------------------------------------- #
game = Game(SCREEN)
menu = Menu(SCREEN)



# Functions ------------------------------------------------------ #
def user_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()


def update():
    global state
    

    if state == "menu":
        aux = menu.update()
        
        if aux == "game1":
            game.reset_game1()
            state = "game1"
        
        elif aux == "game2":
            game.reset_game2()
            state = "game2"
        
        elif aux == "game3":
            game.reset_game3()
            state = "game3"
        
        elif aux == "game4":
            game.reset_game4()
            state = "game4"
    

    elif state == "game1":
        aux = game.update_game1()
        
        if aux == "menu":
            state = "menu"
        
        elif aux == "help_game1":
            game.reset_help_game1()
            state = "help_game1"
    

    elif state == "help_game1":
        aux = game.update_help_game1()
        if aux == "game1":
            game.reset_game1()
            state = "game1"
    

    elif state == "game2":
        aux = game.update_game2()
        
        if aux == "menu":
            state = "menu"
        
        elif aux == "help_game2":
            game.reset_help_game2()
            state = "help_game2"
    

    elif state == "help_game2":
        aux = game.update_help_game2()
        if aux == "game2":
            game.reset_game2()
            state = "game2"


    elif state == "game3":
        aux = game.update_game3()
        
        if aux == "menu":
            state = "menu"
        
        elif aux == "help_game3":
            game.reset_help_game3()
            state = "help_game3"
        
        elif aux == "game3":
            game.reset_game3()
            state = "game3"
    

    elif state == "help_game3":
        aux = game.update_help_game3()
        if aux == "game3":
            game.reset_game3()
            state = "game3" 

    
    elif state == "game4":
        aux = game.update_game4()
        
        if aux == "menu":
            state = "menu"
        
        elif aux == "help_game4":
            game.reset_help_game4()
            state = "help_game4"
        
        if aux == "game5":
            game.reset_game5()
            state = "game5"
    
    elif state == "help_game4":
        aux = game.update_help_game4()
        
        if aux == "game4":
            game.reset_game4()
            state = "game4" 


    elif state == "game5":
        aux = game.update_game5()
        
        if aux == "menu":
            state = "menu"
        
        elif aux == "help_game5":
            game.reset_help_game5()
            state = "help_game5"

        elif aux == "game4":
            game.reset_game4()
            state = "game4"
        
        elif aux == "game5":
            game.reset_game5()
            state = "game5"
    

    elif state == "help_game5":
        aux = game.update_help_game5()

        if aux == "game5":
            game.reset_game5()
            state = "game5" 
    
    

    
    
    
    
    
           
    
    
    pygame.display.update()
    mainClock.tick(FPS)



# Loop ------------------------------------------------------------ #
while True:

    # Buttons ----------------------------------------------------- #
    user_events()

    # Update ------------------------------------------------------ #
    update()

    # FPS
    if DRAW_FPS:
        fps_label = fps_font.render(f"FPS: {int(mainClock.get_fps())}", 1, (255,200,20))
        SCREEN.blit(fps_label, (5,5))
