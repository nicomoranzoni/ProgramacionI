'''

7. Escribir una función que tome una lista de letras, forme una palabra con estas y la devuelva.

'''

def formar_palabra (lista_letras:list)-> str:

    palabra = "".join(lista_letras) #el metodo join une las letras que se ingresan por separado en una lista

    return palabra

lista_letras = ["M", "O", "N", "I", "T", "O", "R"]

print(f"La palabra formada por la lista de letras ingresada es {formar_palabra(lista_letras)}")

