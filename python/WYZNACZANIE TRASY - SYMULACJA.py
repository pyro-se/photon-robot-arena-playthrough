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
def prop_fal(tab,x,y,i,loc_x,loc_y):
    g = True
    #i=1
    poka(tab)
    if not (x<0 or x>11): # or y<0 or y>8
        if tab[y+1][x]=="_":
            tab[y+1][x]=str(i)
            prop_fal(tab,x,y+1,i+1,10,10)
        if tab[y-1][x]=="_":
            tab[y-1][x]=str(i)
            #prop_fal(tab,x,y-1,i+1,10,10)
        if tab[y][x+1]=="_":
            tab[y][x+1]=str(i)
            #prop_fal(tab,x+1,y,i+1,10,10)
        if tab[y][x-1]=="_":
            tab[y][x-1]=str(i)
            #prop_fal(tab,x-1,y,i+1,10,10)
    if not (y<0 or y>8):
        if tab[y+1][x]=="_":
            tab[y+1][x]=str(i)
            #prop_fal(tab,x,y+1,i+1,10,10)
        if tab[y-1][x]=="_":
            tab[y-1][x]=str(i)
            #prop_fal(tab,x,y-1,i+1,10,10)
        if tab[y][x+1]=="_":
            tab[y][x+1]=str(i)
            prop_fal(tab,x+1,y,i+1,10,10)
        if tab[y][x-1]=="_":
            tab[y][x-1]=str(i)
            #prop_fal(tab,x-1,y,i+1,10,10)
    else:
        return tab
    return tab
def Nast_Komorka(x,y):
	return{
		"x+": [x+1,y],
        "x-": [x-1,y],
        "y+": [x,y+1],
        "y-": [x,y-1]
	}.values()

def Trasa(tab,x1,y1,x2,y2):
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

def prop_fal(tab,x,y,i):        
    poka(tab)
    if not (x<0 or x>11): # or y<0 or y>8
        if tab[y+1][x]=="_":
            tab[y+1][x]=str(i)
            prop_fal(tab,x,y+1,i+1,10,10)
        if tab[y-1][x]=="_":
            tab[y-1][x]=str(i)
            #prop_fal(tab,x,y-1,i+1,10,10)
        if tab[y][x+1]=="_":
            tab[y][x+1]=str(i)
            #prop_fal(tab,x+1,y,i+1,10,10)
        if tab[y][x-1]=="_":
            tab[y][x-1]=str(i)
            #prop_fal(tab,x-1,y,i+1,10,10)
    if not (y<0 or y>8):
        if tab[y+1][x]=="_":
            tab[y+1][x]=str(i)
            #prop_fal(tab,x,y+1,i+1,10,10)
        if tab[y-1][x]=="_":
            tab[y-1][x]=str(i)
            #prop_fal(tab,x,y-1,i+1,10,10)
        if tab[y][x+1]=="_":
            tab[y][x+1]=str(i)
            prop_fal(tab,x+1,y,i+1,10,10)
        if tab[y][x-1]=="_":
            tab[y][x-1]=str(i)
            #prop_fal(tab,x-1,y,i+1,10,10)

wypelnij(tab,20)
tab[y_poz][x_poz]="s"
tab[7][10]="o"
poka(tab)
trasa = Trasa(tab,x_poz,y_poz,10,7)
if trasa != None:
    for xy in trasa:
        x, y = xy
        tab[y][x]="@"
        poka(tab)
else:
    print('Nie ma sciezki')
#prop_fal(tab,x_poz,y_poz,1,2,10)
