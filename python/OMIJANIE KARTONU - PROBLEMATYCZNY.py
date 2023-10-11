from photonrobot import *

def naprowadz():
    daleko = True
    while daleko is True:
        d1 = photon.get_distance_from_obstacle()
        photon.rotate_left(20, 50)
        d2 = photon.get_distance_from_obstacle()
        photon.rotate_left(20, 50)
        d3 = photon.get_distance_from_obstacle()
        if d1<d2 and d1<d3:
            d=d1
            if d>10:
                photon.rotate_right(40, 50)
                photon.go_forward(0.9 * d, 50)
            else:
                photon.rotate_right(20, 50)
                daleko = False
        if d2 < d1 and d2 < d3:
            d=d2
            if d > 10:
                photon.rotate_right(20, 50)
                photon.go_forward(0.9 * d, 50)
            else:
                photon.rotate_right(10, 50)
                daleko = False
        if d3 < d2 and d3 < d1:
            d=d3
            if d > 10:
                photon.go_forward(0.9 * d, 50)
            else:
                daleko = False
        
photon.change_color("purple")

czy_lewo = False
czy_prosto = False
w = False
cykl = 0
while True:
    distance = photon.get_distance_from_obstacle()
    if distance > 15:
        czy_prosto = False
    elif distance < 15:
        czy_prosto = True
    photon.rotate_left(90, 50)
    distance = photon.get_distance_from_obstacle()
    if distance < 15:
        czy_lewo = True
        photon.rotate_right(90, 50)
    else:
        czy_lewo = False
        photon.rotate_right(90, 50)


    if not czy_prosto and czy_lewo:
        photon.go_forward(30, 50)

    if not czy_prosto and not czy_lewo:
        photon.rotate_left(90, 50)
        photon.go_forward(30, 50)

    if czy_prosto and czy_lewo:
        photon.rotate_right(90, 50)

    if czy_prosto and not czy_lewo:
        photon.rotate_right(360, 50)
cykl=cykl+1
if cykl==10:
    naprowadz()
    photon.rotate_right(90, 50)
    cykl=0




