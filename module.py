import newModule #as any #puedes renombrar el import piendo despues as y el nombre 
import platform
import math
from newModule import player

newModule.new("Carlos")

x = newModule.player["name"]
print("El nombre es", x)

op = platform.system()
print(op)

print(math.log(10))

print(player["name"])
print(help('modules')) #nombre de todos los modulos.
