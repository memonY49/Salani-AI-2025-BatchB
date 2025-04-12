my_Showroom = [
        [["Toyota","Corolla1","XLI","2007",1200000],
         ["Toyota","Corolla2","XLI","2007",1200000],
         ["Toyota","Corolla3","XLI","2007",1200000],
         ["Toyota","Corolla4","XLI","2007",1200000],
         ["Toyota","Corolla5","XLI","2007",1200000]],

        [["Suzuki","Mehran1","VXR","2008",500000],
         ["Suzuki","Mehran2","VXR","2008",500000],
         ["Suzuki","Mehran3","VXR","2008",500000],
         ["Suzuki","Mehran4","VXR","2008",500000],
         ["Suzuki","Mehran5","VXR","2008",500000]]
    ]
print("1.",my_Showroom[0][0][0])
print("1.",my_Showroom[1][0][0])

userin = input("Enter company name: ")

if userin == "Toyota":
    print("1.",my_Showroom[0][0][1])
    print("2.",my_Showroom[0][1][1])
    print("3.",my_Showroom[0][2][1])
    print("4.",my_Showroom[0][3][1])
    print("5.",my_Showroom[0][4][1])

    userin = input("Enter Car Name: ")
    if userin == my_Showroom[0][0][1]:
        print("Name: ",my_Showroom[0][0][1])
        print("Model: ",my_Showroom[0][0][2])
        print("Year: ",my_Showroom[0][0][3])
        print("Price: ",my_Showroom[0][0][4])
        
    elif userin == my_Showroom[0][1][1]:
        print("Name: ",my_Showroom[0][1][1])
        print("Model: ",my_Showroom[0][1][2])
        print("Year: ",my_Showroom[0][1][3])
        print("Price: ",my_Showroom[0][1][4])
    
    elif userin == my_Showroom[0][2][1]:
        print("Name: ",my_Showroom[0][2][1])
        print("Model: ",my_Showroom[0][2][2])
        print("Year: ",my_Showroom[0][2][3])
        print("Price: ",my_Showroom[0][2][4])
    
    elif userin == my_Showroom[0][3][1]:
        print("Name: ",my_Showroom[0][3][1])
        print("Model: ",my_Showroom[0][3][2])
        print("Year: ",my_Showroom[0][3][3])
        print("Price: ",my_Showroom[0][3][4])
    
    elif userin == my_Showroom[0][4][1]:
        print("Name: ",my_Showroom[0][4][1])
        print("Model: ",my_Showroom[0][4][2])
        print("Year: ",my_Showroom[0][4][3])
        print("Price: ",my_Showroom[0][4][4])
    
    else:
        print("Invaild Input")
        
elif userin == "Suzuki":
    print("1.",my_Showroom[1][0][1])
    print("2.",my_Showroom[1][1][1])
    print("3.",my_Showroom[1][2][1])
    print("4.",my_Showroom[1][3][1])
    print("5.",my_Showroom[1][4][1])

    userin = input("Enter Car Name: ")
    if userin == my_Showroom[1][0][1]:
        print("Name: ",my_Showroom[1][0][1])
        print("Model: ",my_Showroom[1][0][2])
        print("Year: ",my_Showroom[1][0][3])
        print("Price: ",my_Showroom[1][0][4])
        
    elif userin == my_Showroom[1][1][1]:
        print("Name: ",my_Showroom[1][1][1])
        print("Model: ",my_Showroom[1][1][2])
        print("Year: ",my_Showroom[1][1][3])
        print("Price: ",my_Showroom[1][1][4])
    
    elif userin == my_Showroom[1][2][1]:
        print("Name: ",my_Showroom[1][2][1])
        print("Model: ",my_Showroom[1][2][2])
        print("Year: ",my_Showroom[1][2][3])
        print("Price: ",my_Showroom[1][2][4])
    
    elif userin == my_Showroom[1][3][1]:
        print("Name: ",my_Showroom[1][3][1])
        print("Model: ",my_Showroom[1][3][2])
        print("Year: ",my_Showroom[1][3][3])
        print("Price: ",my_Showroom[1][3][4])
    
    elif userin == my_Showroom[1][4][1]:
        print("Name: ",my_Showroom[1][4][1])
        print("Model: ",my_Showroom[1][4][2])
        print("Year: ",my_Showroom[1][4][3])
        print("Price: ",my_Showroom[1][4][4])
    else:
        print("Invaild Input")
    
else:
    print("Invaild Input")










