def contar_apellidos (lista_apellidos_comunes:list)-> None:

    lista_apellidos = []
    for i in range(10):
        apellido = input("Ingrese un apellido: ")
        lista_apellidos.append(apellido)

    for i in range(len(lista_apellidos_comunes)):
        apellido_comun = lista_apellidos_comunes[i]
        contador = 0

        for j in range(len(lista_apellidos)):
            apellido = lista_apellidos[j]
            if apellido == apellido_comun:
                contador += 1 

        mensaje = f"{apellido_comun} se repite {contador} veces"
        print(mensaje)

lista_apellidos_comunes =  ["Lopez", "Gomez", "Fernandez", "Perez", "Martinez" ]
contar_apellidos(lista_apellidos_comunes)