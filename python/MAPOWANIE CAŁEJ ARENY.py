from photonrobot import *
photon.change_color(Colors.blue, "ears")
photon.change_color(Colors.red, "eyes")

import math
i=0
d = 25
x_poz=2
y_poz=2
alfa = 0
k_obr = 15
length = 12
tab = [["_"]*12 for _ in range(9)] #generowanie pustej tablicy 12 x 9
tabulong = [["_"]*12 for _ in range(9)] #generowanie pustej tablicy 12 x 9
for i in range(8,-1,-1):
    print(tab[i])
################################################# generowanie tablic /\ | \/WYPEŁNIANIE OBRĘCZY
def mapa(x_poz, y_poz, tab, alfa):
    while alfa<360: #PEŁNY OBRÓT 360 STOPNI
        pom = photon.get_distance_from_obstacle()
        pom = pom + 12#length
        if pom > 120:
            pom=120
        de_x = math.cos(math.radians(alfa))*(pom) #DELTA X
        de_y = math.sin(math.radians(alfa))*(pom) #DELTA Y
        x_in = max(math.floor(de_x/25) + x_poz,0) #INDEX X TABLICY Z DODANĄ POZYCJĄ
        y_in = max(math.floor(de_y/25) + y_poz,0) #INDEX Y TABLICY Z DODANĄ POZYCJĄ
        
        if pom>=120:
            if tab[y_in][x_in]!="u":
                1+1
                #tab[y_in][x_in] = "o" #zapisywanie do tablicy wystąpienie krańca zasięgu czujnika
        else:
            tab[y_in][x_in] = "x" #zapisywanie do tablicy wystąpienie przeszkody/ściany

        while pom>=26:
            pom-=25
            de_x = math.cos(math.radians(alfa))*pom
            de_y = math.sin(math.radians(alfa))*pom
            x_in = max(math.floor(de_x/25) + x_poz,0)
            y_in = max(math.floor(de_y/25) + y_poz,0)
            if tab[y_in][x_in] == "_":
                tab[y_in][x_in] = "u"
        alfa += 15
        photon.rotate_left(12, 25)
        #i+=1
    return tab

def poka(tab):
    print("-------------------")
    for i in range(8,-1,-1):
        print(tab[i])
    print("-------------------")

def Jazda(poz_x,poz_y,tryb):
    pom = photon.get_distance_from_obstacle()
    if tryb=="index":
        poz_x=poz_x*25
        poz_y=poz_y*25
        
    if poz_x>0: #and pom>poz_x:
        photon.go_forward(poz_x, 25)
    elif poz_x<0:
        photon.go_backward(-poz_x, 25)#żeby ograniczyć skręcanie do minimum
        #photon.go_forward(poz_x, 25)
    #############
    if poz_y>0:
        photon.rotate_left(87, 25) 
        photon.go_forward(poz_y, 25)
        photon.rotate_right(87, 25)
    elif poz_y<0:
        photon.rotate_right(87, 25)
        photon.go_forward(-poz_y, 25)
        photon.rotate_left(87, 25)


###################################################################3

tab=mapa(x_poz,y_poz,tab,0)
tab[y_poz][x_poz] = "s" #ZAZNACZENIE POZYCJI STARTOWEJ ROBOTA
poka(tab)
##################################
dod_x=6
dod_y=0
Jazda(dod_x,dod_y,"index") #tryb 0 to agrumenty po indexach, tryb 1 to wartoci cm
x_poz += dod_x
y_poz += dod_y
print(x_poz," | ",y_poz)
tab = mapa(x_poz,y_poz,tab,0)
poka(tab)

##################################
dod_x=0
dod_y=4
Jazda(dod_x,dod_y,"index") #tryb 0 to agrumenty po indexach, tryb 1 to wartoci cm
x_poz += dod_x
y_poz += dod_y
print(x_poz," | ",y_poz)
tab = mapa(x_poz,y_poz,tab,0)
poka(tab)

##################################
dod_x=-6
dod_y=0
Jazda(dod_x,dod_y,"index") #tryb 0 to agrumenty po indexach, tryb 1 to wartoci cm
x_poz += dod_x
y_poz += dod_y
print(x_poz," | ",y_poz)
tab = mapa(x_poz,y_poz,tab,0)
poka(tab)

##################################
dod_x=0
dod_y=-4
Jazda(dod_x,dod_y,"index") #tryb 0 to agrumenty po indexach, tryb 1 to wartoci cm
tabulong=tab
odl=1
tabulong[x_poz+1,0]=odl #skonczyl na 16,5 cm chyba, albo 17
