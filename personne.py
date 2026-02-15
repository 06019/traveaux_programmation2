class Personne:
    def __init__(self, n,p,a=18):
        self.nom = n
        self.prenom = p
        self.age = a
    def se_presenter(self):
        print(f"nom:{self.nom},prenom : {self.prenom},age : {self.age}")
    def verifie_age(self):
        if self.age >= 18:
            print(f"Age : {self.age},vous etes majeur")
        else:
            print ("vous etes mineur")

p1=Personne("mehdioui","ferhat",15)
p2=Personne("riad","mahrez",)
p1.se_presenter()
p2.se_presenter()
p1.verifie_age()