import cv2
import mediapipe as mp
import numpy as np

def get_finger_states(hand_landmarks, hand_label):
    """
    Analyzes hand landmarks to determine the state (0 or 1) for each of the 5 fingers.
    Returns a list of 5 states [thumb, index, middle, ring, pinky].
    """
    states = []
    if hand_landmarks is None:
        return [0] * 5
        
    lm = hand_landmarks.landmark

    # Landmark indices for tips and PIP joints
    tip_ids = [4, 8, 12, 16, 20]
    pip_ids = [3, 6, 10, 14, 18] # Proximal Interphalangeal joints

    # 1. Thumb Logic
    # We check if the thumb tip's x-coordinate is to the right (left hand)
    # or left (right hand) of the IP joint's x-coordinate.
    # This detects the thumb moving horizontally outwards.
    try:
        if hand_label == 'Left':
            if lm[tip_ids[0]].x > lm[pip_ids[0]].x:
                states.append(1) # Open
            else:
                states.append(0) # Closed
        elif hand_label == 'Right':
            if lm[tip_ids[0]].x < lm[pip_ids[0]].x:
                states.append(1) # Open
            else:
                states.append(0) # Closed

        # 2. Four Fingers Logic
        # We check if the tip's y-coordinate is *above* (smaller) than the PIP joint's y-coordinate.
        # (0,0) is at the top-left corner.
        for i in range(1, 5): # For index, middle, ring, pinky
            if lm[tip_ids[i]].y < lm[pip_ids[i]].y:
                states.append(1) # Open
            else:
                states.append(0) # Closed
    
    except Exception as e:
        print(f"Error in finger state detection: {e}")
        return [0] * 5
            
    return states