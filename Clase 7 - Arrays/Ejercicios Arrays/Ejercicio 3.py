'''

3. Escribir una función que calcule y retorne el producto de todos los elementos de la lista que recibe como parámetro
'''

def calcular_producto (lista_enteros):

    producto_enteros = 1 #Debo iniciar en 1 porque sino siempre sera 0, ya que multiplica por 0

    for elemento in lista_enteros:
        producto_enteros *= elemento
       
    
    return producto_enteros

lista_enteros = [2,4,6]

print(calcular_producto(lista_enteros))