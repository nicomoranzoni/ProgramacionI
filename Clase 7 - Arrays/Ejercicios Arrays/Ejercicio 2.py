'''
2. Escribir una función parecida a la anterior, pero la misma deberá calcular y devolver el promedio de los números positivos. En caso de no haber números positivos validar división por cero

'''

def calcular_promedio_positivos (lista_enteros):
    suma_elementos = 0 
    cantidad_positivos = 0
    
    for elemento in lista_enteros:
            if elemento > 0:
             suma_elementos += elemento
             cantidad_positivos += 1

    if cantidad_positivos < 1:
        promedio = "Error, no hay positivos en la lista"
    else: 
        promedio = suma_elementos/cantidad_positivos

    return promedio


lista_enteros = [1,4,-4,-5,4]

print(f"El promedio de los numeros positivos de la lsita es: {calcular_promedio_positivos(lista_enteros)}")

