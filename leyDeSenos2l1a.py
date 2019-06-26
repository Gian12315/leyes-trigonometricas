import math
print ("Ingrese primer los lados con la relacion.")
a = float(input("Ingrese angulo a:"))
lado = float(input("Ingrese el lado a:"))

ladob = float(input("Ingrese lado b:"))
c = math.degrees(math.asin((math.sin(math.radians(a)) * ladob) / lado))
print(str(c) + "grados.")