import cv2
from djitellopy import Tello
import threading
from pyzbar import pyzbar
import time
import numpy as np
from csv import writer
import datetime
import argparse

startscanning = 0


def scan():
    global myframe
    global startscanning
    # construct the argument parser and parse the arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("-o", "--output", type=str, default="barcode.csv",
                    help="path to output CSV file containing barcodes")
    args = vars(ap.parse_args())
    # open the output CSV file for writing and initialize the set of
    csv = open(args["output"], "w")
    found = set()
    while True:

        if startscanning == 1:
            barcodes = pyzbar.decode(myframe)
            # loop barcode
            for barcode in barcodes:
                (x, y, w, h) = barcode.rect
                cv2.rectangle(myframe, (x, y), (x + w, y + h), (0, 255, 0), 2)
                barcodeData = barcode.data.decode("utf-8")
                barcodeType = barcode.type
                text = "{} ({})".format(barcodeData, barcodeType)
                cv2.putText(myframe, text, (x, y - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

                # if the barcode text is currently not in our CSV file, write
                # the timestamp + barcode to disk and update the set
                if barcodeData not in found:
                    csv.write("{},{}\n".format(datetime.datetime.now(),
                                               barcodeData))
                    csv.flush()
                    found.add(barcodeData)

                # show the frame
                # cv2.resizeWindow('output', 625,450)
            cv2.imshow('output', myframe)

            key = cv2.waitKey(8) & 0xFF
            if key == ord("q"):
                break

    csv.close
    cv2.destroyAllWindows()


def cam():
    print('start cam')
    global myframe
    global startscanning
    while True:
        frame_read = me.get_frame_read()
        myframe = frame_read.frame
        startscanning = 1


# Start Mou
me = Tello()
me.connect()
me.for_back_velocity = 0
me.left_right_velocity = 0
me.up_down_velocity = 0
me.yaw_velocity = 0
me.speed = 0

print(me.get_battery())
me.streamoff()
me.streamon()

# threding cam
camera = threading.Thread(target=cam, args=())
camera.deamon = True
# threding scanning
scanning = threading.Thread(target=scan, args=())
scanning.deamon = True

time.sleep(3)
camera.start()
scanning.start()
time.sleep(1)

# while True:
# me.takeoff()
# time.sleep(3)
#
# me.move_down(25)
# time.sleep(6)
# me.move_up(25)
# time.sleep(6)
# me.move_up(40)
# time.sleep(6)
# me.move_up(50)
# time.sleep(6)
# me.rotate_clockwise(180)
# time.sleep(6)
# me.move_down(50)
# time.sleep(6)
# me.move_down(40)
# time.sleep(6)
# me.move_down(25)
# time.sleep(6)
#
# me.land()
# break