class Robot:

    def __init__(self, nom):
        pass

    def __repr__(self):
        return "Je m'appelle {0} et je suis une intelligence artificiel !!".format(self.nom)
    
    def __str__(self):
        self.__repr__()