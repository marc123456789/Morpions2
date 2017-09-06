from Data import *

""" 
    - Author : Pentakil
    - Date : 02/09/2017

"""
def isFree(case):

    """Si la case est libre cette fonction retourne TRUE sinon FALSE si elle est occuper"""

    if case not in cases:
        return False
    if cases[case] != "*":
        return False
    return True




def grille():
	 
	""" Fonction affichant la grille de jeu """
	print("")
	print(

		cases["A1"],cases["A2"],cases["A3"],"\n",
		cases["B1"],cases["B2"],cases["B3"],"\n",
		cases["C1"],cases["C2"],cases["C3"], sep =""

		)
	print("")
def snake_case(case, joueur):

    """A l'aide de l'id et du joueur passer en parametre, la fonction va placer le joueur dans le dictionnaire CASES""" 
    cases[case] = joueur


def turn(joueur):


    while True:
        j_turn = input("({0}) > ".format(joueur))
        if isFree(j_turn.upper()):
            snake_case(j_turn.upper(), joueur)
            grille()
            break
        else:
            continue


def affiche():
	""" Fonction affichant la liste des modes """
	i = 0
	for elt in modes:
		i += 1
		print("{0}- {1}".format(i, elt))

def isWin(joueur):
