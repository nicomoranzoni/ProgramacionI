arreglo_numeros = [0,0,0,0,0]

seguir = "si"

print(f"Array antes de agregan elementos: {arreglo_numeros}")

while seguir == "si":
    
    #1. Pido el numero
    numero_aux = int(input("Ingrese un numero: "))
    #2. Pido donde quiero guardar el numero
    indice = int(input("Ingres el indice donde va a guardar el dato: "))
    while indice >= len(arreglo_numeros) or indice < 0:
        indice = int(input("Indice ingresado fuera de rango, reingrese un indice valido: "))

    #3. Guardo el numero
    arreglo_numeros[indice] = numero_aux
    
    seguir = input("Desea seguir ingresando numeros?: ")

print(f"Array luego de agregar elementos: {arreglo_numeros}")