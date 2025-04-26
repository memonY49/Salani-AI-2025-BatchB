"""UserData = [{"Name":"abc",
             "Email":"abc@gmail.com",
             "Phone":"023897863",
             "Pass": "abc123"},
            {"Name":"abc1",
             "Email":"abc1@gmail.com",
             "Phone":"023897863",
             "Pass": "abc123"},
            {"Name":"abc2",
             "Email":"abc2@gmail.com",
             "Phone":"023897863",
             "Pass": "abc123"}]

def getUser(Email, Data):
    for user in Data:
        if user["Email"] == Email:
            return user
    else:
        return None

userinemail = input("Enter Email")
userinpass = input("Enter Pass")

userSearch = getUser(userinemail, UserData)

if userSearch != None:
    if userSearch["Pass"] == userinpass:
        print(userSearch)
    else:
        print("Password Not match")
else:
    print("User Not Found")
"""
"""
def area(l,w):
    return l*w
def volume(l,w,h):
    return l*w*h


print("1.Area")
print("2.Volumn")

userin = int(input("ENter your selection: "))
if userin == 1:
    length = int(input("Enter Length: "))
    width = int(input("Enter Width: "))

    results = "Area of {0} and {1} = {2}".format(length,width,area(length,width))
    
    print(results)
elif userin == 2:
    length = int(input("Enter Length: "))
    width = int(input("Enter Width: "))
    height = int(input("Enter Height: "))
    results = "Volumn of {0} , {1} and {2} = {3}".format(length,width,height,volume(length,width,height))
    
    print(results)
"""

"""
name = "Yasir"
Age = 28

message = f'My name is {name} and \' my age is {Age} \' '

print(message)
"""

import math

def find_distance(p1,p2):
    #a = (p2[0] - p1[0])**2
    a = math.pow(2,(p2[0] - p1[0]))
    b = math.pow(2,(p2[1] - p1[1]))
    result = math.sqrt(a+b)
    return result

x1 = 2
y1 = 3
x2 = 4
y2 = 3
print(math.dist((x1,y1),(x2,y2)))
print(find_distance((x1,y1),(x2,y2)))





    


























