#Variable Inmutable
def mi_funcion(numero):
    numero = 10
    print(f"El valor del numero dentro de la funcion es {numero}")
    print(id(numero))

numero_dos = 5

mi_funcion(numero_dos)

print(f"EL valor del numero fuera de la funcion es: {numero_dos}")
print(id(numero_dos))
#Ambas variables numero y numero_dos al tener el mismo valor estan guardadas en el mismo espacio de memoria (Pasaje por referencia)

#Variable Mutables
def mi_funcion(numero):
    numero[0] = 10 
    print(f"El valor del numero dentro de la funcion {numero}")
    print(id(numero))

numero_dos = [5]

mi_funcion(numero_dos)

print(f"EL valor del numero fuera de la funcion es: {numero_dos}")
print(id(numero_dos))
