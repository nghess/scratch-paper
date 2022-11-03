import numpy as np
import random
import cv2

stick = 500
height = 100
width = stick

state1 = [i for i in range(0, stick, 50)]
state2 = []
direction = [-1, 1]
match = 0

for i in state1:
    walk = random.choice(direction)
    new = i+walk
    state2.append(new)



while True:
    count = 0
    #Clear frame
    display = np.zeros((height, width, 3), dtype=np.uint8)

    #print(state2)
    #print(state1)

    for i in range(1, len(state1)-1):
        count += 1

        # Continue in previous direction
        if state1[i] > state2[i]:
            toggle = -1
            new = state2[i] + toggle
            state1[i] = state2[i]
            state2[i] = new
            # Print timestamp
            cv2.putText(display, f'{i}', (new, int(height/2)-5), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=.25, color=(255, 255, 255))

        elif state1[i] < state2[i]:
            toggle = +1
            new = state2[i] + toggle
            state1[i] = state2[i]
            state2[i] = new
            # Print timestamp
            cv2.putText(display, f'{i}', (new, int(height/2)-5), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=.25, color=(255, 255, 255))

        try:
            match = state1.index(new)
            print("collision")
            if state1[i] == state2[i]+1:
                toggle = 2
                #new = state2[i] + toggle

                #state2[i] = new
                state2[i] = state2[i]+toggle
                state1[i] = state1[i]-toggle
                state2[match] = state2[match] - toggle
                print("reverse")

            if state1[i] == state2[match]-1:
                toggle = -2
                #new = state2[i] + toggle

                #state2[i] = new
                state2[i] = state2[i]+toggle
                state1[i] = state1[i]-toggle
                state2[match] = state2[match] - toggle
                print("reverse")
        except:
            print("")



        # Capture dots as they exit
        if new >= 498:
            new = 499
        if new <= 2:
            new = 1

        # Edit image
        display[int(height/2), new] = (0, 0, 255)



    # Display Results
    cv2.imshow('Ants', display)
    #cv2.imwrite("output/lsr-rt/" + str(i) + ".png", display)
    cv2.waitKey(16)

