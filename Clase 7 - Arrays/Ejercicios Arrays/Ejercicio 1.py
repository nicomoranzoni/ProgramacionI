'''
1. Escribir una función que reciba una lista de enteros, la misma calculará y devolverá el promedio de todos los números.
'''

def calcular_promedio (lista_enteros):

    suma_elementos = 0
    
    for elemento in lista_enteros:
        suma_elementos += elemento
    
    promedio = suma_elementos / len(lista_enteros)

    return promedio

lista_enteros = [1,2,3,4,5]

print(f"El promedio de la lista es: {calcular_promedio(lista_enteros)}")
