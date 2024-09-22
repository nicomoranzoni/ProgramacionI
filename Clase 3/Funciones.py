def calcular_precion_con_iva (importe_sin_iva : float , iva: float = 21)-> float: #Definicion (Entrada)

    '''
    Documentar la funcion:
    - Que hace la funcion: Funcion que se encarga de calcular un importe con IVA
    - Que recibe (Entradas): Recibe el importe sin IVA y el porcentaje de IVA (opcional) - Por defecto es 21%
    - Que retorna (Salidas): Retorna el importe con el IVA incluido. 
    '''

    #Desarrollo
    resultado = importe_sin_iva * (1 + (iva / 100))#Proceso, la variebale resultado es una variable local
    return resultado #Salida - Return nos da una salida

#Llamada - Creo una variable para llamar la funcion 
precio_con_iva = calcular_precion_con_iva(1000) #El primer parametro seria el valor sin IVA, si no coloco paramentro opcional mantiene el orginal
print(f"El precio con iva es {precio_con_iva}")

precio_con_iva = calcular_precion_con_iva(1000,10) #Aca modifico el valor del parametro opcional, en vez de 21 pasa a ser 10
print(f"El precio con iva es {precio_con_iva}")
