import math
i=0
d = 25
x_poz=2
y_poz=2
alfa = 0
k_obr = 15
length = 12
tab = [["_"]*12 for _ in range(9)] #generowanie pustej tablicy 12 x 9
for i in range(8,-1,-1):
    print(tab[i])
################################################# generowanie tablic /\ | dane pomiarowe \/
tab_x=[5,5,5,4,3,1,0,-1,-2,-2,-2,-2,-2,-2,-2,-2,-1,-1,0,1,1,2,3,5]
tab_y=[0,1,3,4,5,5,5,5,3,2,1,1,0,-1,-1,-2,-2,-2,-2,-2,-2,-2,-2,-1]
tab_p=[125,125,125,125,125,125,125,125,80,55,43,25,25,43,43,55,43,43,25,43,43,55,80,125]
###############################################3 WYPEŁNIANIE OBRĘCZY
while alfa<360: #PEŁNY OBRÓT 360 STOPNI
    #pom = photon.get_distance_from_obstacle()
    #pom = pom + length
    pom = tab_p[i] + length
    if pom > 120:
        pom=120
    de_x = math.cos(math.radians(alfa))*(pom) #DELTA X
    de_y = math.sin(math.radians(alfa))*(pom) #DELTA Y
    x_in = max(math.floor(de_x/25) + x_poz,0) #INDEX X TABLICY Z DODANĄ POZYCJĄ
    y_in = max(math.floor(de_y/25) + y_poz,0) #INDEX Y TABLICY Z DODANĄ POZYCJĄ
    
    if pom>=120:
        tab[y_in][x_in] = "o" #zapisywanie do tablicy wystąpienie krańca zasięgu czujnika
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
    alfa += k_obr
    i+=1
    
###################################################################3
tab[y_poz][x_poz] = "s" #ZAZNACZENIE POZYCJI ROBOTA
print("-------------------")
for i in range(8,-1,-1):
    print(tab[i])
print("-------------------")