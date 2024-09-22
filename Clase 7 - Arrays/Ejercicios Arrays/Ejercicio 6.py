'''
6.Escribir una función que reciba como parámetros una lista de enteros y retorne todos los índices del del valor máximo encontrado (Puede haber más de uno)

Ejemplo [2,5,5,3,1] -> Retorna el índice [1,2]

'''

def calcular_indices_maximos (lista_enteros:list):

    maximo = lista_enteros[0] #Determino el maximo en 0 con el arranque de la lista
    lista_indices = [] # Creo una lista para ir asignando los indices maximos 

    for i in range(len(lista_enteros)): #recorro la lista de enteros 
        if lista_enteros[i] > maximo: #Si el valor del elmento de la lista es mayor al maximo guardado
            maximo = lista_enteros[i] #Guardo el elemento en la variable maximo
            lista_indices = [i] #Reinicio la lista de indicies almacenando el indice donde se encuentra el valor maximo 
        elif lista_enteros[i] == maximo: #Si el valor del elemento de la lista es igual al valor guardado en el maximo
            lista_indices.append(i) #Agrego con append a la lista de indices 

    return lista_indices

lista_enteros = [2,3,5,5,2,1]

print(f"Los indices de valor maximo encontrados son: {calcular_indices_maximos(lista_enteros)}")



