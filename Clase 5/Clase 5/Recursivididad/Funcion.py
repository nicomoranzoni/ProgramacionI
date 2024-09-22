

'''
Numero Factoreal: Se multiplica el numero en cuestion por todos los anteriores
ej: 5! -> 5*4*3*2*1
8! -> 8*7*6*5*4*3*2*1
Regla: 1! = 1
0! = 1

'''

def funcion_recursiva(numero:int):
        print(numero)
        if numero > 1: 
            funcion_recursiva(numero - 1)

# funcion_recursiva(5)

def calcular_factorial (numero:int) -> int:
    if numero > 1:
        #Calcular factorial
        resultado = numero * calcular_factorial(numero - 1)

        
    else:
        resultado = 1 


    return resultado

print(calcular_factorial(3))

