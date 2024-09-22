'''
4.Se ingresan un máximo de 5 números o hasta que el usuario ingrese el número 0. Mostrar la suma y promedio de los mismos.

'''

acumulador_suma = 0
contador = 0

for i in range (5):
    numero = int(input("Ingrese un numero: "))
    acumulador_suma += numero
    contador += 1
    if numero == 0:
        break

#Ver suma y promedio



promedio = acumulador_suma / contador

print(f"""
La suma de los numeros es: {acumulador_suma}
El promedio de los numeros es: {promedio}
""")





