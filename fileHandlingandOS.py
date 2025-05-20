#
# Myfile = open("abc2.txt","r")
# #
#
# for line in Myfile.readlines():
#     userdetails = line.replace("\n","").split(",")
#     print(f"Name: {userdetails[0]}\nFName: {userdetails[1]}\nPhone: {userdetails[2]}\nCNIC: {userdetails[3]}")

# print(Myfile.readlines())


# str1 = "abc Def ahi"

# print(str1.capitalize())
# print(str1.upper())
# print(str1.lower())
# print(str1.count("E"))
# print(str1.endswith("ghiEa"))
# print(str1.find("E"))
# # print(str1.index("a"))
# print(str1.isalnum())
# print(str1.isalpha())
# print(str1.isnumeric())
# print(str1.isupper())
# print(str1.split(" "))
# print(str1.lstrip())
# print(str1.title())
# print(str1.istitle())
# print(str1[-2:])
# print(str1.replace("def","yasir"))
# print(str1.swapcase())




# myFile = open("abc2.txt","r")
# userin = input("Enter your email: ")
# userpassin = input("Enter your password: ")
#
# TotalUsers = [line.replace("\n","").split(",") for line in myFile.readlines()]
#
# for user in TotalUsers:
#     if user[4] == userin and user[5] == userpassin:
#         print(f"Name: {user[0]}\nFName: {user[1]}\n"
#                       f"Phone: {user[2]}\nCNIC: {user[3]}\n"
#                       f"Email: {user[4]}")
#
#
# myFile.close()
# print(TotalUsers)


# for line in myFile.readlines():
#     userdetails = line.replace("\n","").split(",")
#     if userin == userdetails[4] and userpassin == userdetails[5]:
#         print(f"Name: {userdetails[0]}\nFName: {userdetails[1]}\n"
#               f"Phone: {userdetails[2]}\nCNIC: {userdetails[3]}\n"
#               f"Email: {userdetails[4]}")

# with open("abc2.txt",'r') as myfile:
#     print(myfile.readlines())
#     myfile.seek(0)
#     print(myfile.readlines())


import os

current_dirt = os.getcwd()

# os.mkdir("dataset")
#
# os.chdir('dataset')
# os.rename('database','dataset')
# os.mkdir('A')
# os.mkdir('B')
# os.mkdir('C')

# os.rmdir('D:\\testScripts\\myNewProject\\dataset')
# os.remove('abc7.txt')
# for dirt in os.walk('dataset'):
#     # print(dirt)
#     print(f"Path: {dirt[0]}")
#     print(f"Folders: {dirt[1]}")
#     print(f"Files: {dirt[2]}")
#     print("*"*30)


mypath = os.path.join(os.getcwd(),"database.java")

# print(os.path.splitext('image.png'))

cd = os.getcwd()
listdirt = os.listdir()
print(listdirt)
for dirt in listdirt:
    if os.path.splitext(dirt)[1] == '.txt':
        newpath = os.path.join(cd,dirt)
        print(os.path.split(newpath))




































