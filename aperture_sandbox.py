import cv2
import numpy as np

cv2.rotate

def grating(canvas, angle, spacing, step=0):
    frame = np.zeros_like(canvas, dtype=np.uint8)
    pt1 = [step,0]
    pt2 = [step,height]

    reps = canvas.shape[0] // spacing

    for ii in range(reps):
        cv2.line(frame, pt1, pt2, (1,1,1), 1)
        pt1[0] += spacing
        pt2[0] += spacing

    #cv2.rotate()
    return frame    

height = 512
width = 512
origin = [height//2, width//2]

canvas = np.zeros([height, width], dtype=np.uint8)
mask = cv2.circle(canvas.copy(), origin, 200, (1,1,1), -1)

line_one_top = [0,0]
line_one_btm = [width,height]

line_two_top = [0,height]
line_two_btm = [width,0]

step = 5



#Make a function to add an arbitrary line/offset

while True:

    frame = grating(canvas, angle=10, spacing=10, step=step)
    step += 1
    # frame = canvas.copy()

    # cv2.line(frame, line_one_top, line_one_btm, (255,255,255), 3)
    # cv2.line(frame, line_two_top, line_two_btm, (255,255,255), 3)
    
    frame *= mask

    if step >= 10:
        step = 0

    # line_one_top[0] += step
    # line_one_btm[0] += step

    # line_two_top[0] += step
    # line_two_btm[0] += step

    # if line_one_top[0] >= width:
    #     line_one_top = [-width,0]
    #     line_one_btm = [0,height]
    #     line_two_top = [-width,height]
    #     line_two_btm = [0,0]

    cv2.imshow("Aperture", frame*255)
    key = cv2.waitKey(16) 
    if key == ord('q'):
        break
    cv2.destroyAllWindows