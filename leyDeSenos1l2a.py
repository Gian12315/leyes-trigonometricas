import math
print ("Ingrese primer los lados con la relacion: ")
a = float(input("Ingrese angulo a: "))
lado = float(input("Ingrese el lado: "))

b = float(input("Ingrese angulo b: "))
c = (math.sin(math.radians(b)) * lado) / math.sin(math.radians(a))
print(str(c) + "unidades.")