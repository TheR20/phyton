"""
def addNumber(x):
    result=x+x
    return result

print(addNumber(5))


#get an input
name = input("wahts ur name?")
print("your name is", name)
"""
#retunr diferent results

from tokenize import Double


def multiplyFunc(x,y):
    suma= x+y
    resta=x-y
    divi= x/y
    return suma, resta, divi

print(multiplyFunc(1,1))

#lambda anonymous
x= lambda i: i +11
print(x(5))

x= lambda i, y, z: i + +y +z
print(x(1,1,1))
##########
def new(i):
    return lambda a:a*i

double = new(2)
print(double(5)) #10

#scope of the function
#crear una variable global que este desde dentro de una funcion

y = 10
def new():
    global x
    x= 20
    y= 20
    print(x, y)

new() #20, 20
print(x, y) #20, 10 
