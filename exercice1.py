class Voiture:
    def __init__(self,marque,annee,vitesse,kilomerrage):
        self.marque = marque
        self.annee = annee
        self.vitesse = vitesse
        self.kilomerrage = kilomerrage

    def se_presenter(self):
        print(f"la marque: {self.marque},l'annee de sortie est : {self.annee},avec une vitesse maximale de : {self.vitesse}.et un kilometrage de :{self.kilomerrage}")

v1 = Voiture("TOYOTA","2004","180",200000)
v2 = Voiture("KIA","2014","220",160000)

v1.se_presenter()
v2.se_presenter()

