import math

c = float(input("Ingrese el lado a correspondiente al angulo a buscar: "))
a = float(input("Ingrese el lado a: "))
b = float(input("Ingrese el lado b: "))

angulo = math.degrees(math.acos((pow(a,2) + pow(b,2) - pow(c,2)) / (2*a*b)))
print (str(angulo) + " grados.")