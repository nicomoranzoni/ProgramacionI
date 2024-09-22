'''
5. Escribir una función que reciba como parámetros una lista de enteros y muestre el índice del valor máximo encontrado (no se tienen en cuenta si hay más de un máximo) Reutilizar la función anterior.

Ejemplo [2,5,5,3,1] -> Imprime el índice  1 y su valor

'''

def calcular_indice_maximo (lista_enteros):
    
    indicador_maximo = 0
    maximo = lista_enteros[0]

    for i in range(len(lista_enteros)):
        if lista_enteros[i] > maximo:
            maximo = lista_enteros [i]
            indicador_maximo = i
            valor_maximo = lista_enteros[i]
    
    return f"El indice del valor maximo es {indicador_maximo} y su valor es {valor_maximo}"

lista_enteros = [2,4,2,6,3,1]


print(calcular_indice_maximo(lista_enteros))