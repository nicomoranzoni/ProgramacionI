lista_nombres = ["Mariano","Gonzalo","German", "David", "Yanina"]

nombre_ingresado = input("Ingrese un nombre: ")

bandera = False #No encontró el dato

for i in range (len(lista_nombres)):
    if lista_nombres[i] == nombre_ingresado:
        bandera = True #Se encontró el dato
        break
    
if bandera == True:
    print("Se encontró el dato")
else:
    print("No se encontró el dato")

print("------------------------Otro ejemplo-----------------------------------")

#SISTEMA QUE PERMITE CONTAR LA CANTIDAD DE VECES QUE SE REPITE UN DATO 
lista_nombres = ["Mariano","David","Gonzalo", "David", "Yanina", "David", "German"]
contador = 0

nombre_ingresado = input("Ingrese un nombre: ")

for nombre in lista_nombres:
    if nombre == nombre_ingresado:
        contador += 1

if contador == 1:
    print(f"El nombre {nombre_ingresado} se repite {contador} vez")
else:
    print(f"El nombre {nombre_ingresado} se repite {contador} veces")


print("------------------------Otro ejemplo-----------------------------------")
#COMPARACION DE DOS LISTAS
lista_nombres_profes = ["Mariano","David","Gonzalo"]
lista_nombres_alumnos = ["Juan","Gonzalo","Maria", "Patricia"]

#recorro lista profes
for nombre_profe in lista_nombres_profes: 
    #Recorro demtro los alumnos
    for nombre_alumno in lista_nombres_alumnos:
        if nombre_profe == nombre_alumno:
            print(f"El profe {nombre_profe} tambien es alumno")
            break
#-------------------Otra forma de comparacion-----------------------------------
for i in range (len(lista_nombres_profes)):
    for j in range(len(lista_nombres_alumnos)): #la j es el indice de la segunda lista (alumnos en este caso)
        nombre_profe = lista_nombres_profes[i]
        nombre_alumno = lista_nombres_alumnos[j]
        if nombre_profe == nombre_alumno:
            print(f"El profe {nombre_profe} tambien es alumno")
            break
        
