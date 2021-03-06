#!/usr/bin/python2.7
import freenect
import cv2
import numpy as np
import time
from usb.core import find as finddev

dev1=finddev(idVendor=0x045e,idProduct=0x02ae)
dev2=finddev(idVendor=0x045e,idProduct=0x02b0)
dev3=finddev(idVendor=0x045e,idProduct=0x02ad)
dev1.reset()
dev2.reset()
ctx=freenect.init()
mdev=freenect.open_device(ctx,0)
freenect.shutdown(ctx)
print(ctx)
print(mdev)
freenect.sync_stop()


def applyCustomColorMap(im_gray) :

    lut = np.zeros((256, 1, 3), dtype=np.uint8)

    lut[:, 0, 0] = [0,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,0,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,0,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,0,50,50,50,50,50,50,50,50,50,50,50,50,52,49,51,0,48,48,48,46,47,47,43,45,45,45,44,44,43,43,43,0,46,45,46,45,50,50,50,51,55,56,56,56,62,61,61,0,61,68,67,67,68,73,73,73,73,78,79,79,79,78,86,0,100,101,100,103,101,101,101,103,103,103,106,103,105,105,104,0,105,104,106,102,104,104,255,255,255,255,255,255,255,255,255,0,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,0,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,0,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,0,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,0,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,0,255,255,255,255,255,255,255,255,255,255,50,50,50,50,50,0,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50]
    
    lut[:, 0, 1] = [0,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,0,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,0,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,0,62,62,62,62,62,62,62,62,62,62,62,62,61,62,72,0,73,73,84,83,84,83,85,96,96,96,96,107,107,107,107,0,123,122,123,124,139,137,138,140,152,155,154,154,168,170,170,0,171,184,183,183,184,194,195,194,195,205,206,206,206,208,219,0,235,236,231,231,231,231,225,226,226,225,227,220,219,219,219,0,211,213,212,205,206,206,153,152,151,149,148,147,146,144,143,0,141,139,138,137,135,134,133,132,130,129,128,126,125,124,123,0,120,119,118,116,115,114,112,111,110,109,107,106,105,104,102,0,100,98,97,96,95,93,92,91,90,88,87,86,84,83,82,0,79,78,77,75,74,73,72,70,69,68,67,65,64,63,61,0,59,58,56,55,54,53,51,50,49,47,46,45,44,42,41,0,39,37,36,35,33,32,31,30,28,27,62,62,62,62,62,0,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62]

    lut[:, 0, 2] = [0,181,181,181,181,181,181,181,181,181,181,181,181,181,181,181,0,181,181,181,181,181,181,181,181,181,181,181,181,181,181,181,0,181,181,181,181,181,181,181,181,181,181,181,181,181,181,181,0,181,181,181,181,181,181,181,181,181,181,181,181,182,181,186,0,186,186,194,193,194,193,194,201,201,201,201,207,207,207,207,0,210,209,210,205,208,213,211,209,213,211,212,212,217,214,214,0,212,217,214,214,213,217,214,215,214,217,215,215,216,211,216,0,179,178,167,165,166,166,156,154,154,156,152,141,141,141,141,0,126,127,127,116,111,111,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,181,181,181,181,181,0,181,181,181,181,181,181,181,181,181,181,181,181,181,181,181]

    im_color = cv2.LUT(im_gray, lut)

    return im_color;



#function to get depth image from kinect
def get_depth():
    array,_=freenect.sync_get_depth()
    array=array.astype(np.uint8)
    return array


while 1:
    if not mdev:
        ctx=freenect.init()
        mdev=freenect.open_device(ctx,0)
        print(ctx)
        print(mdev)
        freenect.shutdown(ctx)
        time.sleep(0.1)
        k = cv2.waitKey(5) & 0xFF
        if k == 27:
            break
    else:
        while 1:
            #if asdasdsd
            #    shutdown now -h
            #get a frame from depth sensor
            im=get_depth()
            im=get_depth();
            im=cv2.cvtColor(im, cv2.COLOR_GRAY2BGR);
            im_color=applyCustomColorMap(im);
            #display depth image in fullscreen
            cv2.namedWindow("test", cv2.WND_PROP_FULLSCREEN)
            cv2.setWindowProperty("test", cv2.WND_PROP_FULLSCREEN, cv2.cv.CV_WINDOW_FULLSCREEN)
            cv2.imshow("test",im_color)
            # quit program when 'esc' key is pressed
            #if asdsad
            #   program end (break)   
            k = cv2.waitKey(5) & 0xFF
            if k == 27:
                break  
        break
freenect.shutdown(ctx)
cv2.destroyAllWindows()

