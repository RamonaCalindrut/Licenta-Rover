import numpy as np
from PIL import ImageGrab
import cv2
import time

def stream_simulation(): 
    last_time = time.time()
    while(True):
        # 800x600 windowed mode
        #printscreen =  np.array(ImageGrab.grab(bbox=(0,40,800,640)))
        printscreen =  np.array(ImageGrab.grab(bbox=(0,40,320,240)))
        print('loop took {} seconds'.format(time.time()-last_time))
        last_time = time.time()
        cv2.imshow('Rover Stream',cv2.cvtColor(printscreen, cv2.COLOR_BGR2RGB))
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

stream_simulation()