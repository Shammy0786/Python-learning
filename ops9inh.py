class Dad:
    basket_ball=3

class Son(Dad):
    basket_ball = 9
    dance=6
    def isdance(self):
        return f"{self.dance} types of dance can do"

class Grandson(Son):
    # dance = 9
    def isdance(self):
        return f" {self.dance} types dance can do awosemly"

darry=Dad()
berry=Son()
jerry=Grandson()
print(berry.isdance())
print(jerry.basket_ball)
