from photonrobot import *
import time
import random
import math

photon.change_color("black")
speed = 77
rpm = 50

while True:
    D = photon.get_distance_from_obstacle()
    photon.go_forward_infinity(speed)
    if D < 35: #(speed/100)*40 + (speed * 0.1) :
        photon.stop()
        r1 = random.randint(90, 180)
        r2 = random.randint(0, 9)
        obr = (56 * (rpm/100)) / 60
        if rpm == 100:
            czas = obr * (r1 / 360)
        else:
            czas = obr * (r1 / 360) * (10 - (0.1 * rpm))
        #czas = parseDou
        if r2 > 4:
            photon.rotate_right_infinity(rpm)
            time.sleep(czas)
            print('Skrecono ',r1,' stopni w prawo', obr, math.floor(czas))
            photon.stop()
        else:
            photon.rotate_left_infinity(rpm)
            time.sleep(czas)
            print('Skrecono ',r1,' stopni w lewo', obr, math.floor(czas))
            photon.stop()

    
