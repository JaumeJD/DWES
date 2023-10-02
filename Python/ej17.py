horas = int(input('Introduce las horas de la salida: '))
minutos = int(input('Introduce los minutos de la salida: '))
segundos = int(input('Introduce los segundos de la salida: '))

horaDeSalidaEnSeg = horas * 3600 + minutos * 60 + segundos

duracionViajeEnSeg = int(input('¿Cuántos segundos dura su viaje? '))

horaDeLlegadaEnSeg = horaDeSalidaEnSeg + duracionViajeEnSeg

horasLlegada = horaDeLlegadaEnSeg // 3600

minutosLlegada = (horaDeLlegadaEnSeg % 3600) // 60

segundosLlegada = (horaDeLlegadaEnSeg % 3600) % 60

print("Hora de llegada:")
print(str(horasLlegada)+":"+str(minutosLlegada)+":"+str(segundosLlegada))

