file = open("files/main.txt", "r")
print(file.read()) #si pones u numero dentro del read te da ese numero de lineas 
print(file.readline()) #te da solo el primer readline

file.close()