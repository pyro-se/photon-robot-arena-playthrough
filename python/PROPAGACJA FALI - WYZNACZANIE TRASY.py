#from photonrobot import *
import random

znak = "x"
y_poz = 2
x_poz = 2
tab = [["_"]*12 for _ in range(9)] #generowanie pustej tablicy 12 x 9
def poka(tab):
    print("-------------------")
    for i in range(8,-1,-1):
        print(tab[i])
    print("-------------------")
#-----------------------------------------------
def wypelnij(tab,ile):
    for i in range(9):
        tab[i][0] = znak
        tab[i][11] = znak
    for j in range(12):
        tab[0][j] = znak
        tab[8][j] = znak
    for k in range(ile):
        x = random.randint(1, 10)
        y = random.randint(1, 7)
        tab[y][x] = znak
#-----------------------------------------------
def Trasa2(tab,x1,y1,x2,y2):
    szukana = [[[x1, y1]]]
    historia = [x1, y1]
    while szukana != []:
        obecna_sciezka = szukana.pop(0)
        obecne_xy = obecna_sciezka[-1]
        x, y = obecne_xy
        #print(obecne_xy)
        if obecne_xy == [x2, y2]:
            return obecna_sciezka
        for next_xy in Nast_Komorka(x, y):
            next_x, next_y = next_xy
            if next_x <0 or next_x>=12:
                continue
            if next_y<0 or next_y>=9:
                continue
            if next_xy in historia:
                continue
            if tab[next_y][next_x]==znak:
                continue
            szukana.append(obecna_sciezka + [next_xy])
            historia += [next_xy]
################################################################

def Nast_Komorka(x,y):
	return{
		"x+": [x+1,y],
        "x-": [x-1,y],
        "y+": [x,y+1],
        "y-": [x,y-1]
	}.values()

def propagacja(tab,x,y):
    i=1
    maks = 0
    #x, y = x1, y1
    wiktor = []
    tmp = []
    for next_xy in Nast_Komorka(x, y):
        next_x, next_y = next_xy
        if tab[next_y][next_x] == "_" :
            tab[next_y][next_x] = str(i)
            tmp.append([next_x, next_y])
            if i>maks:
                maks=i
    print(wiktor)
    while i<20:
        wiktor = tmp
        tmp = []
        i+=1
        for xy in wiktor:
            x, y = xy
            for next_xy in Nast_Komorka(x, y):
                next_x, next_y = next_xy
                if tab[next_y][next_x] == "_" :
                    tab[next_y][next_x] = str(i)
                    tmp.append([next_x, next_y])
                    if i>maks:
                        maks=i
    wiktor = []
    return tab#, maks

def trasa(tab,x,y):
    #x,y <--- START
    znaczek = "#"
    wiktor = []
    min = 25
    while tab[y][x] != "o":
        for next_xy in Nast_Komorka(x, y):
            next_x, next_y = next_xy
            if tab[next_y][next_x] == "o":
                x, y = next_x, next_y
                return tab
            elif tab[next_y][next_x] not in ["x","s",znaczek,"_"]:
                if int(tab[next_y][next_x]) < min:
                    tmp_x, tmp_y = next_x, next_y
                    min = int(tab[next_y][next_x])
                    #print(min)
        x = tmp_x
        y = tmp_y
        tab[y][x]=znaczek
    return tab

##############################################################################
xx=10
yy=7
wypelnij(tab,25)
tab[yy][xx]="o"
tab[y_poz][x_poz]="s"
poka(tab)

tab = propagacja(tab,xx,yy)
poka(tab)
tab = trasa(tab,x_poz,y_poz)

i, j = 0, 0
for wiersze in tab:
    j=0
    for w in wiersze:
        if w not in ["x","s","_","o","#"]:
            tab[i][j]="_"
        j+=1
    i+=1
poka(tab)
