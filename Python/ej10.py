# Un alumno desea saber cual sera su calificacion final en la materia 
# Dicha calificacion se compone de los siguientes porcentajes: 
# * 55% del promedio de sus tres calificaciones parciales.
# * 30% de la calificacion del examen final.
# * 15% de la calificacion de un trabajo final.

import math

# Primer porcentaje

p1 = float(input('Primera calificación parcial: '))
p2 = float(input('Segunda calificación parcial: '))
p3 = float(input('Tercera calificación parcial: '))

mediaParciales = (p1 + p2 + p3) / 3

porcentaje1 = (mediaParciales * 55) / 100

# Segundo porcentaje

exFinal = float(input('Calificacion examen final: '))

porcentaje2 = (exFinal * 30) / 100

# Tercer porcentaje

trabFinal = float(input('Calificacion trabajo final: '))

porcentaje3 = (trabFinal * 15) / 100

# Calificacion final

calFinal = porcentaje1 + porcentaje2 + porcentaje3

print('Tu calificacion final de la asignatura es %.2f' %calFinal)