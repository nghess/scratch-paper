import numpy as np
import random
import cv2

stick = 1001
height = 100
width = stick
direction = [-1, 1]
ants = np.array([i for i in range(0, stick, 50)])
step = [random.choice(direction) for x in range(len(ants))]
match = 0

while True:

    # Clear frame
    display = np.zeros((height, width, 3), dtype=np.uint8)

    # Animate
    for x in range(1, len(ants)-1):
        ants[x] = ants[x]+step[x]
        if ants[x] == stick:
            ants[x] = 0

        # Collision detection and direction toggle
        match = np.where(ants == ants[x])[0]
        if len(match) == 2:
            step[match[0]] *= -1
            step[match[1]] *= -1

        # Draw ants and labels
        cv2.putText(display, f'{x+1}', (ants[x], int(height/2)-5), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=.25, color=(255, 255, 255))
        display[int(height/2), ants[x]] = (0, 0, 255)

    # Display Results
    cv2.imshow('Ants', display)
    cv2.waitKey(16)

