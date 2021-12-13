import pygame
import image
from settings import *
from hand_tracking import HandTracking
import cv2

class Hand:
    def __init__(self):
        self.orig_image_hand_right = image.load("Assets/right_hand.png", size=(HAND_SIZE, HAND_SIZE))
        self.image_smaller_hand_right = image.load("Assets/right_hand.png", size=(HAND_SIZE - 50, HAND_SIZE - 50))
        self.orig_image_hand_left = image.load("Assets/left_hand.png", size=(HAND_SIZE, HAND_SIZE))
        self.image_smaller_hand_left = image.load("Assets/left_hand.png", size=(HAND_SIZE - 50, HAND_SIZE - 50))
        self.orig_image_pen_right = image.load("Assets/right_pen.png", size=(HAND_SIZE, HAND_SIZE))
        self.image_smaller_pen_right = image.load("Assets/right_pen.png", size=(HAND_SIZE - 50, HAND_SIZE - 50))
        self.orig_image_pen_left = image.load("Assets/left_pen.png", size=(HAND_SIZE, HAND_SIZE))
        self.image_smaller_pen_left = image.load("Assets/left_pen.png", size=(HAND_SIZE - 50, HAND_SIZE - 50))
        self.orig_image_eraser_right = image.load("Assets/right_eraser.png", size=(HAND_SIZE, HAND_SIZE))
        self.image_smaller_eraser_right = image.load("Assets/right_eraser.png", size=(HAND_SIZE - 50, HAND_SIZE - 50))
        self.orig_image_eraser_left = image.load("Assets/left_eraser.png", size=(HAND_SIZE, HAND_SIZE))
        self.image_smaller_eraser_left = image.load("Assets/left_eraser.png", size=(HAND_SIZE - 50, HAND_SIZE - 50))

        


    def follow_mouse(self): # change the hand pos center at the mouse pos
        self.rect.center = pygame.mouse.get_pos()
        #self.hand_tracking.display_hand()

    def follow_mediapipe_hand(self, x, y):
        self.rect.center = (x, y)

    def draw_hitbox(self, surface):
        pygame.draw.rect(surface, (200, 60, 0), self.rect)


    def draw(self, surface):
        image.draw(surface, self.image, self.rect.center, pos_mode="top_left")

        if DRAW_HITBOX:
            self.draw_hitbox(surface)
