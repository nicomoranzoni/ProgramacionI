def mi_funcion ():
    numero = 5 # Numero es una variable local (se crea dentro de la funcion) de una funcion -> mi_funcion
    texto = "Hola"
    print(f"Variable texto dentro de la funcion: {texto}")

texto = "Hola Mundo" #Es una variable global (se crea fuera de la funcion) por ende yo puedo acceder a ella por fuera de mi funcion 

mi_funcion()

print(f"variable texto fuera de la funcion: {texto}")