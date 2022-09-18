#list
color = ["red","orenga"]
number =[1,2,3]
color.insert(1, "green")
color.append("purple")
colores = ["rojo","naranja"]
color.extend(colores)
print(color)
#color.remove("red")
color.pop(1) #if its empty will delete last item
#del color #delete complete list 
#color.clear() delete all item in a list 

#tuple their items are uncahngeable
colors = ("red","orange")
numbers = (1,2,3)
numeros =( 4,5,6)

allTuples = numbers+numeros
#del tambien borra por completo
print(allTuples)

#sets items are unchangeable and do not allow duplicates
setcolor ={"red","blue"}
for colorines in setcolor:
    print(colorines)
setcolor.add("green")
nuevoscolores ={"purple","black"}
setcolor.update(nuevoscolores)
print("pepino" in setcolor) #return false cos it is not in the set

#dictionary is unordered changeble and does not allow duplicates
newDict = {"key1": "Value1", "key2": "Value2"}
x= newDict.get("key1")
print(x)
y= newDict.keys()
print(y)
w = newDict.values()
z = newDict.items()
if "name" in newDict:
    print("yes")
newDict["key1"] = "cambiado"
newDict.update({"key2": "TambienCambiado"})
newDict.update({"key3": 5, "key4":6})
newDict["key5"] = 20
print(newDict)