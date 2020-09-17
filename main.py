import cv2
from djitellopy import Tello
import threading
#import pyzbar.pyzbar as pyzbar
import time
import numpy as np
from csv import writer
import datetime

def cam():
    print('start cam')
    global outputFrame
    global startstream
    while True:
        frame_read = me.get_frame_read()
        myframe = frame_read.frame
        cv2.imshow("drone",myframe)
        if cv2.waitKey(1) & 0xFF ==ord("q"):
            break

cv2.destroyAllWindows()

def fly() :
    me.takeoff()
    time.sleep()

    me.move_down(57)
    time.sleep(6)
    me.move_up(43)
    time.sleep(6)
    me.move_up(32)
    time.sleep(6)
    me.move_up(46)
    time.sleep(6)
    me.rotate_clockwise(180)
    time.sleep(6)
    me.move_down(45)
    time.sleep(6)
    me.move_down(35)
    time.sleep(6)
    me.move_down(58)


#Start Mou
me = Tello()
me.connect()
me.for_back_velocity =0
me.left_right_velocity = 0
me.up_down_velocity = 0
me.yaw_velocity = 0
me.speed = 0

#threading flying position
flying= threading.Thread(target=fly, args=())
flying.daemon= True
#threding cam
cam= threading.Thread(target=cam, args=())
cam.deamon= True

print(me.get_battery())
me.streamoff()
me.streamon()

<<<<<<< Updated upstream
# while True:
#     frame_read = me.get_frame_read()
#     myframe = frame_read.frame
#     cv2.imshow("drone",myframe)
#     if cv2.waitKey(1) & 0xFF ==ord("q"):
#         break
# cv2.destroyAllWindows()

me.takeoff()
time.sleep(5)

me.move_down(57)
time.sleep(6)
me.move_up(43)
time.sleep(6)
me.move_up(32)
time.sleep(6)
me.move_up(46)
time.sleep(6)
me.rotate_clockwise(180)
time.sleep(6)
me.move_down(45)
time.sleep(6)
me.move_down(35)
time.sleep(6)
me.move_down(58)

=======
>>>>>>> Stashed changes
time.sleep(3)
me.land()
cv2.destroyAllWindows()

cam.start()
time.sleep(1)
flying.start()
