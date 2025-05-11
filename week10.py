import math
# class Animal :
#     def __init__(self):
#         self.lags = 0
#         self.ears = 0
#         self.eyes = 0
#         self.height = 0.0
#     def sound(self):
#         print(".........")
#     def eat(self,meal):
#         print(f"Eating...{meal}")
#
#     def setlags(self,value):
#         self.lags = value
#     def getlags(self):
#         return self.lags
#
#     def setears(self,value):
#         self.ears = value
#     def getears(self):
#         return self.ears
# class calculate:
#     def add(self,a,b):
#         return a+b
#     # def add(self,a,b,c):
#     #     return a+b+c
#
# class cat (Animal):
#     def sound(self):
#         print("Meow")
#
# class dog (Animal,calculate):
#     def sound(self):
#         print("Bhaw Bhaw")
#
#
#
#
#
#
# #
# #
# cat1 = cat()
# cat1.setlags(4)
# print(cat1.getlags())
# cat1.eat("meat")
#
# #
# # c1 = calculate()
# #
# # result = c1.add(1,2)
# #
# # print(result)
import sys


class Father:
    def __init__(self):
        self.FatherName = ""
        self.age = ""
        self.occupation = ""
        self.height = 0
        self.weight = 0

    def __add__(self,other):
        return "two father classes are added"
    def getFatherName(self):
        return self.FatherName
    def setFatherName(self,value):
        self.FatherName = value


class Mother:
    def __init__(self):
        self.Name = ""
        self.age = ""
        self.occupation = ""
        self.height = 0
        self.weight = 0

    def getName(self):
        return self.Name
    def setName(self,value):
        self.Name = value

class Child(Father,Mother):
    def __init__(self):
        self.Name = ""
        self.age = ""
        self.occupation = ""
        self.height = 0
        self.weight = 0


    def getName(self):
        return self.Name

    def setName(self, value):
        self.Name = value
#
# child1 = Child()
#
# child1.setName("boy")
#
# child1.setFatherName("father")
#
# print(child1.getFatherName())
# print(child1.getName())
#
#
#
#
# while True:
#     userin = int(input())
#     if userin == 0:
#         sys.exit(0)

class calculator:
    def __init__(self):
        self.result = 0
    def add(self, a,b):
        return a+b
    def sub(self,a,b):
        return a-b

c1 = calculator()

# while True:
#     print("1.add\n2.sub\n0.exit")
#     try:
#         userSelection = int(input("Enter Your Selection"))
#         if userSelection == 1:
#             c1.result = c1.add(int(input("Enter First value..")),int(input("Enter First value..")))
#             print(c1.result)
#         elif userSelection == 2:
#             c1.result = c1.sub(int(input("Enter First value..")), int(input("Enter First value..")))
#             print(c1.result)
#         elif userSelection == 0:
#             break
#         else:
#             print("Invalid Selection...!")
#
#     except:
#         print("Invailed Input...")
#         pass
# sys.exit(0)

f1 = Father()
f2 = Father()

print(f1+f1)













