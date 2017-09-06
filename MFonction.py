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


#

def grille():
	 
	""" Fonction affichant la grille de jeu """
	print(

		cases["A1"],cases["A2"],cases["A3"],"\n",
		cases["B1"],cases["B2"],cases["B3"],"\n",
		cases["C1"],cases["C2"],cases["C3"], sep =""

		)

def place(case, joueur):

    """A l'aide de l'id et du joueur passer en parametre, la fonction va placer le joueur dans le dictionnaire CASES""" 
    cases[case] = joueur

#

def affiche():
	""" Fonction affichant la liste des modes """
	i = 0
	for elt in mode:
		i += 1
		print("{0}- {1}".format(i, elt))

def isWin(joueur):
    """Fonction determinant l'issue de la partie si le joueur a gagner ou pas"""
    if cases["A1"] == joueur and cases["A2"] == joueur and cases["A3"] == joueur:
	    print("Le joueur {0} a gagner !!".format(joueur))
	    return True
    elif cases["B1"] == joueur and cases["B2"] == joueur and cases["B3"] == joueur:
	    print("Le joueur {0} a gagner !!".format(joueur))
	    return True
    elif cases["C1"] == joueur and cases["C2"] == joueur and cases["C3"] == joueur:
	    print("Le joueur {0} a gagner !!".format(joueur))
	    return True
    elif cases["A1"] == joueur and cases["B1"] == joueur and cases["C1"] == joueur:
	    print("Le joueur {0} a gagner !!".format(joueur))
	    return True
    elif cases["A2"] == joueur and cases["B2"] == joueur and cases["C2"] == joueur:
	    print("Le joueur {0} a gagner !!".format(joueur))
	    return True
    elif cases["A3"] == joueur and cases["B3"] == joueur and cases["C3"] == joueur:
	    print("Le joueur {0} a gagner !!".format(joueur))
	    return True
    elif cases["A1"] == joueur and cases["B2"] == joueur and cases["C3"] == joueur:
	    print("Le joueur {0} a gagner !!".format(joueur))
	    return True
    elif cases["A3"] == joueur and cases["B2"] == joueur and cases["C1"] == joueur:
	    print("Le joueur {0} a gagner !!".format(joueur))
	    return True
    if cases["A1"] != "*" and cases["A2"] != "*" and cases["A3"] != "*" and cases["B1"] != "*" and cases["B2"] != "*" and cases["B3"] != "*" and cases["C1"] != "*" and cases["C2"] != "*" and cases["C3"] != "*":
	    print("match nul !!")
	    return True

    return False


