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

		cases[(0, 0)],cases[(1, 0)],cases[(2, 0)],"\n",
		cases[(0, 1)],cases[(1, 1)],cases[(2, 1)],"\n",
		cases[(0, 2)],cases[(1, 2)],cases[(2, 2)], sep =""

		)
	print("")
def snake_case(case, joueur):

    """A l'aide de l'id et du joueur passer en parametre, la fonction va placer le joueur dans le dictionnaire CASES""" 
    cases[case] = joueur

def caseInToId(case):
    for i, elt in enumerate(cases):
        if i+1 == case:
            return elt

def onTurn(joueur):


    while True:
        j_turn = input("({0}) > ".format(joueur))

        try:
            j_turn = int(j_turn)
        except ValueError:
            continue
        
        j_turn = caseInToId(j_turn)

        if isFree(j_turn):
            snake_case(j_turn, joueur)
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
    """Fonction determinant l'issue de la partie si le joueur a gagner ou pas"""
    
    for y in cases:
        if cases[(0, y[1])] == cases[(1, y[1])] == cases[(2, y[1])] == joueur:
            print("Le joueur {0} a gagner la partie !".format(joueur))
            return True
    
    for j in cases:
        if cases[(j[1], 0)] == cases[(j[1], 1)] == cases[(j[1], 2)] == joueur:
            print("Le joueur {0} a gagner la partie !".format(joueur))
            return True
    
    if cases[(2, 0)] == cases[(1, 1)] == cases[(0, 2)] == joueur:
        print("Le joueur {0} a gagner la partie !".format(joueur))
        return True
    if cases[(0, 0)] == cases[(1, 1)] == cases[(2, 2)] == joueur:
        print("Le joueur {0} a gagner la partie !".format(joueur))
        return True
    return False
