import mediapipe as mp
import cv2

class HandDetector:
    def __init__(self):
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(max_num_hands=2)
        self.mp_draw = mp.solutions.drawing_utils
        
    def find_hands(self, img, draw=True):
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(img_rgb)
        
        if self.results.multi_hand_landmarks and draw:
            for hand_landmarks in self.results.multi_hand_landmarks:
                self.mp_draw.draw_landmarks(
                    img, hand_landmarks, self.mp_hands.HAND_CONNECTIONS)
        return img
    
    def get_landmarks(self, img, hand_num=0):
        if self.results.multi_hand_landmarks:
            return self.results.multi_hand_landmarks[hand_num].landmark
        return None
    
    def count_fingers(self, landmarks):
        tip_ids = [4, 8, 12, 16, 20]  # MediaPipe finger landmarks
        fingers = 0
        
        # Thumb (right hand)
        if landmarks[tip_ids[0]].x < landmarks[tip_ids[0]-1].x:
            fingers += 1
            
        # Other fingers
        for i in range(1, 5):
            if landmarks[tip_ids[i]].y < landmarks[tip_ids[i]-2].y:
                fingers += 1
                
        return fingers
    
    def detect_operation(self, prev_landmarks, curr_landmarks):
        # Implement your operation detection logic here
        return None  # Replace with +, -, ×, ÷