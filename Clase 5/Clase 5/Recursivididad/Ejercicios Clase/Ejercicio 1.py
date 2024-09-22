def sumar_naturales (numero:int) -> int:
    if numero == 1: #Caso base -  no hay recursividad -  Siempre tengo un caso base
        return 1
    else:
        resultado = numero + sumar_naturales(numero - 1)
        return resultado
    

print(sumar_naturales(5))