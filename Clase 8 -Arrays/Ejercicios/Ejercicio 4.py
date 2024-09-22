''''
4. Escribir una función que me permita ingresar por teclado los nombres de 5 personas y almacenarlos en una lista. Retornar una lista con el/los nombres de la personas con el nombre más corto (tener en cuenta más de un mínimo)
'''

# def retornar_nombre_corto (lista_nombres)->list:

#     lista_nombres = []
#     largo_minimo = len(lista_nombres[0])

    
    
#     lista_nombres[i] = nombre





def encontrar_nombre_corto (lista:list)->list:
    nombres_cortos = []

    largo_minimo = len(lista[0])

    for nombre in lista:
        if len(nombre) < largo_minimo:
            nombres_cortos = nombre
            largo_minimo = len(nombre)
        elif len(nombre) == largo_minimo:
            nombres_cortos.append(nombre)
    
    return nombres_cortos

lista = ["Juan", "Pedro", "Nicolas", "Lucas"]

print(encontrar_nombre_corto(lista))