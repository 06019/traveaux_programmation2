class Operation :
    def __init__(self,n1,n2):
        self.nombre1 = n1
        self.nombre2 = n2
    def somme (self):
        return self.nombre1 + self.nombre2
    def soustraction (self):
        return self.nombre1 - self.nombre2
    def multiplication (self):
        return self.nombre1 * self.nombre2
    def division (self):
        if(self.nombre2 == 0):
            print("veuillez saisir un nombre non nul")
            return None
        return self.nombre1 / self.nombre2




a1 = Operation(1,0)

print (f"la somme des deux nombres est : {a1.somme()} ")
print (f"la soustraction  de n1 - n2 est : {a1.soustraction()} ")
print(f"la multiplication  des deux nombres est : {a1.multiplication()} ")
print(f"le cotient de a1 sur a2  est : {a1.division()} ")

