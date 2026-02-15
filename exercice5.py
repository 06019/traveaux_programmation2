class Utilisateur:
    def __init__(self, id,nom,prenom,email,mot_pass=None,etat_connexion=False):
        self.identifiant = id
        self.nom = nom
        self.prenom = prenom
        self.email = email
        self.mot_pass = mot_pass
        self.etat_connexion = etat_connexion

    def connecter(self):
        self.etat_connexion = True
        return True

    def deconnecter(self):
        self.etat_connexion = False
        return False
    def affecter_mot_pass(self,mot_pass):
        if len(mot_pass)<= 6:
            print ("Mot de passe invalide")
            return False
        self.mot_pass = mot_pass
        return True

    def afficher_etat_connexion(self):
        if self.etat_connexion == True:
            print ("Etat : connecte")
        else:
            print ("Etat : deconnecte")
u1=Utilisateur(1,"mehdioui","ferhat","mehdiouiferhat@gmail.com")
u1.affecter_mot_pass(mot_pass="Boreal26")
u1.connecter()
u1.afficher_etat_connexion()
u1.deconnecter()
u1.afficher_etat_connexion()


