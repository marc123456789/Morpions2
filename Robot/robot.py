class Robot:

    def __init__(self, nom):
        self.nom = nom

    def __repr__(self):
        return "Je m'appelle {0} et je suis une intelligence artificiel !!".format(self.nom)
    
    def __str__(self):
        return self.__repr__()
