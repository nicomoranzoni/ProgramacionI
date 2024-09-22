'''
Necesitamos un sistema que me permita cargar las notas de los alumnos en la universidad hasta que el usuario quiera. (1 al 10)
Mostrar la suma y el promedio de esas notas
Mostrar cada una de las notas cargadas

'''

'''
Explicacion Append
lista_numeros = [5,6,7]
print(lista_numeros)

#Para agregar numero a la lista utilizo metodo append, agrega de manera ordenada 

lista_numeros.append(10)
lista_numeros.append(20)
lista_numeros.append(5)

print(lista_numeros)

#Puedo tambien tener un Array vacio e ir agrenadole elementos

lista_numeros_dos = []
lista_numeros_dos.append(20)
lista_numeros_dos.append(10)
lista_numeros_dos.append(5)

print(lista_numeros_dos)'''



notas_alumnos = []

suma_notas = 0 #Acumulador

seguir = "si"

print(f"Notas antes de la carga: {notas_alumnos}")


while seguir == "si":
    
    nota_aux = int(input("Ingrese una nota (Entre 1 y 10): "))
    
    while nota_aux > 10 or nota_aux < 1:
        nota_aux = int(input("Error. Reingrese una nota (Entre 1 y 10): "))

    #notas_alumnos [i] = nota_aux
    notas_alumnos.append(nota_aux) #Voy agregando a la lista las notas que ingresa el usuario
    suma_notas += nota_aux

    
    seguir = input("Desea seguir ingresando numeros?")


print(f"Notas despues de la carga: {notas_alumnos}")

print(f"La suma de las notas es de: {suma_notas}")

promedio_notas = suma_notas / len(notas_alumnos)

print(f"El promedio de las notas de los almunos es: {promedio_notas}")

#Muestro el total de las notas
for nota in notas_alumnos:
    print(f"La nota de fue: {nota}")


