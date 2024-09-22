'''

7.Ingresar un número. Mostrar cada número primo que hay entre el 1 y el número ingresado. Informar cuántos números primos se encontraron.

'''

contador = 0

numero = int(input("Ingrese un numero: "))

for i in range(2, numero + 1):
    es_primo = True
    for num in range (2,i):
        if i % num == 0:
            es_primo = False
            break
    if es_primo:
        contador += 1
        print(f"{i} es primo")

print(f"La cantidad de primos que hay son {contador}")