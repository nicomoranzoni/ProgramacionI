'''
1.Crear una función que reciba dos números (acumulador y contador) y calcule el promedio, en caso de que haya división por cero imprimir un mensaje de error y retornar 0.

'''

def calcular_promedio (acumulador : float, contador: float)-> float:

    '''
    - Funcion que se encarga de calcular el promedio
    - Recibe un acumulador y un contador
    - Retorna un promedio del los parametros recibidos.
    '''

    if contador == 0:
        print("No es posible dividir por 0")
        return 0
    else:
        promedio = acumulador/contador
        return promedio

print(f"El promedio es {calcular_promedio(100,50)}")
print(f"El promedio es {calcular_promedio(100,0)}")
