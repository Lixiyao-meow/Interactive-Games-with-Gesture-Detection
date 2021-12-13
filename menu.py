import pygame
import sys
from settings import *
from background import Background
import ui


class Menu:
    def __init__(self, surface):
        self.surface = surface
        self.background = Background()


    def draw(self):
        self.background.draw(self.surface)
        # draw title
        ui.draw_text(self.surface, GAME_TITLE, (SCREEN_WIDTH//2, 120), COLORS["title"], font=FONTS["big"],
                    shadow=True, shadow_color=(255,255,255), pos_mode="center")


    def update(self):
        self.draw()
        if ui.button(self.surface, 175, "Drawing Canvas"):
            return "game1"
        if ui.button(self.surface, 275, "Kalimba"):
            return "game2"
        if ui.button(self.surface, 375, "Rock-Paper-Scissors 1"):
            return "game3"
        if ui.button(self.surface, 475, "Rock-Paper-Scissors 2"):
            return "game4"

        if ui.button(self.surface, 475+BUTTONS_SIZES[1]*1.5, "Quit"):
            pygame.quit()
            sys.exit()
