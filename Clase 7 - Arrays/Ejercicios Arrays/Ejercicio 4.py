'''

4.Escribir una función que reciba como parámetros una lista de enteros y retorne el índice del valor máximo encontrado (retornar un sólo índice, en caso de que haya más de un máximo el primero)

Ejemplo [2,5,5,3,1] -> Retorna el índice 1


'''



def calcular_indice_maximo (lista_enteros):
    
    indicador_maximo = 0
    maximo = lista_enteros[0]

    for i in range(len(lista_enteros)):
        if lista_enteros[i] > maximo:
            maximo = lista_enteros [i]
            indicador_maximo = i
    
    return indicador_maximo

lista_enteros = [2,4,2,6,3,1]

print(f"El indicardor maximo es: {calcular_indice_maximo(lista_enteros)}")



