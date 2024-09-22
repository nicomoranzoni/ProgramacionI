'''
3. Realizar una función para calcular el número de Fibonacci (investigar que es) de un número ingresado por consola. La función deberá seguir el siguiente prototipo:

	def calcular_fibonacci (numero:int) -> int:

La sucesión de Fibonacci comienza con los números 0 y 1, y cada número subsecuente es la suma de los dos anteriores:

'''
def calcular_fibonacci (numero:int) -> int:
    if numero > 1:
        #Aca calculo finobacci de manera recursiva
        #Fibonacci(numero) = Fibonacci(numero - 1 ) + Fibonacci (numero - 2)
        resultado = calcular_fibonacci(numero - 1 ) + calcular_fibonacci(numero - 2)
    else: 
        #Caso base 
        resultado = numero
    return resultado

print(calcular_fibonacci(9))



#F(0) -> 0
#F(1) -> 1
#F(2) -> F(0) + F(1) -> 1