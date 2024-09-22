'''
7. Escribir una función que reciba como parámetros una lista de enteros y muestre la posición del valor máximo encontrado. Reutilizar la función anterior.

Ejemplo [2,5,5,3,1] -> Muestra tanto el índice 1 como el 2 y sus valores

'''

def calcular_indices_maximos (lista_enteros:list):

    maximo = lista_enteros[0] #Determino el maximo en 0 con el arranque de la lista
    indice_maximo = 0 # Creo una lista para ir asignando los indices maximos 

    for i in range(len(lista_enteros)): #recorro la lista de enteros 
        if lista_enteros[i] > maximo: #Si el valor del elmento de la lista es mayor al maximo guardado
            maximo = lista_enteros[i] #Guardo el elemento en la variable maximo
            indice_maximo = [i] #Reinicio la lista de indicies almacenando el indice donde se encuentra el valor maximo 
        elif lista_enteros[i] == maximo: #Si el valor del elemento de la lista es igual al valor guardado en el maximo
            indice_maximo.append(i) #Agrego con append a la lista de indices 

    return f"La posicion del valor maximo es: {indice_maximo} y su valor: {maximo}"

lista_enteros = [2,3,5,5,2,1]

print(calcular_indices_maximos(lista_enteros))