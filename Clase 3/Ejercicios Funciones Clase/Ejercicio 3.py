'''
3- Crear una función que verifique si un número es par o no, devuelve True si es par, y False si es impar
'''

def verificar_par (numero: int)->bool:

    '''
    - Se encarga de verificar si un numero es par o no
    - Recibe un numero
    - Retorna True si es par, False si no lo es
    '''

    if numero % 2 == 0 :
        return True
    else:
        return False
    
resultado = verificar_par(7)
 
print(f"El numero es par: {resultado}")
