#DECISION MAKING STATEMENTS
#Que1
print("to check whether year is leap or not")
year =  int(input("enter an year : "))
if(year % 100) == 0:
    if(year % 400) == 0:
        print(year, "is a leap year")
elif(year % 4) == 0:
        print(year, "is a leap year")    
else:
    print(year, "is not a leap year")
print("\n")

#Que2
print("to check whether it is a square and rectangle")
print("enter the dimensions")
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))
d = int(input("d: "))
if(a==b and b==c and c==d):
    print("it is a square")
elif(a==c and b==d):
    print("it is a rectangle")
else:
    print("it is neither square nor recatngle")   
print("\n")

#Que3
print("youngest and oldest among 3 people")
a = int(input("age of 1st member :"))
b = int(input("age of 2nd member :"))
c = int(input("age of 3rd member :"))
if(a>b):
    if(a>c):
        print("a is oldest")
    else:
        print("c is oldest")
else:
    if(b>c):
        print("b is oldest")
    else:
        print("c is oldest")
if(a<b):
    if(a<c):
        print("a is youngest")
    else:
        print("c is youngest")
else:
    if(b<c):
        print("b is youngest")
    else:
        print("c is youngest")
print("\n")

#Que4
print("employee workplace")
age = int(input("enter your age : "))
sex = input("enter your gender(M/F) : ")
marStatus = input("enter your marital status(Y/N) : ")
if(sex == 'F'):
    print("employee can work in urban areas")
elif(sex == 'M' and age >=20 and age <=40):
    print("employee can work in any area")
elif(sex == 'M' and age >=40 and age <=60):
    print("employee can work in urban area")
else:
    print("ERROR")
print("\n")

#Que5
print("total cost with or without discount")
qty = int(input("enter no. of units : "))
amount = qty * 100
if(amount >=1000):
    total_cost = amount - (10/100)*amount
    print("total cost is : ", total_cost)
else:
    total_cost = amount
    print("total cost is : ", total_cost)
print("\n")

#LOOPS
#Que1
print("print 10 numbers")
i = 0
for i in range(0,10):
    a = int(input("enter the integer :"))
for i in range(0,10):
    print(a, end = "  ")
print("\n")

#Que2
print("infinite loop")
print("At last of the assignment")
print("\n")

#Que3
print("list of integers and print their square")
list1 = []
list2 = []
num = int(input("enter the numbers of elements : "))
print("enter the elements : ")
for i in range(0,num):
    a = int(input())
    list1.append(a)
    b = a*a
    list2.append(b)
print("elements of list are : ", list1)
print("square of elements are : ", list2)
print("\n")

#Que4
print("make different lists for elements with different data type")
myList = ["abc", 2, 3.4, "xyz", 5, 8.9]
print(myList)
p = []
q = []
r = []
for i in range(0,len(myList)):
    if str(myList[i]).isdigit():
        p.append(myList[i])
    elif str(myList[i]).isalpha():
        q.append(myList[i])
    else:
        r.append(myList[i])
print(p,"\n",q ,"\n",r)      
print("\n")        

#Que5
print("prime numbers from 1 to 100")
for a in  range(1,101):
    i = 2
    while i < a:
        b = a % i
        if(b == 0):
            break
        i = i + 1
    if(a == i):
        print(a , end = " ")
print("\n")

#Que6
print("print a pattern")
for i in range(0,5):
    print("\r")
    for j in range (0,i):
        print("*", end = " ")
print("\n")

#Que7
#WITH FOR LOOP
myList = []
num = int(input("enter the number of elements : "))
print("enter the elements : ")
for i in range(0,num):
    a = int(input("\t"))
    myList.append(a)
print(myList)
var = int(input("enter another element : "))
for i in myList:
    if(i == var):
        myList.remove(var)
print(myList)
print("\n")

#WITHOUT USING FOR LOOP
myList = []
num = int(input("enter the number of elements : "))
print("enter the elements : ")
for i in range(0,num):
    a = int(input("\t"))
    myList.append(a)
print(myList)
var = int(input("enter the element to be deleted: "))
if var in myList:
    myList.remove(var)
    print("list after deleting element" , myList)
else:
    print("element not found")
    print(myList)
print("\n")

#Que2
print("infinite loop")
num = 1
while num <=10:
    print(num, end = " ")
print("\n")
