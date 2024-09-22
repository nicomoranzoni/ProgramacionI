'''
4.Crear una función que verifique si un primo o no, devuelve True si es primo, False si no lo es

'''

def verificar_primo (numero: int ) -> bool:

    '''
    - Se encarga de verificar si es un numero primo o no
    - Recibe un numero
    - Retorna True si es primo, False si no lo es

    '''

    bandera = True #Si es true el numero es un primo
    for i in range (2,numero,1):
     if numero % i == 0: #Si entra a este IF -> No es primo
        # print(f"{numero} / {i} me da un resultado entero")
        bandera = False # Si la vandera es false el numero no es primo
        break #Coloco un break para que no siga iterando una vez que se que ya no es primo 

    if bandera == True and numero >= 1:
        print(f"El {numero} es primo")
    else:
        print(f"El {numero} no es primo")

def verificar_numero_primo(num):
    if num < 2:
        print(f'{num} no es primo')
        return False
    for i in range(2,num):
        if num % i == 0:
            print(f'{num} no es primo')#No print dentro de la funcion
            return False
    print(f'{num} es primo')#No print dentro de la funcion
    return True

