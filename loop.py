x =1 

while x<7:
    x+=1
    if x == 5:
        continue #do not show number 5 
    print(x)
    
color = ["red","orenga"]
for colorines in color:
    print("the color is", colorines)
    for letras in colorines:
        print("la letras son", letras)
        if x == "e":
            break

for x in range(2,7):
    print(x)

for x in range(2,12,2): #incrementos de 2 en 2 
    print(x)
else:
    print("The loop has finished")
    