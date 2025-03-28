# #Task: perform basic mathematical operations (+,-,,/,//,%,*) using def function and lambda functions


##single way by giving user input on time and calling the function we want.
num1 = int(input("Please enter first number : "))
num2 = int(input("please enter second number : "))
def addition(n1,n2):
    return n1+n2
def sub(n1,n2):
    return n1 - n2
def multiplication(n1,n2):
    return n1*n2
def division(n1,n2):
    return(n1/n2)
def floordivision(n1,n2):
    return n1//n2
def modulo(n1,n2):
    return(n1%n2)
def squareroot(n1):
    return n1**2
#calling all functions
print("Addition of ",num1," and ", num2 ," = ",addition(num1,num2))
print("subraction of",num1, "and ",num2,"= ",sub(num1,num2))
print("multiplication of ",num1, "and",num2,"=",multiplication(num1,num2))
print("division of ", num1,"and ",num2,"= ",division(num1,num2))
print("floor division of",num1,"and ",num2, "= ", floordivision(num1,num2))
print("modulo of" , num1,"and",num2,"= ",modulo(num1,num2))
print("Squareroot of", num1," = ",squareroot(num1))

# indivisual function of each operator
#Addition using function
print("Addition using function")
add1 = int(input("please enter first number : "))
add2 = int(input("please enter second number : "))
def addition(a1,a2):
    print(a1+a2)
    return a1+a2
addition(add1,add2)

#Subraction
print("Subraction")
sub1 = int(input("please enter first number"))
sub2 = int(input("please enter second number"))
def sub(s1,s2):
    print(s1-s2)
    return s1-s2
sub(sub1,sub2)

#Multiplication
print("Multiplication")
mul1 = int(input("please enter first number"))
mul2 = int(input("please enter second number"))
def mul(m1,m2):
    print(m1*m2)
    return(m1*m2)
mul(mul1,mul2)

#Division
print("Division")
div1 = int(input("please enter first number"))
div2 = int(input("please enter second number"))
def div(d1,d2):
    print(d1/d2) 
    return d1/d2
div(div1,div2)

# Floor Division
print("Floor Division")
fdiv1 = int(input("please enter first number"))
fdiv2 = int(input("please enter second number"))
def Floordivision(fd1,fd2):
    print(fd1//fd2)
    return(fd1//fd2)
Floordivision(fdiv1,fdiv2)

#Modulo
print("Modulo")
mod1 = int(input("please enter first number"))
mod2 = int(input("please enter second number"))
def modulo(md1,md2):
    print(md1%md2)
    return(md1%md2)
modulo(mod1,mod2)

Exponentiation
print("Exponentiation or square root")
sqr1 = int(input("please enter first number"))
def squareroot(sr1):
    print(sr1**2)
    return sr1**2
squareroot(sqr1)



