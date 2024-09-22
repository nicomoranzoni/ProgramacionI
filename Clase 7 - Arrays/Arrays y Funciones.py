def mi_funcion (arreglo_numeros):
    mi_arreglo = [1,2,3]

    arreglo_numeros[0] = 10
    arreglo_numeros[4] = 10
    
    #en las funciones de Arrays no hace falta retornar el Array (Arreglo) que paso x parametro 
    #Si el Array/Arreglo se creo dentro de la funcion y no se pasó como parametro, si puedo retornarlo para no perder su valor cuando la funcion termine
    return mi_arreglo


arreglo_numeros = [1,2,3,4,5]

print(f"arreglo_numeros antes de la funcion: {arreglo_numeros}")

mi_funcion(arreglo_numeros)



print(f"arreglo_numeros despues de la funcion: {arreglo_numeros}")

