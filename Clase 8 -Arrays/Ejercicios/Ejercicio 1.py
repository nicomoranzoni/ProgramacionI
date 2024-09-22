'''
1. Escribir una función que reciba como parámetro una lista de str y cuente la cantidad de elementos con más de cinco caracteres.
Para contar los caracteres de un string también se usa la función len

'''

def contar_elementos (lista_str):
    contador = 0

    for elemento in lista_str:
        if len(elemento) > 5:
            contador += 1
    
    return contador

lista_str = ["Hola", "Computadora", "Monitor", "vaso"]
print(f"La cantidad de elementos con mas de 5 caracteres son: {contar_elementos(lista_str)}")