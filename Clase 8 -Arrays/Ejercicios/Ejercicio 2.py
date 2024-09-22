'''
Escribir una función que reciba como parámetro una lista de str y retorne una nueva lista con los elementos de más de cinco caracteres.
'''

def retornar_nueva_lista (lista_str:str)->list:

    lista_nueva_cinco_caracteres = []
    if type (lista_str == list):
        for elemento in lista_str:
            if len(elemento) > 5:
                lista_nueva_cinco_caracteres.append(elemento)
        return lista_nueva_cinco_caracteres
    else:
        return "Error, no se recibió un Array"

lista_str = ["Vaso", "Monitor", "Tele", "Teclado"]
print(f"Los elementos de la lista de mas de 5 caracteres son: {retornar_nueva_lista(lista_str)}")

