from photonrobot import *
import time
import random
import math

photon.change_color("black")
speed = 50
rpm = 25

while True:
    D = photon.get_distance_from_obstacle()
    print("jade")
    photon.go_forward_infinity(speed)
    if D < 20: #(speed/100)*40 + (speed * 0.1) :
        photon.stop()
        #photon.rotate_right_infinity(rpm)
        dystansy=[]
        photon.change_color("blue")
        for i in range(12):
            photon.rotate_right_infinity(rpm)
            #time.sleep(((56 * (rpm/100)) / 60) * (20/360))
            d = photon.get_distance_from_obstacle()
            dystansy.append(d)
            #photon.stop()
            print(i)
            
        photon.stop()
        photon.change_color("red")
        max_wartosc = max(dystansy)
        index = dystansy.index(max_wartosc)
        obr = (56 * (rpm/100)) / 60 # ILE ZAJMUJE JEDEN OBROT SEKUND
        print(dystansy)
        #if rpm == 100:
        #    czas = obr * ((index * 20) / 360) # ILE SEKUND POTRZEBA DO WYKONANIA X STOPNI
        #else:
        czas = obr * (((index * 20)/360) + (10 - (0.1 * rpm)))
        print(czas)
        photon.stop()
        time.sleep(1)
        print(1)
        photon.rotate_right_infinity(rpm)
        time.sleep(czas)
        print(1)
        print('Skrecono ', index*20,' stopni w prawo', obr, czas)
        photon.stop()
        
        #else:
        #    photon.rotate_left_infinity(rpm)
        #    time.sleep(czas)
        #    print('Skrecono ',r1,' stopni w lewo', obr, math.floor(czas))
        #    photon.stop()

    
