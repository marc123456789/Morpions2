from MFonction import *
from Data import *
from os import *
from time import * 

modes = int()

while True:
    system("CLS")
    affiche()

    modes = input(">")

    try:
        modes = int(modes)
    except ValueError:
        print("la valeur choisie n'est pas un chiffre")
        continue
    
    if modes == 1:
        print("vous avez choisi le mode : {0}".format(mode[0]))
        break
    elif modes == 2:
        print("vous avez choisi le mode : {0}".format(mode[1]))
        break
    elif modes == 3:
        print("vous avez choisi le mode : {0}".format(mode[2]))
        break

while True:
    j1 = input("J1> X ou O : ")
    j2 = input("J2> X ou O : ")

    if j1 != "X" and j1 != "O" or j2 != "X" and j2 != "O":
        continue

    elif j1 == j2 :
        print("joueur 1 et 2 je peuvent pas être identique")
        continue
    else:
        break

system("CLS")
print("joueur 1 > {0}, joueur 2 > {1}".format(j1, j2))
print("le jeu va commencer ...")
sleep(2)

while True:
    system("CLS")
    grille()
    print("c'est je tour du joueur 1 ({0})".format(j1))
    while True:
        c = input(">")
        if isFree(c.upper()):
            place(c.upper(), j1)
            break
        else:
            continue
    system("CLS")
    if isWin(j1):
        break
    grille()
    print("c'est je tour du joueur 2 ({0})".format(j2))
    while True:
        c = input(">")
        if isFree(c.upper()):
            place(c.upper(), j2)
            break
        else:
            continue
    system("CLS")
    if isWin(j2):
        break
