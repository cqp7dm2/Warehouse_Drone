import cv2
from djitellopy import Tello
import time
import numpy as np
from csv import writer
import datetime

width = 320
height = 240
alpha=1.7
beta=255

Row = 0
CL= 0
X = 0 # Current X
Y = 0 # Current Y
XD = 0 #X destination
YD = 0 #Y destination
XP = 0 #X Pathing
YP = 0 # YPathing

me = Tello()
me.connect()
me.for_back_velocity =0
me.left_right_velocity = 0
me.up_down_velocity = 0
me.yaw_velocity = 0
me.speed = 0

print(me.get_battery())
me.streamoff()
me.streamon()

me.takeoff()
time.sleep(6)

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

# time.sleep(5)
# me.move_left(20)
# time.sleep(5)
# me.move_up(30)
CL += 1
print('Current Area:', CL)
# X += 10
# Y += 200
time.sleep(3)
# me.move_right(20)
CL += 1
# print('Current Box:', CL)
# time.sleep(5)
# me.move_down(20)
# redcir()
# CL += 1
# print('Current Box:', CL)
# time.sleep(5)
# me.move_left(20)
# redcir()
# CL += 1
# print('Current Box:', CL)
# time.sleep(5)
# me.land()
# Row += 1

me.land()


#write end log
now=datetime.datetime.now()
time1= now.strftime("%I:%M:%S%p")
date=now.strftime("%d%b%Y")
log_content=['Auto Mode endded at','time:',time1,'date',date]
append_list_as_row('Drone_tracking.csv', log_content)
append_list_as_row('Drone_tracking.csv', [])

#end
cv2.destroyAllWindows()

