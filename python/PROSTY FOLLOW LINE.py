from photonrobot import *
photon.change_color("red")
def info(line):
    print("L: ",line.front_right, " ","C: ",line.front_center ," ","R: ",line.front_left)

v_obr=6
v = 21
while True:
    photon.go_forward_infinity(v)
    line = photon.get_line_sensors()
    if line.front_left==True:
        photon.rotate_right_infinity(v_obr)
        while line.front_center==False:
            line = photon.get_line_sensors()
    elif line.front_right==True:
        photon.rotate_left_infinity(v_obr)
        while line.front_center==False:
            line = photon.get_line_sensors()

                    
