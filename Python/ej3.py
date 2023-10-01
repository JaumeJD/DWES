#Dados los catetos de un triangulo rectangulo, calcular su hipotenusa.
import math

c1 = float(input("Primer cateto:"))
c2 = float(input("Segundo cateto:"))

hipotenusa = math.sqrt(c1 ** 2 + c2 ** 2)

print("%.2f"%hipotenusa)