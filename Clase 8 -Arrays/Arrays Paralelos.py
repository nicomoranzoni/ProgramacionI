'''
Arrays Paralelos me permiten estructurar informacion mas compleja (x ej toda la informacion de un alumno: nombre, apellido, edad, legajo)
Esta informacon se va a relacionar por un mismo indice
Los arrays paralelos tienen el mismo largo-misma longitud
'''

lista_nombres = ["Mariano", "Gozalo", "German"]
lista_apellidos = ["Fernandez", "Ochoa", "Scarafilo"]
lista_edades = [30,40,50]
lista_legajos = [11111,22222,33333]

#Arrays paralelos solo se pueden recorrer con for i in range

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
    
