import math

a = float(input("Ingrese lado a: "))
b = float(input("Ingrese lado b: "))
angulo = float(input("Ingrese el angulo: "))
c = math.sqrt(a**2+ b**2 - (2*a*b*math.cos(math.radians(angulo))))
print(str(c) + " unidades.")