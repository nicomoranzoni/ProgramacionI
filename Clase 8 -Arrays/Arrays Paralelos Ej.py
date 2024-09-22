#Cargar secuencialmente 3 alumnos de manera algoritmica (sin append)

lista_nombres = [0,0,0]
lista_apellidos = [0,0,0]
lista_edades = [0,0,0]
lista_legajos = [0,0,0]

for i in range(len(lista_nombres)):
    print("---------Ingreso de alumnos-----------")
    #Ingreso los datos
    nombre = input("Ingrese nombre de alumno: ")  
    apellido = input("Ingrese apellido de alumno: ")  
    edad = int(input("Ingrese edad de alumno: ")  )
    legajo = int(input("Ingrese legajo de alumno: "))   

    #Cargo los datos
    lista_nombres[i] = nombre
    lista_apellidos[i] = apellido
    lista_edades[i] = edad
    lista_legajos[i] = legajo

for i in range (len(lista_nombres)): #Como muestro datos
    print("Alumno: ")

#     nombre_aux = lista_nombres[i]
#     apellido_aux = lista_apellidos[i]
#     edad_aux = lista_edades[i]
#     legajo_aux = lista_legajos[i]

    print(f"""
Nombre: {lista_nombres[i]}
Apellido: {lista_apellidos[i]}
Edad: {lista_edades[i]}
Legajo: {lista_legajos[i]}
""")

#-------------------------------------APPEND    
##Cargar secuencialmente 3 alumnos de manera algoritmica (con append)

lista_nombres = []
lista_apellidos = []
lista_edades = []
lista_legajos = []

for i in range(3):
    print("---------Ingreso de alumnos-----------")
    #Ingreso los datos
    nombre = input("Ingrese nombre de alumno: ")  
    apellido = input("Ingrese apellido de alumno: ")  
    edad = int(input("Ingrese edad de alumno: ")  )
    legajo = int(input("Ingrese legajo de alumno: "))   

    #agrego los datos (appendear)
    lista_nombres.append(nombre)
    lista_apellidos.append(apellido)
    lista_edades.append(edad)
    lista_legajos.append(legajo)

for i in range (len(lista_nombres)): #Como muestro datos
    print("Alumno: ")

#     nombre_aux = lista_nombres[i]
#     apellido_aux = lista_apellidos[i]
#     edad_aux = lista_edades[i]
#     legajo_aux = lista_legajos[i]

    print(f"""
Nombre: {lista_nombres[i]}
Apellido: {lista_apellidos[i]}
Edad: {lista_edades[i]}
Legajo: {lista_legajos[i]}
""")