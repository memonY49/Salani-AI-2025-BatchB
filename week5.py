

"""
for count in range(0,7):
    print(mylist[count])
"""
"""
count = 10
while True:
    count+=1
    print(count)
    if count == 40:
        break
   """
"""
for count in range(100,0,-2):
    print(count)
"""
"""
for element in mylist:
    print(element)

----*
---* *
--* * *
-* * * *


for row in range(0,3):                          #row = 0,1,2
    for a in range(3,row,-1):
        print(" ",end="")
    for b in range(0,row+1):
        print("* ",end="")
    print()
for row in range(0,3):                          #row = 0,1,2
    for a in range(0,row+1):
        print(" ",end="")
    for b in range(3,row,-1):
        print("* ",end="")
    print()


rows = 5
for row in range(0,rows):
    print(" "*(rows-row),"* "*row)

for row in range(rows,0,-1):
    print(" "*(rows-row),"* "*row)
   """ 

mylist = [{"Name":"abc",
           "Email": "abc@gmail.com",
           "Password":"abc123"},
          {"Name":"abc1",
           "Email": "abc1@gmail.com",
           "Password":"abc123"},
          {"Name":"abc2",
           "Email": "abc2@gmail.com",
           "Password":"abc123"}]


"""
while True:
    status = False
    userin = input("enter your email: ")
    for element in mylist:
        if userin == element["Email"]:
            status = True
            print(element["Name"])
            break
    else:
        print("user not found")
    
    if status:
        break
"""
"""
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    if b == 0:
        return "you can not devide from 0"
    return a/b
def mod(a,b):
    return a%b



print("1: add")
print("2: sub")
print("3: mul")
print("4: div")
print("5: mod")



userin = int(input("Select an option"))

if userin == 1:
    print(add(int(input("Please enter value 1: ")),
              int(input("Please enter value 2: "))))
elif userin == 2:
    print(sub(int(input("Please enter value 1: ")),
              int(input("Please enter value 2: "))))
elif userin == 3:
    print(mul(int(input("Please enter value 1: ")),
              int(input("Please enter value 2: "))))
elif userin == 4:
    print(div(int(input("Please enter value 1: ")),
              int(input("Please enter value 2: "))))
elif userin == 5:
    print(mod(int(input("Please enter value 1: ")),
              int(input("Please enter value 2: "))))


"""


























