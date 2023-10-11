from photonrobot import *
import math

photon.change_color("purple")

D = photon.get_distance_from_obstacle()
if D > 20:
    photon.go_forward(15, 50)

for i in range(2):
    dis = []
    photon.rotate_left(30,50)
    DL1 = photon.get_distance_from_obstacle()
    #dis.append(photon.get_distance_from_obstacle())
    photon.rotate_left(30,50)
    DL2 = photon.get_distance_from_obstacle()
    #dis.append(photon.get_distance_from_obstacle())

    photon.rotate_right(60,50)
    DC = photon.get_distance_from_obstacle()
    #dis.append(photon.get_distance_from_obstacle())

    photon.rotate_right(30,50)
    DR1 = photon.get_distance_from_obstacle()
    #dis.append(photon.get_distance_from_obstacle())

    photon.rotate_right(30,50)
    DR2 = photon.get_distance_from_obstacle()
    #dis.append(photon.get_distance_from_obstacle())
    
    dis.append(DL2)
    dis.append(DL1)
    dis.append(DC)
    dis.append(DR1)
    dis.append(DR2)
    
    
    photon.rotate_left(120,50)
    index = 0
    for j in dis:
        if j == min(dis) and index>0:
            photon.rotate_right(30*index,50)
        index+=1
    photon.make_sound("dog")
    photon.go_forward(math.floor(min(dis)*0.5), 50)


D = photon.get_distance_from_obstacle()
if D >= 5:
    photon.rotate_right(90,50)
elif D < 5:
    photon.go_backward(5,50)
    photon.rotate_right(90,50)
photon.make_sound("cat")

D = photon.get_distance_from_obstacle()
while D>10:
    photon.go_forward(math.floor(D*0.7), 50)
    D = photon.get_distance_from_obstacle()

photon.rotate_right(90,50) #twarza do mierzenia

photon.change_color("blue")
#photon.rotate_right(180,50)
#D = photon.get_distance_from_obstacle()
#photon.rotate_left(180,50) #CELOWO WYKOMENTOWANE BO NIE BY£O POTRZEBNE US
#photon.go_backward(math.floor(D+15),25)
photon.go_backward(60,25)

##### ZACZYNAMY MIERZENIE
M = []
tmp = 0

for i in range(2):
    tmp = 0
    D = photon.get_distance_from_obstacle()
    while D > 10:
        D = photon.get_distance_from_obstacle()
        #photon.go_forward(math.floor(D*0.8), 50)
        if D < 20:
            #photon.go_forward(D-10, 50)
            #tmp += D-10
            print("test - koniec")
            tmp+=D
            break
        else:
            photon.go_forward(20, 50)
            tmp += 20
         
        #tmp += D*0.8
    D = photon.get_distance_from_obstacle()
    tmp+= 15#Dodanie d³ugoœci robota
    M.append(tmp)
    photon.rotate_right(90,50)
    D = photon.get_distance_from_obstacle()
    #if i==0:
    photon.go_backward(40,25)
    photon.go_forward(5, 50)
    photon.make_sound("cat")

#M=[200, 268]
#photon.go_forward(5, 50)
zal = M[0]/M[1]
alfa = math.atan(zal)
alfa = math.degrees(alfa)
photon.rotate_right(90-math.floor(alfa),50)
print(math.floor(alfa))
print(zal)
print(alfa)
final = math.sqrt((M[0]/2)**2 + (M[1]/2)**2)
photon.go_forward(math.floor(final)-10,100)
photon.rotate_right(360,100)
print(M)
print(M[0]*M[1])
