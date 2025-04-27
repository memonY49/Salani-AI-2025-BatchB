

def factorial(n):
    fact = 1
    for i in range(n,0,-1):
        fact = fact * i
    return fact



def fabonacci(n):
    a = 0
    b = 1
    print(a,b,sep = ",", end=",")
    for i in range(0,n):
        c = a+b
        a = b
        b = c
        if c > n:
            break
        print(c,end = ",")

def series(n):
    a = 0
    b = 1
    c = a+b
    print(a,b,sep = ",", end=",")
    for i in range(0,n):
        print(c,end = ",")
        c=c*2
        if c > n:
            break
        

def minvalue(List1):
    minvalue = List1[0]
    minlocation = 0
    """
    for i in range(0,len(List1)):
        if List1[i] < minvalue:
            minvalue = List1[i]
            minlocation = i
    """
    for element in List1:
        if element < minvalue:
            minvalue = element
            minlocation = List1.index(minvalue)
    return minlocation


while True:
    try:
        a = [22000000000000000000000,55,3,6,77,9,1,44,7]
        #fabonacci(int(input("Enter range: ")))
        print(minvalue(a))
        break
    except:
        print("Invailed Number!!")



#0,1,1,2,4,8,16,32,64,128,256,...

#task : Create a fuction to find min value in a list return index
        #(do not use list.min())






