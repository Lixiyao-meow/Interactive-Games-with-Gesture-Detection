import cv2
import mediapipe as mp
from settings import *
import numpy as np
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands



class HandTracking:
    def __init__(self):
        self.hand_tracking = mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5)
        self.left_hand_pos1 = (0,0)
        self.left_hand_pos2 = (0,0)
        self.right_hand_pos1 = (0,0)
        self.right_hand_pos2 = (0,0)
        self.results = None


    def scan_hands(self, image):
        rows, cols, _ = image.shape

        # Flip the image horizontally for a later selfie-view display, and convert
        # the BGR image to RGB.
        image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
        # To improve performance, optionally mark the image as not writeable to
        # pass by reference.
        image.flags.writeable = False
        self.results = self.hand_tracking.process(image)

        # Draw the hand annotations on the image.
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        if self.results.multi_hand_landmarks:
            for i in range (len(self.results.multi_hand_landmarks)):
                if self.results.multi_handedness[i].classification[0].label=="Right":
                    self.right_hand_pos1 = self.right_hand_pos2
                    self.right_hand_pos2 =(int(self.results.multi_hand_landmarks[i].landmark[8].x * SCREEN_WIDTH*3//2 - SCREEN_WIDTH//4),int(self.results.multi_hand_landmarks[i].landmark[8].y * SCREEN_HEIGHT*3//2 - SCREEN_HEIGHT//4))
                    mp_drawing.draw_landmarks(
                        image,
                        self.results.multi_hand_landmarks[i],
                        mp_hands.HAND_CONNECTIONS,
                        mp_drawing_styles.get_default_hand_landmarks_style(),
                        mp_drawing_styles.get_default_hand_connections_style())
                else :
                    self.left_hand_pos1 = self.left_hand_pos2
                    self.left_hand_pos2 = (int(self.results.multi_hand_landmarks[i].landmark[8].x * SCREEN_WIDTH*3//2 - SCREEN_WIDTH//4),int(self.results.multi_hand_landmarks[i].landmark[8].y * SCREEN_HEIGHT*3//2 - SCREEN_HEIGHT//4))
                    mp_drawing.draw_landmarks(
                        image,
                        self.results.multi_hand_landmarks[i],
                        mp_hands.HAND_CONNECTIONS,
                        mp_drawing_styles.get_default_hand_landmarks_style(),
                        mp_drawing_styles.get_default_hand_connections_style())
        return image

    def get_hand_center(self):
        return (self.hand_x, self.hand_y)


    def display_hand(self):
        cv2.imshow("image", self.image)
        cv2.waitKey(1)

    def is_hand_closed(self):

        pass


