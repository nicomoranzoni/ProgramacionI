'''
6. Escribir una función que pida una cantidad indeterminada de strings al usuario y las almacene en una lista.
'''

def almacenar_str ():
    seguir = "si"
    lista_str =[]

    while seguir == "si": 
        
        str_ingresado = input("Ingrese una palabra deseada: ")

        lista_str.append(str_ingresado)       

        seguir = input("Desea seguir ingresando datos?: ")
    
    return lista_str


print(f"La lista de strings ingresados por el usuario fue: {almacenar_str()}")