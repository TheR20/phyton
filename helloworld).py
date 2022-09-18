#a=input('first name  ')
#b=input('second name  ')
#c=a+b
#print(c)

#Iterador de frutas
#fruitstup=('lemon','Orange')
#newit = iter(fruitstup)
#print los elementos, por cada next da un valor 
#print(next(newit)) #lemon
#print(next(newit)) #Orange

#Iteradores 2 
#fruitstr ='orange'
#newit = iter(fruitstr)
#print(next(newit)) #o
#print(next(newit)) #r
#print(next(newit)) #a
#print(next(newit)) #n
#print(next(newit)) #g
#print(next(newit)) #e

#iteradores 3
#fruitstup=('lemon','Orange')
#loop
#for i in fruitstup:
 #   print(i)

#build iterator to return numbers, start fro m1 and +1 each sequence
class newNumbers:
    def __iter__(self):
        self.a = 10 
        return self 
    def __next__(self):
        if self.a <= 17:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration
  #create Object based on NewNumbers class
newclass = newNumbers()
newiter = iter(newclass)

 #iterate over numbers 
print(next(newiter))
print(next(newiter))

for x in newiter:
    print(x)