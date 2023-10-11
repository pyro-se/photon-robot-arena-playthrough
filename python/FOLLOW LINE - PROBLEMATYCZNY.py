from photonrobot import *
import time
photon.change_color("red")

def info(line):
    print("L: ",line.front_right, " ","C: ",line.front_center ," ","R: ",line.front_left)

def switch_kier(x):
    if x.front_left: #prawy
        return 1
    elif x.front_right: #lewy
        return 0

ost = 0 # 0 to lewo | 1 to prawo
v_obr = 5
kierunek = 0
while True:
#    pom = False
    photon.go_forward_infinity(10)
    line = photon.get_line_sensors()
    info(line)
    kierunek = switch_kier(line)
    
    while (not line.front_center): #and ((not line.front_right) and (not line.front_left)):
        if kierunek==0: #lewy
            photon.rotate_right_infinity(v_obr)
            while True:
                line = photon.get_line_sensors()
                if(line.front_center):
                    photon.stop()
                    ost = 0
                    break
        elif kierunek==1: #prawy
            photon.rotate_left_infinity(v_obr)
            while True:
                line = photon.get_line_sensors()
                if(line.front_center):
                    photon.stop()
                    ost = 1
                    break
        while (not line.front_right) and (not line.front_left) and (not line.front_center):
            line = photon.get_line_sensors()
            #photon.go_backward(1, 40)
            if ost == 0: #lewy
                photon.rotate_left_infinity(v_obr)
            if ost == 1: #elif
                photon.rotate_right_infinity(v_obr)
        photon.stop()
        line = photon.get_line_sensors()
