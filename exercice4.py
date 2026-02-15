class Compte :
    def __init__(self,solde=0):
        self.solde = solde
    def deposer(self,montant):
        self.solde += montant
        return self.solde
    def retirer(self,montant):
        self.solde -= montant
        return self.solde
    def affiicher_solde(self):
       print(f"votre solde actuel est: {self.solde}")
c1 = Compte()
c2 = Compte()

c1.deposer(200)
c1.retirer(50)
c1.affiicher_solde()

c2.deposer(400)
c2.retirer(120)
c2.affiicher_solde()

