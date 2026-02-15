class Rectangle:
    def __init__(self,x,y):
        self.langueur = x
        self.largeur = y
    def Surface(self):
        return (self.largeur * self.langueur)
v1 = Rectangle(10,20)
v2 = Rectangle(2,4)

print(f"la surface de v1 est : {v1.Surface()}")
print(f"la surface de v2 est : {v2.Surface()}")
