#1. Take an input year from user and decide whether it is a leap year or not.

a=int(input("enter year"))
if(((a%4==0) and (a%100!=0)) or (a%400==0)):
    print(" {} is a leap year".format(a))
else:
    print("{} is not a leap year".format(a))

#Q.2- Take length and breadth input from user and check whether the dimensions are of square or rectangle.

l=input("enter length")
b=input("enter breath")
if(l==b):
    print("square")
elif(l!=b):
    print("rectangle")
    
#Q.3- Take the input age of 3 people and determine oldest and youngest among them.

a=int(input("enter age 1"))
b=int(input("enter age 2"))
c=int(input("enter age 3"))
if(a>b and a>c):
    print("max is %d"%(a))
elif(b>a and b>c):
    print("max is %d"%(b))
elif(c>b and c>a):
    print("max is %d"%(c))
if(a<b and a<c):
    print("min is %d"%(a))
elif(b<a and b<c):
    print("min is %d"%(b))
elif(c<b and c<a):
    print("min is %d"%(c))
    
'''Q.4- Ask user to enter age, sex ( M or F ), marital status ( Y or N ) and then using following rules print their place of service. 

1. if employee is female, then she will work only in urban areas. 
2. if employee is a male and age is in between 20 to 40 then he may work in anywhere 
3. if employee is male and age is in between 40 t0 60 then he will work in urban areas only. 
4. And any other input of age should print "ERROR".'''

a=int(input("enter age"))
b=input("enter sex M or F")
c=input("enter marital status Y or N")
if(b=='F' or b=='f'):
    print("she will work only in urban areas. ")
else:
    if((b=='M' or b=='m') and (a>=20 and a<=40)):
        print(" he may work in anywhere ")
    elif((b=='M' or b=='m') and (a>40 and a<=60)):
        print(" he may work in urban areas only")
    elif((a<20 and a>60)):
        print("ERROR")
    
#Q.5- A shop will give discount of 10% if the cost of purchased quantity is more than 1000.Ask user for quantity Suppose, one unit will cost 100. Judge and print total cost for user. 
a=int(input("enter no of units"))
b=int(input("enter cost"))
c=a*b
if(c>=1000):
    print(c-(c*10/100))
else:
    print("no discount")

    
#####################################################################################################################################################3
                                                  #FOR LOOP#


#Q.1- Take 10 integers from user and print it on screen.
a=[]
c=int(input("enter no of int"))
for i in range(c):
    d=int(input())
    a.append(d)
print(a)

    
#Q.2- Write an infinite loop.An infinite loop never ends. Condition is always true.

a="hello"
while (True):
    print(a)


#Q.3- Create a list of integer elements by user input. Make a new list which will store square of elements of previous list

a=[]
b=[]
c=int(input("enter no of int"))
for i in range(c):
    d=int(input())
    a.append(d)
print(a)
for i in range(c):
    h=a[i]*a[i]
    b.append(h)
print(b)
    
#Q.4- From a list containing ints, strings and floats, make three lists to store them separately

a=[]
m=[]
c=int(input("enter no of int"))
for i in range(c):
    d=input()
    a.append(d)
print(a)
for i in range(c):
    if str(a[i]).isdigit():
        m.append(a[i])
    elif str(a[i]).isalpha():
        n.append(a[i])
print(m)
print(n)


#Q.5- Using range(1,101), make a list containing only prime numbers. 

print("Prime numbers between 1 and 101 are:")

for num in range(1,102):
   # prime numbers are greater than 1
   if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
           print(num)
    

