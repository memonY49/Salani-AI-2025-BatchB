# class calculator:
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b
#
#     def geta(self):
#         return self.a
#     def getb(self):
#         return self.b
#
#
#
#
# if __name__ == '__main__':
#     mycal = calculator(2,2)
#     mycal2 = calculator(7,6)
#
#     print(mycal.geta())
#     print(mycal2.geta())


class car :
    def __init__(self,color,sunroof,seats,power=600):
        self.v = 4
        self.color = color
        self.doors = 4
        self.seats = seats
        self.gears = 0
        self.sunroof = sunroof
        self.Hpower = power
        self.ac = True
        self.speed = 0
    def turnOn(self):
        print("Engin on")
    def accelerate(self,speed):
        self.speed = speed
    def brack(self):
        self.speed = 0
    def gearChange(self,gear):
        self.gears = gear


mehran = car( sunroof=False,color="Silver")
aulto = car(power=650, seats=4,sunroof=False, color="White")
corola = car(power=1300, sunroof=False,seats=5,color="Black")


mehran.turnOn()
mehran.accelerate(40)
mehran.gearChange(2)

print(corola.color,corola.speed,corola.seats,corola.sunroof)











