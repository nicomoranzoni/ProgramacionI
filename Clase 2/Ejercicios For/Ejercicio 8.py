'''
8. Ingresar un número y mostrar la tabla de multiplicar de ese número. 

Por ejemplo si se ingresa el numero 3:
3 x 0 = 0 
3 x 1  = 3
3 x 2 = 6
3 x 3  = 9

'''

numero = int(input("ingrese un numero: "))

for i in range (11):

    resultado = numero * i

    print(f"{numero} * {i} = {resultado}")
