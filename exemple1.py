class Voiture:
    def __init__(self, marque,couleur):
        self.marque = marque
        self.couleur = couleur
    def affiche(self):
        print(f"marque :{self.marque} , couleur :{self.couleur}")

v1 = Voiture("toyota","grise")
v2 = Voiture("ford","blanche")
v3 = Voiture("fiat500","rouge")

v1.affiche()
v2.affiche()
v3.affiche()