'''
Escribir una función que reciba una lista de strings y devuelva la cantidad de caracteres que tienen en promedio.

'''

def mostrar_cantidad_caracteres_promedio (lista_str:list):
    contador_caracteres = 0

    if type (lista_str) == list:

        if lista_str != 0:
            for elemento in lista_str:
                contador_caracteres += len(elemento)
            
            promedio = contador_caracteres / len(lista_str)

            return promedio
        else:
            return "Error, Array vacio"
    else:
        return "Error, no se recibó un Array"        
        

lista_str = ["Hola", "Vaso", "Mouse", "Pantalla"]

print(f"La cantidad de caracteres que tiene en promedio es {mostrar_cantidad_caracteres_promedio(lista_str)}")
