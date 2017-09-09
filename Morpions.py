import MFonction
import Data


#-- Variable --#
game = None
j1 = None
j2 = None
canBegin = False
#--------------#

MFonction.affiche()

while game == None:

    game = input("> ")

    try:
        game = int(game)
    except ValueError:
        game = None
        continue

    try:
        game = Data.modes[game-1]
    except IndexError:
        game = None
    else:
        print("Vous avez choisie le mode de jeu : {0}".format(game))

if game == Data.modes[0]:
    while j1 == None:
        j1 = input("(j1) X ou O > ")

        if j1 != "X" and j1 != "O":
            j1 = None
            continue

    while j2 == None:
        j2 = input("(j2) X ou O > ")

        if j2 != "X" and j2 != "O":
            j2 = None
            continue

    if j1 == j2:
        j1 = "X"
        j2 = "O"
        print("joueur 1 et 2 sont identique !")

    print("joueur 1 - {0}, joueur 2 - {1}".format(j1, j2))
    MFonction.grille()
    canBegin = True
else: 
    print("Le mode de jeu ({0}) n'est pas encore disponnible !".format(game))   
    canBegin = False



while canBegin: 
    MFonction.onTurn(j1)
    if MFonction.isWin(j1):
        break
    MFonction.onTurn(j2)  
    if MFonction.isWin(j1):
        break
input("Entrer une touche pour continuer...")