horas = int(input('Introduce las horas de la salida: '))
minutos = int(input('Introduce los minutos de la salida: '))
segundos = int(input('Introduce los segundos de la salida: '))

duraciónViaje = int(input('¿Cuántos segundos dura su viaje? '))

horasEnSegundos = horas * 3600

minutosEnSegundos = minutos * 60

horaDeSalida = horasEnSegundos + minutosEnSegundos + segundos

horaDeLlegadaEnSeg = horaDeSalida + duraciónViaje

horasLlegada = horaDeLlegadaEnSeg // 3600

minutosLlegada = (horaDeLlegadaEnSeg % 3600) // 60

segundosLlegada = (horaDeLlegadaEnSeg % 3600) % 60

print("Hora de llegada:")
print(str(horasLlegada)+":"+str(minutosLlegada)+":"+str(segundosLlegada))

