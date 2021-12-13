import pygame
import time
import random
from settings import *
from background import Background
from hand import Hand
from hand_tracking import HandTracking
import cv2
import ui
import image
import numpy as np

class Game:
    def __init__(self, surface):
        self.surface = surface
        self.background = Background()

        # Load camera
        self.cap = cv2.VideoCapture(0)

        self.sounds = {}
        self.sounds["do1"] = pygame.mixer.Sound(f"Assets/Sounds/do1.mp3")
        self.sounds["do1"].set_volume(SOUNDS_VOLUME)
        self.sounds["re1"] = pygame.mixer.Sound(f"Assets/Sounds/re1.mp3")
        self.sounds["re1"].set_volume(SOUNDS_VOLUME)
        self.sounds["mi1"] = pygame.mixer.Sound(f"Assets/Sounds/mi1.mp3")
        self.sounds["mi1"].set_volume(SOUNDS_VOLUME)
        self.sounds["fa1"] = pygame.mixer.Sound(f"Assets/Sounds/fa1.mp3")
        self.sounds["fa1"].set_volume(SOUNDS_VOLUME)
        self.sounds["sol1"] = pygame.mixer.Sound(f"Assets/Sounds/sol1.mp3")
        self.sounds["sol1"].set_volume(SOUNDS_VOLUME)
        self.sounds["la1"] = pygame.mixer.Sound(f"Assets/Sounds/la1.mp3")
        self.sounds["la1"].set_volume(SOUNDS_VOLUME)
        self.sounds["si1"] = pygame.mixer.Sound(f"Assets/Sounds/si1.mp3")
        self.sounds["si1"].set_volume(SOUNDS_VOLUME)
        self.sounds["do2"] = pygame.mixer.Sound(f"Assets/Sounds/do2.mp3")
        self.sounds["do2"].set_volume(SOUNDS_VOLUME)
        self.sounds["re2"] = pygame.mixer.Sound(f"Assets/Sounds/re2.mp3")
        self.sounds["re2"].set_volume(SOUNDS_VOLUME)
        self.sounds["mi2"] = pygame.mixer.Sound(f"Assets/Sounds/mi2.mp3")
        self.sounds["mi2"].set_volume(SOUNDS_VOLUME)
        self.sounds["fa2"] = pygame.mixer.Sound(f"Assets/Sounds/fa2.mp3")
        self.sounds["fa2"].set_volume(SOUNDS_VOLUME)
        self.sounds["sol2"] = pygame.mixer.Sound(f"Assets/Sounds/sol2.mp3")
        self.sounds["sol2"].set_volume(SOUNDS_VOLUME)
        self.sounds["la2"] = pygame.mixer.Sound(f"Assets/Sounds/la2.mp3")
        self.sounds["la2"].set_volume(SOUNDS_VOLUME)
        self.sounds["si2"] = pygame.mixer.Sound(f"Assets/Sounds/si2.mp3")
        self.sounds["si2"].set_volume(SOUNDS_VOLUME)
        self.sounds["do3"] = pygame.mixer.Sound(f"Assets/Sounds/do3.mp3")
        self.sounds["do3"].set_volume(SOUNDS_VOLUME)
        self.sounds["re3"] = pygame.mixer.Sound(f"Assets/Sounds/re3.mp3")
        self.sounds["re3"].set_volume(SOUNDS_VOLUME)
        self.sounds["mi3"] = pygame.mixer.Sound(f"Assets/Sounds/mi3.mp3")
        self.sounds["mi3"].set_volume(SOUNDS_VOLUME)

        self.brush_right_status = "None"
        self.brush_left_status = "None"


        dsize = (400, 400)
        self.Overlayer = []
        self.Overlayer.append(image.load("Assets/rock.png", size=dsize, convert="default"))
        self.Overlayer.append(image.load("Assets/paper.png", size=dsize, convert="default"))
        self.Overlayer.append(image.load("Assets/scissors.png", size=dsize, convert="default"))
        self.Overlayer.append(image.load("Assets/nothing.png", size=dsize, convert="default"))

        self.start_time = time.time()
        self.time_count = time.time()
        self.player_choice = 3
        self.computer_choice = 3
        self.count = 0 #count turn
        self.c_win = 0 
        self.c_lose = 0

        self.H=[]
        self.S=[]
        self.V=[]

    def reset_game1(self): 
        for i in range (SCREEN_WIDTH):
            for j in range(SCREEN_HEIGHT):
                    self.background.image.set_at((i,j), (255,255,255))
        self.hand_tracking = HandTracking()
        self.hand = Hand()
        self.side = 0

    def update_game1(self):

        _, self.frame = self.cap.read()
        self.frame = self.hand_tracking.scan_hands(self.frame)

        self.background.draw(self.surface)

        if (self.hand_tracking.results.multi_hand_landmarks):
            for i in range (len(self.hand_tracking.results.multi_hand_landmarks)):
                if self.hand_tracking.results.multi_handedness[i].classification[0].label=="Right":
                    x1 = self.hand_tracking.right_hand_pos1[0]
                    y1 = self.hand_tracking.right_hand_pos1[1]
                    x2 = self.hand_tracking.right_hand_pos2[0]
                    y2 = self.hand_tracking.right_hand_pos2[1]
                    x3 = self.hand_tracking.results.multi_hand_landmarks[i].landmark[12].x
                    y3 = self.hand_tracking.results.multi_hand_landmarks[i].landmark[12].y
                    x4 = self.hand_tracking.results.multi_hand_landmarks[i].landmark[9].x
                    y4 = self.hand_tracking.results.multi_hand_landmarks[i].landmark[9].y
                    x5 = self.hand_tracking.results.multi_hand_landmarks[i].landmark[16].x
                    y5 = self.hand_tracking.results.multi_hand_landmarks[i].landmark[16].y
                    x6 = self.hand_tracking.results.multi_hand_landmarks[i].landmark[20].x
                    y6 = self.hand_tracking.results.multi_hand_landmarks[i].landmark[20].y
                    if y3 > y4:
                        if self.brush_right_status == "Draw" or self.brush_right_status == "Continue_Draw":
                            self.brush_right_status = "Continue_Draw"
                        else:
                            self.brush_right_status = "Draw"
                    elif y5<y4 and y6<y4:
                        if self.brush_right_status == "Eraser" or self.brush_right_status == "Continue_Eraser":
                            self.brush_right_status = "Continue_Eraser"
                        else:
                            self.brush_right_status = "Eraser"
                    else:
                        self.brush_right_status = "None"
                    if self.brush_right_status == "Draw":
                        image.draw(self.surface, self.hand.image_smaller_pen_right, self.hand_tracking.right_hand_pos2, pos_mode="down_left")
                        for k in range (-10,11):
                            for j in range(-10,11):
                                if (k**2+j**2<101):
                                    self.background.image.set_at((x2+k,y2+j), (0,0,0))
                    elif self.brush_right_status == "Continue_Draw":
                        image.draw(self.surface, self.hand.image_smaller_pen_right, self.hand_tracking.right_hand_pos2, pos_mode="down_left")
                        for k in range (-10,11):
                            for j in range(-10,11):
                                if (k**2+j**2<101):
                                    self.background.image.set_at((x2+k,y2+j), (0,0,0))
                        if x1<x2:
                            for la in range (x2-x1+1):
                                for j in range(-10,11):
                                    self.background.image.set_at((x1+la,la*y2//(x2-x1)+(x2-x1-la)*y1//(x2-x1)+j), (0,0,0))
                        elif x1>x2:
                            for la in range (x1-x2+1):
                                for j in range(-10,11):
                                    self.background.image.set_at((x2+la,la*y1//(x1-x2)+(x1-x2-la)*y2//(x1-x2)+j), (0,0,0))
                        if y1<y2:
                            for la in range (y2-y1+1):
                                for j in range(-10,11):
                                    self.background.image.set_at((la*x2//(y2-y1)+(y2-y1-la)*x1//(y2-y1)+j, y1+la), (0,0,0))
                        elif y1>y2:
                            for la in range (y1-y2+1):
                                for j in range(-10,11):
                                    self.background.image.set_at((la*x1//(y1-y2)+(y1-y2-la)*x2//(y1-y2)+j, y2+la), (0,0,0))
                    elif self.brush_right_status == "Eraser":
                        image.draw(self.surface, self.hand.orig_image_eraser_right, self.hand_tracking.right_hand_pos2, pos_mode="top_left")
                        for k in range (-50,51):
                            for j in range(-50,51):
                                if (k**2+j**2<2501):
                                    self.background.image.set_at((x2+k,y2+j), (255,255,255))
                    elif self.brush_right_status == "Continue_Eraser":  
                        image.draw(self.surface, self.hand.image_smaller_eraser_right, self.hand_tracking.right_hand_pos2, pos_mode="top_left")
                        for k in range (-50,51):
                            for j in range(-50,51):
                                if (k**2+j**2<2501):
                                    self.background.image.set_at((x2+k,y2+j), (255,255,255))
                        if x1<x2:
                            for la in range (x2-x1+1):
                                for j in range(-50,51):
                                    self.background.image.set_at((x1+la,la*y2//(x2-x1)+(x2-x1-la)*y1//(x2-x1)+j), (255,255,255))
                        elif x1>x2:
                            for la in range (x1-x2+1):
                                for j in range(-50,51):
                                    self.background.image.set_at((x2+la,la*y1//(x1-x2)+(x1-x2-la)*y2//(x1-x2)+j), (255,255,255))
                        if y1<y2:
                            for la in range (y2-y1+1):
                                for j in range(-50,51):
                                    self.background.image.set_at((la*x2//(y2-y1)+(y2-y1-la)*x1//(y2-y1)+j, y1+la), (255,255,255))
                        elif y1>y2:
                            for la in range (y1-y2+1):
                                for j in range(-50,51):
                                    self.background.image.set_at((la*x1//(y1-y2)+(y1-y2-la)*x2//(y1-y2)+j, y2+la), (255,255,255))
                    else :
                        image.draw(self.surface, self.hand.orig_image_pen_right, self.hand_tracking.right_hand_pos2, pos_mode="down_left")
                if self.hand_tracking.results.multi_handedness[i].classification[0].label=="Left":
                    x1 = self.hand_tracking.left_hand_pos1[0]
                    y1 = self.hand_tracking.left_hand_pos1[1]
                    x2 = self.hand_tracking.left_hand_pos2[0]
                    y2 = self.hand_tracking.left_hand_pos2[1]
                    x3 = self.hand_tracking.results.multi_hand_landmarks[i].landmark[12].x
                    y3 = self.hand_tracking.results.multi_hand_landmarks[i].landmark[12].y
                    x4 = self.hand_tracking.results.multi_hand_landmarks[i].landmark[9].x
                    y4 = self.hand_tracking.results.multi_hand_landmarks[i].landmark[9].y
                    x5 = self.hand_tracking.results.multi_hand_landmarks[i].landmark[16].x
                    y5 = self.hand_tracking.results.multi_hand_landmarks[i].landmark[16].y
                    x6 = self.hand_tracking.results.multi_hand_landmarks[i].landmark[20].x
                    y6 = self.hand_tracking.results.multi_hand_landmarks[i].landmark[20].y
                    if y3 > y4:
                        if self.brush_left_status == "Draw" or self.brush_left_status == "Continue_Draw":
                            self.brush_left_status = "Continue_Draw"
                        else:
                            self.brush_left_status = "Draw"
                    elif y5<y4 and y6<y4:
                        if self.brush_left_status == "Eraser" or self.brush_left_status == "Continue_Eraser":
                            self.brush_left_status = "Continue_Eraser"
                        else:
                            self.brush_left_status = "Eraser"
                    else:
                        self.brush_left_status = "None"
                    if self.brush_left_status == "Draw":
                        image.draw(self.surface, self.hand.image_smaller_pen_left, self.hand_tracking.left_hand_pos2, pos_mode="down_right")
                        for k in range (-10,11):
                            for j in range(-10,11):
                                if (k**2+j**2<101):
                                    self.background.image.set_at((x2+k,y2+j), (0,0,0))
                    elif self.brush_left_status == "Continue_Draw":
                        image.draw(self.surface, self.hand.image_smaller_pen_left, self.hand_tracking.left_hand_pos2, pos_mode="down_right")
                        for k in range (-10,11):
                            for j in range(-10,11):
                                if (k**2+j**2<101):
                                    self.background.image.set_at((x2+k,y2+j), (0,0,0))
                        if x1<x2:
                            for la in range (x2-x1+1):
                                for j in range(-10,11):
                                    self.background.image.set_at((x1+la,la*y2//(x2-x1)+(x2-x1-la)*y1//(x2-x1)+j), (0,0,0))
                        elif x1>x2:
                            for la in range (x1-x2+1):
                                for j in range(-10,11):
                                    self.background.image.set_at((x2+la,la*y1//(x1-x2)+(x1-x2-la)*y2//(x1-x2)+j), (0,0,0))
                        if y1<y2:
                            for la in range (y2-y1+1):
                                for j in range(-10,11):
                                    self.background.image.set_at((la*x2//(y2-y1)+(y2-y1-la)*x1//(y2-y1)+j, y1+la), (0,0,0))
                        elif y1>y2:
                            for la in range (y1-y2+1):
                                for j in range(-10,11):
                                    self.background.image.set_at((la*x1//(y1-y2)+(y1-y2-la)*x2//(y1-y2)+j, y2+la), (0,0,0))
                    elif self.brush_left_status == "Eraser":
                        image.draw(self.surface, self.hand.orig_image_eraser_left, self.hand_tracking.left_hand_pos2, pos_mode="top_right")
                        for k in range (-50,51):
                            for j in range(-50,51):
                                if (k**2+j**2<2501):
                                    self.background.image.set_at((x2+k,y2+j), (255,255,255))
                    elif self.brush_left_status == "Continue_Eraser":  
                        image.draw(self.surface, self.hand.image_smaller_eraser_left, self.hand_tracking.left_hand_pos2, pos_mode="top_right")
                        for k in range (-50,51):
                            for j in range(-50,51):
                                if (k**2+j**2<2501):
                                    self.background.image.set_at((x2+k,y2+j), (255,255,255))
                        if x1<x2:
                            for la in range (x2-x1+1):
                                for j in range(-50,51):
                                    self.background.image.set_at((x1+la,la*y2//(x2-x1)+(x2-x1-la)*y1//(x2-x1)+j), (255,255,255))
                        elif x1>x2:
                            for la in range (x1-x2+1):
                                for j in range(-50,51):
                                    self.background.image.set_at((x2+la,la*y1//(x1-x2)+(x1-x2-la)*y2//(x1-x2)+j), (255,255,255))
                        if y1<y2:
                            for la in range (y2-y1+1):
                                for j in range(-50,51):
                                    self.background.image.set_at((la*x2//(y2-y1)+(y2-y1-la)*x1//(y2-y1)+j, y1+la), (255,255,255))
                        elif y1>y2:
                            for la in range (y1-y2+1):
                                for j in range(-50,51):
                                    self.background.image.set_at((la*x1//(y1-y2)+(y1-y2-la)*x2//(y1-y2)+j, y2+la), (255,255,255))
                    else :
                        image.draw(self.surface, self.hand.orig_image_pen_left, self.hand_tracking.left_hand_pos2, pos_mode="down_right")
                    
        if ui.button(self.surface, 0, "Menu", pos_x = SCREEN_WIDTH-150, b_size = (150, 50)):
            return "menu"
        if ui.button(self.surface, 0, "Help", pos_x = 0, b_size = (150, 50)):
            return "help_game1"
        if ui.button(self.surface, SCREEN_HEIGHT-50, "Blank", pos_x = SCREEN_WIDTH-150, b_size = (150, 50)):
            for i in range (SCREEN_WIDTH):
                for j in range(SCREEN_HEIGHT):
                    self.background.image.set_at((i,j), (255,255,255))
         
        cv2.imshow("Frame", self.frame)
        cv2.waitKey(1)

    def reset_help_game1(self): 
        for i in range (SCREEN_WIDTH):
            for j in range(SCREEN_HEIGHT):
                    self.background.image.set_at((i,j), (0,0,0))

    def update_help_game1(self): 
        self.background.draw(self.surface)
        if ui.button(self.surface, 0, "<- Return", pos_x = 0, b_size = (250, 50)):
            return "game1"
        ui.draw_text(self.surface, "Use two fingers to point", (SCREEN_WIDTH//2,SCREEN_HEIGHT//2-100), (255,255,255), pos_mode = "center")
        ui.draw_text(self.surface, "Use one finger to draw", (SCREEN_WIDTH//2,SCREEN_HEIGHT//2), (255,255,255), pos_mode = "center")
        ui.draw_text(self.surface, "Open your hand to erase", (SCREEN_WIDTH//2,SCREEN_HEIGHT//2+100), (255,255,255), pos_mode = "center")

    def reset_game2(self): 
        self.background.image = image.load("Assets/kalimba.jpg", size=(SCREEN_WIDTH, SCREEN_HEIGHT),
                                convert="default")
        a1 = ((9/14-1/4)/(9/17))*(SCREEN_HEIGHT/SCREEN_WIDTH)
        b1 = (1/4)*SCREEN_HEIGHT
        a2 = ((1/4-4/7)/(1-9/17))*(SCREEN_HEIGHT/SCREEN_WIDTH)
        b2 = 1/4*SCREEN_HEIGHT-a2*SCREEN_WIDTH
        for x in range (SCREEN_WIDTH):
            for y in range (SCREEN_HEIGHT):
                is_above = (x<=9*SCREEN_WIDTH/17 and y<=a1*x+b1) or (x>9*SCREEN_WIDTH/17 and y<=a2*x+b2)
                if is_above:
                    aux = 2*abs(x*17//SCREEN_WIDTH-8)-(x*17//SCREEN_WIDTH<8)
                    self.background.image.set_at((x,y), (max(0,(aux-8)*255//8), 255-max(0,(aux-8)*255//8)-max(0,255-aux*255//8), max(0,255-aux*255//8)))

        self.hand_tracking = HandTracking()
        self.hand = Hand()
        self.side = 0
    
    def update_game2(self):

        _, self.frame = self.cap.read()
        self.frame = self.hand_tracking.scan_hands(self.frame)

        self.background.draw(self.surface)

        a1 = ((9/14-1/4)/(9/17))*(SCREEN_HEIGHT/SCREEN_WIDTH)
        b1 = (1/4)*SCREEN_HEIGHT
        a2 = ((1/4-4/7)/(1-9/17))*(SCREEN_HEIGHT/SCREEN_WIDTH)
        b2 = 1/4*SCREEN_HEIGHT-a2*SCREEN_WIDTH
        if (self.hand_tracking.results.multi_hand_landmarks):
            for i in range (len(self.hand_tracking.results.multi_hand_landmarks)):
                if self.hand_tracking.results.multi_handedness[i].classification[0].label=="Right":
                    x1 = self.hand_tracking.right_hand_pos1[0]
                    y1 = self.hand_tracking.right_hand_pos1[1]
                    is_above = ((x1>=0 and x1<=9*SCREEN_WIDTH/17 and y1<=a1*x1+b1) or (x1>9*SCREEN_WIDTH/17 and x1<SCREEN_WIDTH and y1<=a2*x1+b2))
                    x2 = self.hand_tracking.right_hand_pos2[0]
                    y2 = self.hand_tracking.right_hand_pos2[1]
                    is_below = ((x2>=0 and x2<=9*SCREEN_WIDTH/17 and y2>a1*x2+b1) or (x2>9*SCREEN_WIDTH/17 and x2<SCREEN_WIDTH and y2>a2*x2+b2))
                    if is_below:
                        image.draw(self.surface, self.hand.image_smaller_hand_right, self.hand_tracking.right_hand_pos2, pos_mode="top_left")
                    else:
                        image.draw(self.surface, self.hand.orig_image_hand_right, self.hand_tracking.right_hand_pos2, pos_mode="top_left")
                    if (is_above and is_below):
                        if x1*17//SCREEN_WIDTH==0:    
                            self.sounds["re3"].set_volume(SOUNDS_VOLUME)
                            self.sounds["re3"].play()
                        elif x1*17//SCREEN_WIDTH==1:
                            self.sounds["si2"].set_volume(SOUNDS_VOLUME)
                            self.sounds["si2"].play()
                        elif x1*17//SCREEN_WIDTH==2:
                            self.sounds["sol2"].set_volume(SOUNDS_VOLUME)
                            self.sounds["sol2"].play()
                        elif x1*17//SCREEN_WIDTH==3:
                            self.sounds["mi2"].set_volume(SOUNDS_VOLUME)
                            self.sounds["mi2"].play()
                        elif x1*17//SCREEN_WIDTH==4:
                            self.sounds["do2"].set_volume(SOUNDS_VOLUME)
                            self.sounds["do2"].play()
                        elif x1*17//SCREEN_WIDTH==5:
                            self.sounds["la1"].set_volume(SOUNDS_VOLUME)
                            self.sounds["la1"].play()
                        elif x1*17//SCREEN_WIDTH==6:
                            self.sounds["fa1"].set_volume(SOUNDS_VOLUME)
                            self.sounds["fa1"].play()
                        elif x1*17//SCREEN_WIDTH==7:
                            self.sounds["re1"].set_volume(SOUNDS_VOLUME)
                            self.sounds["re1"].play()
                        elif x1*17//SCREEN_WIDTH==8:
                            self.sounds["do1"].set_volume(SOUNDS_VOLUME)
                            self.sounds["do1"].play()
                        elif x1*17//SCREEN_WIDTH==9:
                            self.sounds["mi1"].set_volume(SOUNDS_VOLUME)
                            self.sounds["mi1"].play()
                        elif x1*17//SCREEN_WIDTH==10:
                            self.sounds["sol1"].set_volume(SOUNDS_VOLUME)
                            self.sounds["sol1"].play()
                        elif x1*17//SCREEN_WIDTH==11:
                            self.sounds["si1"].set_volume(SOUNDS_VOLUME)
                            self.sounds["si1"].play()
                        elif x1*17//SCREEN_WIDTH==12:
                            self.sounds["re2"].set_volume(SOUNDS_VOLUME)
                            self.sounds["re2"].play()
                        elif x1*17//SCREEN_WIDTH==13:
                            self.sounds["fa2"].set_volume(SOUNDS_VOLUME)
                            self.sounds["fa2"].play()
                        elif x1*17//SCREEN_WIDTH==14:
                            self.sounds["la2"].set_volume(SOUNDS_VOLUME)
                            self.sounds["la2"].play()
                        elif x1*17//SCREEN_WIDTH==15:
                            self.sounds["do3"].set_volume(SOUNDS_VOLUME)
                            self.sounds["do3"].play()
                        elif x1*17//SCREEN_WIDTH==16:
                            self.sounds["mi3"].set_volume(SOUNDS_VOLUME)
                            self.sounds["mi3"].play()
                if self.hand_tracking.results.multi_handedness[i].classification[0].label=="Left":
                    x1 = self.hand_tracking.left_hand_pos1[0]
                    y1 = self.hand_tracking.left_hand_pos1[1]
                    is_above = ((x1>=0 and x1<=9*SCREEN_WIDTH/17 and y1<=a1*x1+b1) or (x1>9*SCREEN_WIDTH/17 and x1<SCREEN_WIDTH and y1<=a2*x1+b2))
                    x2 = self.hand_tracking.left_hand_pos2[0]
                    y2 = self.hand_tracking.left_hand_pos2[1]
                    is_below = ((x2>=0 and x2<=9*SCREEN_WIDTH/17 and y2>a1*x2+b1) or (x2>9*SCREEN_WIDTH/17 and x2<SCREEN_WIDTH and y2>=a2*x2+b2))
                    if is_below:
                        image.draw(self.surface, self.hand.image_smaller_hand_left, self.hand_tracking.left_hand_pos2, pos_mode="top_right")
                    else:
                        image.draw(self.surface, self.hand.orig_image_hand_left, self.hand_tracking.left_hand_pos2, pos_mode="top_right")
                    if (is_above and is_below):
                        if x1*17//SCREEN_WIDTH==0:    
                            self.sounds["re3"].set_volume(SOUNDS_VOLUME)
                            self.sounds["re3"].play()
                        elif x1*17//SCREEN_WIDTH==1:
                            self.sounds["si2"].set_volume(SOUNDS_VOLUME)
                            self.sounds["si2"].play()
                        elif x1*17//SCREEN_WIDTH==2:
                            self.sounds["sol2"].set_volume(SOUNDS_VOLUME)
                            self.sounds["sol2"].play()
                        elif x1*17//SCREEN_WIDTH==3:
                            self.sounds["mi2"].set_volume(SOUNDS_VOLUME)
                            self.sounds["mi2"].play()
                        elif x1*17//SCREEN_WIDTH==4:
                            self.sounds["do2"].set_volume(SOUNDS_VOLUME)
                            self.sounds["do2"].play()
                        elif x1*17//SCREEN_WIDTH==5:
                            self.sounds["la1"].set_volume(SOUNDS_VOLUME)
                            self.sounds["la1"].play()
                        elif x1*17//SCREEN_WIDTH==6:
                            self.sounds["fa1"].set_volume(SOUNDS_VOLUME)
                            self.sounds["fa1"].play()
                        elif x1*17//SCREEN_WIDTH==7:
                            self.sounds["re1"].set_volume(SOUNDS_VOLUME)
                            self.sounds["re1"].play()
                        elif x1*17//SCREEN_WIDTH==8:
                            self.sounds["do1"].set_volume(SOUNDS_VOLUME)
                            self.sounds["do1"].play()
                        elif x1*17//SCREEN_WIDTH==9:
                            self.sounds["mi1"].set_volume(SOUNDS_VOLUME)
                            self.sounds["mi1"].play()
                        elif x1*17//SCREEN_WIDTH==10:
                            self.sounds["sol1"].set_volume(SOUNDS_VOLUME)
                            self.sounds["sol1"].play()
                        elif x1*17//SCREEN_WIDTH==11:
                            self.sounds["si1"].set_volume(SOUNDS_VOLUME)
                            self.sounds["si1"].play()
                        elif x1*17//SCREEN_WIDTH==12:
                            self.sounds["re2"].set_volume(SOUNDS_VOLUME)
                            self.sounds["re2"].play()
                        elif x1*17//SCREEN_WIDTH==13:
                            self.sounds["fa2"].set_volume(SOUNDS_VOLUME)
                            self.sounds["fa2"].play()
                        elif x1*17//SCREEN_WIDTH==14:
                            self.sounds["la2"].set_volume(SOUNDS_VOLUME)
                            self.sounds["la2"].play()
                        elif x1*17//SCREEN_WIDTH==15:
                            self.sounds["do3"].set_volume(SOUNDS_VOLUME)
                            self.sounds["do3"].play()
                        elif x1*17//SCREEN_WIDTH==16:
                            self.sounds["mi3"].set_volume(SOUNDS_VOLUME)
                            self.sounds["mi3"].play()
                    
        if ui.button(self.surface, 0, "Menu", pos_x = SCREEN_WIDTH-150, b_size = (150, 50)):
            return "menu"
        if ui.button(self.surface, 0, "Help", pos_x = 0, b_size = (150, 50)):
            return "help_game2"

        cv2.imshow("Frame", self.frame)
        cv2.waitKey(1)

    def reset_help_game2(self): 
        for i in range (SCREEN_WIDTH):
            for j in range(SCREEN_HEIGHT):
                    self.background.image.set_at((i,j), (0,0,0))
 
    def update_help_game2(self):  
        self.background.draw(self.surface)
        if ui.button(self.surface, 0, "<- Return", pos_x = 0, b_size = (250, 50)):
            return "game2"
        ui.draw_text(self.surface, "Use your indexes to play", (SCREEN_WIDTH//2,SCREEN_HEIGHT//2-100), (255,255,255), pos_mode = "center")
        ui.draw_text(self.surface, "To play, one index must go from", (SCREEN_WIDTH//2,SCREEN_HEIGHT//2), (255,255,255), pos_mode = "center")
        ui.draw_text(self.surface, "a touch to the bottom of the screen", (SCREEN_WIDTH//2,SCREEN_HEIGHT//2+100), (255,255,255), pos_mode = "center")

    def reset_game3(self): 
        for i in range (SCREEN_WIDTH):
            for j in range(SCREEN_HEIGHT):
                    self.background.image.set_at((i,j), (0,0,0))
        self.hand_tracking = HandTracking()
        self.hand = Hand()
        self.side = 0

        self.start_time = time.time()
        self.time_count = time.time()
        self.player_choice = 3
        self.computer_choice = 3
        self.count = 0 #count turn
        self.c_win = 0 
        self.c_lose = 0

    def update_game3(self):

        _, self.frame = self.cap.read()
        self.frame = self.hand_tracking.scan_hands(self.frame)

        self.background.draw(self.surface)

        ui.draw_text(self.surface, "Round "+str(self.count), (SCREEN_WIDTH//2,50), (255,255,255), pos_mode="center")
        if self.c_win==3:
            ui.draw_text(self.surface, "You win!!! :))))", (SCREEN_WIDTH//2-100, SCREEN_HEIGHT-100), (255,255,255), pos_mode="center")
            if ui.button(self.surface, SCREEN_HEIGHT-100, "Restart", pos_x = SCREEN_WIDTH//2+100, b_size = (200, 50)):
                return "game3"
        elif self.c_lose==3:
            ui.draw_text(self.surface, "You lose :(((", (SCREEN_WIDTH//2-100, SCREEN_HEIGHT-100), (255,255,255), pos_mode="center") 
            if ui.button(self.surface, SCREEN_HEIGHT-100, "Restart", pos_x = SCREEN_WIDTH//2+100, b_size = (200, 50)):
                return "game3" 
        
        ui.draw_text(self.surface, "Score:", (SCREEN_WIDTH//2, SCREEN_HEIGHT//2-50), (255,255,255),pos_mode="center")
        ui.draw_text(self.surface, str(self.c_win), (SCREEN_WIDTH//2-50, SCREEN_HEIGHT//2), (255,255,255),pos_mode="center")
        ui.draw_text(self.surface, "-", (SCREEN_WIDTH//2, SCREEN_HEIGHT//2), (255,255,255),pos_mode="center")
        ui.draw_text(self.surface, str(self.c_lose), (SCREEN_WIDTH//2+50, SCREEN_HEIGHT//2), (255,255,255),pos_mode="center")
        # count 3 2 1 before every turn
        if( time.time() - self.time_count < 1 and self.c_win<3 and self.c_lose<3):
            ui.draw_text(self.surface, "3", (SCREEN_WIDTH//2, 150), (255,255,255), pos_mode="center")
        elif(time.time() - self.time_count < 2 and self.c_win<3 and self.c_lose<3):
            ui.draw_text(self.surface, "2", (SCREEN_WIDTH//2, 150), (255,255,255), pos_mode="center")
        elif(time.time() - self.time_count < 3 and self.c_win<3 and self.c_lose<3):
            ui.draw_text(self.surface, "1", (SCREEN_WIDTH//2, 150), (255,255,255), pos_mode="center")
        elif( time.time() - self.time_count >= 3 and self.c_win<3 and self.c_lose<3): # Process every second
            self.computer_choice = random.randint(0,2) 
            self.player_choice = 3
            # 0:rock; 1:paper, 2:scissors
            if (self.hand_tracking.results.multi_hand_landmarks):
                x_orig = self.hand_tracking.results.multi_hand_landmarks[0].landmark[0].x
                y_orig = self.hand_tracking.results.multi_hand_landmarks[0].landmark[0].y
                x_base_index = self.hand_tracking.results.multi_hand_landmarks[0].landmark[6].x
                y_base_index = self.hand_tracking.results.multi_hand_landmarks[0].landmark[6].y
                x_tip_index = self.hand_tracking.results.multi_hand_landmarks[0].landmark[8].x
                y_tip_index = self.hand_tracking.results.multi_hand_landmarks[0].landmark[8].y
                x_base_middle = self.hand_tracking.results.multi_hand_landmarks[0].landmark[10].x
                y_base_middle = self.hand_tracking.results.multi_hand_landmarks[0].landmark[10].y
                x_tip_middle = self.hand_tracking.results.multi_hand_landmarks[0].landmark[12].x
                y_tip_middle = self.hand_tracking.results.multi_hand_landmarks[0].landmark[12].y
                x_base_ring = self.hand_tracking.results.multi_hand_landmarks[0].landmark[14].x
                y_base_ring = self.hand_tracking.results.multi_hand_landmarks[0].landmark[14].y
                x_tip_ring = self.hand_tracking.results.multi_hand_landmarks[0].landmark[16].x
                y_tip_ring = self.hand_tracking.results.multi_hand_landmarks[0].landmark[16].y
                x_base_little = self.hand_tracking.results.multi_hand_landmarks[0].landmark[18].x
                y_base_little = self.hand_tracking.results.multi_hand_landmarks[0].landmark[18].y
                x_tip_little = self.hand_tracking.results.multi_hand_landmarks[0].landmark[20].x
                y_tip_little = self.hand_tracking.results.multi_hand_landmarks[0].landmark[20].y

                firstOpen = ((x_orig-x_base_index)*(x_base_index-x_tip_index)+(y_orig-y_base_index)*(y_base_index-y_tip_index)>0)
                secondOpen = ((x_orig-x_base_middle)*(x_base_middle-x_tip_middle)+(y_orig-y_base_middle)*(y_base_middle-y_tip_middle)>0)
                thirdOpen = ((x_orig-x_base_ring)*(x_base_ring-x_tip_ring)+(y_orig-y_base_ring)*(y_base_ring-y_tip_ring)>0)
                fourthOpen = ((x_orig-x_base_little)*(x_base_little-x_tip_little)+(y_orig-y_base_little)*(y_base_little-y_tip_little)>0)  
                if not firstOpen and not secondOpen and not thirdOpen and not fourthOpen:
                    self.player_choice = 0
                    self.count += 1
                    if self.computer_choice == 1:
                        self.c_lose += 1
                    elif self.computer_choice == 2:
                        self.c_win += 1
                        
                elif firstOpen and secondOpen and thirdOpen and fourthOpen:
                    self.player_choice = 1
                    self.count += 1
                    if self.computer_choice == 0:
                        self.c_win += 1
                    elif self.computer_choice == 2:
                        self.c_lose += 1
                    
                elif firstOpen and secondOpen and not thirdOpen and not fourthOpen:
                    self.player_choice = 2
                    self.count += 1
                    if self.computer_choice == 0:
                        self.c_lose += 1
                    elif self.computer_choice == 1:
                        self.c_win += 1
                    
                else:
                    self.player_choice = 3
                    self.computer_choice = 3
            else:
                self.computer_choice = 3
            
            self.time_count = time.time()
        
        image.draw(self.surface, self.Overlayer[self.player_choice], (300,SCREEN_HEIGHT//2), pos_mode="center")
        image.draw(self.surface, self.Overlayer[self.computer_choice], (SCREEN_WIDTH - 300,SCREEN_HEIGHT//2), pos_mode="center")
        
        ui.draw_text(self.surface, "Player", (300,SCREEN_HEIGHT//2-250), (255,255,255), pos_mode = "center")
        ui.draw_text(self.surface, "Computer", (SCREEN_WIDTH - 300, SCREEN_HEIGHT//2-250), (255,255,255), pos_mode = "center")

        if ui.button(self.surface, 0, "Menu", pos_x = SCREEN_WIDTH-150, b_size = (150, 50)):
            return "menu"
        if ui.button(self.surface, 0, "Help", pos_x = 0, b_size = (150, 50)):
            return "help_game3"

        cv2.imshow("Frame", self.frame)
        cv2.waitKey(1)

    def reset_help_game3(self): 
        for i in range (SCREEN_WIDTH):
            for j in range(SCREEN_HEIGHT):
                    self.background.image.set_at((i,j), (0,0,0))
        
    def update_help_game3(self):   
        self.background.draw(self.surface)
        if ui.button(self.surface, 0, "<- Return", pos_x = 0, b_size = (250, 50)):
            return "game3"
        ui.draw_text(self.surface, "Play Rock-Paper-Scissor normally", (SCREEN_WIDTH//2,SCREEN_HEIGHT//2), (255,255,255), pos_mode = "center")    
      
    def reset_game4(self):
        for i in range (SCREEN_WIDTH):
            for j in range(SCREEN_HEIGHT):
                    self.background.image.set_at((i,j), (0,0,0))
        self.hand_tracking = HandTracking()
        self.hand = Hand()
        self.side = 0

        self.start_time = time.time()
        self.time_count = time.time()
        self.player_choice = 3
        self.computer_choice = 3
        self.count = 0 #count turn
        self.c_win = 0 
        self.c_lose = 0
        self.H=[]
        self.S=[]
        self.V=[]

    def update_game4(self):
        # left-click to take samples of hand's colour
        def mouseRGB(event, x, y, flags, param):
            if event == cv2.EVENT_LBUTTONDOWN: #checks mouse left button down condition
                frame2 = cv2.cvtColor(self.frame, cv2.COLOR_BGR2HSV)
                print(frame2[y,x,0], frame2[y,x,1], frame2[y,x,2])
                self.H.append(frame2[y,x,0])
                self.S.append(frame2[y,x,1])
                self.V.append(frame2[y,x,2])

        def skinmask(img):
            hsvim = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
            skinRegionHSV = cv2.inRange(hsvim, lower, upper)
            blurred = cv2.blur(skinRegionHSV, (2,2))
            ret, thresh = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY)
            return thresh

        # get the hand's contour
        def getcnthull(mask_img):
            contours, hierarchy = cv2.findContours(mask_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            contours = max(contours, key = lambda x: cv2.contourArea(x))
            hull = cv2.convexHull(contours)
            return contours, hull

        def getdefects(contours):
            hull = cv2.convexHull(contours, returnPoints=False)
            defects = cv2.convexityDefects(contours, hull)
            return defects

        '''
        This part will ask the user to click on their hand to get samples of their 
        hand's colour. The user will be advised to take colours from rock, paper and
        scissors gesture to optimize the colour samples.
        ​
        When enough samples have been taker, press "esc" to quit this part.
        '''
        
        _, self.frame = self.cap.read()
        self.background.draw(self.surface)

        self.background.draw(self.surface)

        self.frame = cv2.flip(self.frame,1) # Flip the image horizontally for a later selfie-view display
        cv2.namedWindow('Frame')
        cv2.setMouseCallback('Frame',mouseRGB)
        try:
            lower = np.array([np.percentile(self.H, 5),np.percentile(self.S, 5), np.percentile(self.V, 5)], dtype = "uint8")
            upper = np.array([np.percentile(self.H, 95),np.percentile(self.S, 95), np.percentile(self.V, 95)], dtype = "uint8")

            '''
            This part is to detect the hand's contour and the number of cavity. The 
            recognition of gesture depends only on the cavity number.
            ​
            We process the image every second for more stability.
            '''

            
            mask_img = skinmask(self.frame)
            contours, hull = getcnthull(mask_img)
            cv2.drawContours(self.frame, [contours], -1, (255,255,0), 2)
            cv2.drawContours(self.frame, [hull], -1, (0, 255, 255), 2)
            defects = getdefects(contours)
            
            if defects is not None:             
                cnt = 0 # count the cavity number 
                for i in range(defects.shape[0]):  # calculate the angle
                    s, e, f, d = defects[i][0]
                    start = tuple(contours[s][0])
                    end = tuple(contours[e][0])
                    far = tuple(contours[f][0])
                    a = np.sqrt((end[0] - start[0]) ** 2 + (end[1] - start[1]) ** 2)
                    b = np.sqrt((far[0] - start[0]) ** 2 + (far[1] - start[1]) ** 2)
                    c = np.sqrt((end[0] - far[0]) ** 2 + (end[1] - far[1]) ** 2)
                    angle = np.arccos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c))  #      cosine theorem
                    if angle <= np.pi / 4:  # angle less than 90 degree, treat as fingers
                        cnt += 1
                        cv2.circle(self.frame, far, 4, [0, 0, 255], -1)
                if cnt > 0:
                    cnt = cnt+1
                
                # detect the shape depending on hand's cavity number
                if cnt < 1:
                    gesture = "rock"
                    self.player_choice = 0
                elif cnt >=1 and cnt<3:
                    gesture = "scissors"
                    self.player_choice = 2
                elif cnt >=3:
                    gesture = "paper"
                    self.player_choice = 1
                
            cv2.putText(self.frame, str(cnt), (0, 50), cv2.FONT_HERSHEY_SIMPLEX,1, (255, 0, 0) , 2, cv2.LINE_AA)
            cv2.putText(self.frame, gesture, (0, 100), cv2.FONT_HERSHEY_SIMPLEX,1, (255, 0, 0) , 2, cv2.LINE_AA)
        except:
            pass

        
        ui.draw_text(self.surface, "Clic on different parts of your hand", (SCREEN_WIDTH//2,25), (255,255,255), pos_mode = "center")
        ui.draw_text(self.surface, "and in different positions until" , (SCREEN_WIDTH//2,75), (255,255,255), pos_mode = "center")
        ui.draw_text(self.surface, "computer choice is correct" , (SCREEN_WIDTH//2,125), (255,255,255), pos_mode = "center")
        image.draw(self.surface, self.Overlayer[self.player_choice], (SCREEN_WIDTH//2,SCREEN_HEIGHT//2), pos_mode="center")   
        if ui.button(self.surface, SCREEN_HEIGHT-50, "Reset", pos_x=SCREEN_WIDTH-150, b_size = (150, 50)):
            self.reset_game4()
        if ui.button(self.surface, SCREEN_HEIGHT-100, "Start", pos_x=SCREEN_WIDTH//2-75, b_size = (150, 50)):
            return "game5" 
        if ui.button(self.surface, 0, "Menu", pos_x = SCREEN_WIDTH-150, b_size = (150, 50)):
            return "menu"
        if ui.button(self.surface, 0, "Help", pos_x = 0, b_size = (150, 50)):
            return "help_game4"

        cv2.imshow("Frame", self.frame)
        cv2.waitKey(1)

    def reset_help_game4(self): 
            for i in range (SCREEN_WIDTH):
                for j in range(SCREEN_HEIGHT):
                        self.background.image.set_at((i,j), (0,0,0))

    def update_help_game4(self): 
        self.background.draw(self.surface)
        if ui.button(self.surface, 0, "<- Return", pos_x = 0, b_size = (250, 50)):
            return "game4"
        ui.draw_text(self.surface, "Clic on your hand until the white line", (SCREEN_WIDTH//2,SCREEN_HEIGHT//2-150), (255,255,255), pos_mode = "center")
        ui.draw_text(self.surface, "is a perfect contour of your hand", (SCREEN_WIDTH//2,SCREEN_HEIGHT//2-50), (255,255,255), pos_mode = "center")
        ui.draw_text(self.surface, "Try different position in order that the computer ", (SCREEN_WIDTH//2,SCREEN_HEIGHT//2+50), (255,255,255), pos_mode = "center")
        ui.draw_text(self.surface, "find the good item (Rock, Paper, or Scissor)", (SCREEN_WIDTH//2,SCREEN_HEIGHT//2+150), (255,255,255), pos_mode = "center")
        
    def reset_game5(self):
        for i in range (SCREEN_WIDTH):
            for j in range(SCREEN_HEIGHT):
                    self.background.image.set_at((i,j), (0,0,0))
        self.hand_tracking = HandTracking()
        self.hand = Hand()
        self.side = 0

        self.start_time = time.time()
        self.time_count = time.time()
        self.player_choice = 3
        self.computer_choice = 3
        self.count = 0 #count turn
        self.c_win = 0 
        self.c_lose = 0

    def update_game5(self):   
        # left-click to take samples of hand's colour
        def mouseRGB(event, x, y, flags, param):
            if event == cv2.EVENT_LBUTTONDOWN: #checks mouse left button down condition
                frame2 = cv2.cvtColor(self.frame, cv2.COLOR_BGR2HSV)
                print(frame2[y,x,0], frame2[y,x,1], frame2[y,x,2])
                self.H.append(frame2[y,x,0])
                self.S.append(frame2[y,x,1])
                self.V.append(frame2[y,x,2])

        def skinmask(img):
            hsvim = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
            skinRegionHSV = cv2.inRange(hsvim, lower, upper)
            blurred = cv2.blur(skinRegionHSV, (2,2))
            ret, thresh = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY)
            return thresh

        # get the hand's contour
        def getcnthull(mask_img):
            contours, hierarchy = cv2.findContours(mask_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            contours = max(contours, key = lambda x: cv2.contourArea(x))
            hull = cv2.convexHull(contours)
            return contours, hull

        def getdefects(contours):
            hull = cv2.convexHull(contours, returnPoints=False)
            defects = cv2.convexityDefects(contours, hull)
            return defects

        '''
        This part will ask the user to click on their hand to get samples of their 
        hand's colour. The user will be advised to take colours from rock, paper and
        scissors gesture to optimize the colour samples.
        ​
        When enough samples have been taker, press "esc" to quit this part.
        '''
        
        _, self.frame = self.cap.read()
        self.background.draw(self.surface)

        self.background.draw(self.surface)

        self.frame = cv2.flip(self.frame,1) # Flip the image horizontally for a later selfie-view display
        cv2.namedWindow('Frame')
        cv2.setMouseCallback('Frame',mouseRGB)
        try:
            lower = np.array([np.percentile(self.H, 5),np.percentile(self.S, 5), np.percentile(self.V, 5)], dtype = "uint8")
            upper = np.array([np.percentile(self.H, 95),np.percentile(self.S, 95), np.percentile(self.V, 95)], dtype = "uint8")

            '''
            This part is to detect the hand's contour and the number of cavity. The 
            recognition of gesture depends only on the cavity number.
            ​
            We process the image every second for more stability.
            ''' 
            mask_img = skinmask(self.frame)
            contours, hull = getcnthull(mask_img)
            cv2.drawContours(self.frame, [contours], -1, (255,255,0), 2)
            cv2.drawContours(self.frame, [hull], -1, (0, 255, 255), 2)
            defects = getdefects(contours)
            

            ui.draw_text(self.surface, "Round "+str(self.count), (SCREEN_WIDTH//2,100), (255,255,255), pos_mode="center")
            if self.c_win==3:
                ui.draw_text(self.surface, "You win!!! :))))", (SCREEN_WIDTH//2-100, SCREEN_HEIGHT-100), (255,255,255), pos_mode="center")
                if ui.button(self.surface, SCREEN_HEIGHT-100, "Restart", pos_x = SCREEN_WIDTH//2+100, b_size = (200, 50)):
                    return "game5"
            elif self.c_lose==3:
                ui.draw_text(self.surface, "You lose :(((", (SCREEN_WIDTH//2-100, SCREEN_HEIGHT-100), (255,255,255), pos_mode="center") 
                if ui.button(self.surface, SCREEN_HEIGHT-100, "Restart", pos_x = SCREEN_WIDTH//2+100, b_size = (200, 50)):
                    return "game5" 
            
            ui.draw_text(self.surface, "Score:", (SCREEN_WIDTH//2, SCREEN_HEIGHT//2-50), (255,255,255),pos_mode="center")
            ui.draw_text(self.surface, str(self.c_win), (SCREEN_WIDTH//2-50, SCREEN_HEIGHT//2), (255,255,255),pos_mode="center")
            ui.draw_text(self.surface, "-", (SCREEN_WIDTH//2, SCREEN_HEIGHT//2), (255,255,255),pos_mode="center")
            ui.draw_text(self.surface, str(self.c_lose), (SCREEN_WIDTH//2+50, SCREEN_HEIGHT//2), (255,255,255),pos_mode="center")
            # count 3 2 1 before every turn
            if( time.time() - self.time_count < 1 and self.c_win<3 and self.c_lose<3):
                ui.draw_text(self.surface, "3", (SCREEN_WIDTH//2, 150), (255,255,255), pos_mode="center")
            elif(time.time() - self.time_count < 2 and self.c_win<3 and self.c_lose<3):
                ui.draw_text(self.surface, "2", (SCREEN_WIDTH//2, 150), (255,255,255), pos_mode="center")
            elif(time.time() - self.time_count < 3 and self.c_win<3 and self.c_lose<3):
                ui.draw_text(self.surface, "1", (SCREEN_WIDTH//2, 150), (255,255,255), pos_mode="center")
            elif( time.time() - self.time_count >= 3 and self.c_win<3 and self.c_lose<3): # Process every second
                self.computer_choice = random.randint(0,2) 
                self.player_choice = 3
                if defects is not None:             
                    cnt = 0 # count the cavity number 
                    for i in range(defects.shape[0]):  # calculate the angle
                        s, e, f, d = defects[i][0]
                        start = tuple(contours[s][0])
                        end = tuple(contours[e][0])
                        far = tuple(contours[f][0])
                        a = np.sqrt((end[0] - start[0]) ** 2 + (end[1] - start[1]) ** 2)
                        b = np.sqrt((far[0] - start[0]) ** 2 + (far[1] - start[1]) ** 2)
                        c = np.sqrt((end[0] - far[0]) ** 2 + (end[1] - far[1]) ** 2)
                        angle = np.arccos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c))  #      cosine theorem
                        if angle <= np.pi / 4:  # angle less than 90 degree, treat as fingers
                            cnt += 1
                            cv2.circle(self.frame, far, 4, [0, 0, 255], -1)
                    if cnt > 0:
                        cnt = cnt+1
                    
                    # detect the shape depending on hand's cavity number
                    if cnt < 1:
                        gesture = "rock"
                        self.player_choice = 0
                    elif cnt >=1 and cnt<3:
                        gesture = "scissors"
                        self.player_choice = 2
                    elif cnt >=3:
                        gesture = "paper"
                        self.player_choice = 1
                    

                    if cnt < 1:
                        self.player_choice = 0
                        self.count += 1
                        if self.computer_choice == 1:
                            self.c_lose += 1
                        elif self.computer_choice == 2:
                            self.c_win += 1
                            
                    elif cnt >=3:
                        self.player_choice = 1
                        self.count += 1
                        if self.computer_choice == 0:
                            self.c_win += 1
                        elif self.computer_choice == 2:
                            self.c_lose += 1
                        
                    else:
                        self.player_choice = 2
                        self.count += 1
                        if self.computer_choice == 0:
                            self.c_lose += 1
                        elif self.computer_choice == 1:
                            self.c_win += 1
                else:
                    self.computer_choice = 3
            
                self.time_count = time.time()
        
            image.draw(self.surface, self.Overlayer[self.player_choice], (300,SCREEN_HEIGHT//2), pos_mode="center")
            image.draw(self.surface, self.Overlayer[self.computer_choice], (SCREEN_WIDTH - 300,SCREEN_HEIGHT//2), pos_mode="center")
            
            ui.draw_text(self.surface, "Player", (300,SCREEN_HEIGHT//2-250), (255,255,255), pos_mode = "center")
            ui.draw_text(self.surface, "Computer", (SCREEN_WIDTH - 300, SCREEN_HEIGHT//2-250), (255,255,255), pos_mode = "center")

            if ui.button(self.surface, 0, "Menu", pos_x = SCREEN_WIDTH-150, b_size = (150, 50)):
                return "menu"
            if ui.button(self.surface, 0, "Help", pos_x = 0, b_size = (150, 50)):
                return "help_game5"
            if ui.button(self.surface, 0, "Reset", pos_x = SCREEN_WIDTH//2-75, b_size = (150, 50)):
                return "game4"
                

            cv2.putText(self.frame, str(cnt), (0, 50), cv2.FONT_HERSHEY_SIMPLEX,1, (255, 0, 0) , 2, cv2.LINE_AA)
            cv2.putText(self.frame, gesture, (0, 100), cv2.FONT_HERSHEY_SIMPLEX,1, (255, 0, 0) , 2, cv2.LINE_AA)
        except:
            pass


        cv2.imshow("Frame", self.frame)
        cv2.waitKey(1)

    def reset_help_game5(self): 
            for i in range (SCREEN_WIDTH):
                for j in range(SCREEN_HEIGHT):
                        self.background.image.set_at((i,j), (0,0,0))

    def update_help_game5(self): 
        self.background.draw(self.surface)
        if ui.button(self.surface, 0, "<- Return", pos_x = 0, b_size = (250, 50)):
            return "game5"
        ui.draw_text(self.surface, "Play Rock-Paper-Scissor normally", (SCREEN_WIDTH//2,SCREEN_HEIGHT//2), (255,255,255), pos_mode = "center")    
      
