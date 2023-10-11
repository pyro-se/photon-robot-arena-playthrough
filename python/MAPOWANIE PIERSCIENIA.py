from photonrobot import *
import math

photon.change_color("pink", ColorMode.eyes)
photon.change_color("blue", ColorMode.ears)

d = 25
x1=2
y1=2
alfa = 0
k_obr = 15
length = 12
tab = [["_"]*12 for _ in range(9)] #generowanie pustej tablicy 12 x 9
for i in range(8,-1,-1):
    print(tab[i])
################################################# generowanie tablic /\

while alfa<360: #PEŁNY OBRÓT 360 STOPNI
    pom = photon.get_distance_from_obstacle()
    if pom > 125:
        pom=125
    pom = pom + length
    cp1 = math.cos(math.radians(alfa))*(pom/d) #delta X
    sp1 = math.sin(math.radians(alfa))*(pom/d) #delta Y
    tab[round(sp1+y1)][round(cp1+x1)] = "o" #zapisywanie do tablicy wystąpienie przeszkody (ściany lub krańca zasięgu czujnika)

    ###############################################3 WYPEŁNIANIE OBRĘCZY
    if cp1>=sp1: #x>y
        for i in range (x1+1,int(cp1),1):
            y=math.tan(math.radians(alfa))*i+y1 #y=tg(alfa)*x+b
            y = round(y)
            #tab[round(x1+i)][round(y1+y)] = "U"
            print(y1+y," ",x1+i)
            tab[y1+y][x1+i] = "u"
            if y1+y<0:
                tab[0][x1+i] = "u"
            elif x1+i<0:
                tab[y1+y][0] = "u"
    else: #y>=x
        for j in range (y1+1,int(sp1),1):
            ctg = 1/math.tan(math.radians(alfa))
            x=ctg*j+x1 #x=ctg(alfa)*y+b
            x = round(x)
            #tab[round(x1+x)][round(y1+j)] = "U"
            tab[y1+j][x1+x] = "u"
    ###################################################################3

    alfa += k_obr
    photon.rotate_left(k_obr-3, 50)

tab[y1][x1]="x"
for i in range(8,-1,-1):
    print(tab[i])