'''
Necesitamos un sistema que me permita cargar las notas de 5 alumnos en mi universidad. (1 al 10)
Mostrar la suma y el promedio de esas notas
Mostrar cada una de las notas cargadas

'''

notas_alumnos = [0,0,0,0,0]

suma_notas = 0 #Acumulador

print(f"Notas antes de la carga: {notas_alumnos}")
#Carga secuencial
for i in range(len(notas_alumnos)):
    nota_aux = int(input("Ingrese una nota (Entre 1 y 10): "))
    
    while nota_aux > 10 or nota_aux < 1:
        nota_aux = int(input("Error. Reingrese una nota (Entre 1 y 10): "))

    notas_alumnos [i] = nota_aux

    suma_notas += nota_aux



print(f"Notas despues de la carga: {notas_alumnos}")

print(f"La suma de las notas es de: {suma_notas}")

promedio_notas = suma_notas / len(notas_alumnos)

print(f"El promedio de las notas de los almunos es: {promedio_notas}")

#Muestro el total de las notas
for nota in notas_alumnos:
    print(f"La nota de fue: {nota}")
