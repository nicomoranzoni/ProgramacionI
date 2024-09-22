arreglo_numeros = [0,0,0,0,0]

#Sino tambien puedo hacer arreglo_numeros = [0] * 5 - Funciona solo Python

print("----------------- Carga elementos secuncial -------------------------------")

for i in range(len(arreglo_numeros)): #Determino con un for each la cantidad de elementos que quiero agregar

    #1. Pedir el dato
    numero_aux = int(input("Ingrese un numero: "))
    #2. Agregar el dato al Array
    arreglo_numeros[i] = numero_aux #Agrego el numero a la posicion correspondiente secuencialmente (primer numero ingresado i=0, segundo i=1, etc)

print(arreglo_numeros)

print("----------------- Carga elementos secuncial y mostrar el indice en donde cargo  -------------------------------")
for i in range(len(arreglo_numeros)):
    print(f"Elementos: {arreglo_numeros[i]}, Indice : {i}")