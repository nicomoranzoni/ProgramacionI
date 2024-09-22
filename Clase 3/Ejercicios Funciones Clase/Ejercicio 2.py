'''
Crear una función que calcule el área de un rectángulo. La función recibe la base y la altura y retorna el área.

'''

def calcular_area_rectangulo (base : float, altura: float)-> float:

    '''
    - Funcion que se encarga de calcular el area de un rectangulo
    - Recibe la base y altura
    - Retorna el area del rectangulo
    '''

    area = base * altura
    return area

area_calculada = calcular_area_rectangulo(100,30)
print(f"El area del rectangulo es: {area_calculada}")