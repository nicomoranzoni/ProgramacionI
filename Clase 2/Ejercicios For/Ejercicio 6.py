'''
6.Ingresar un número. Determinar si el número es primo o no.


'''
#Primero decir que todo numero es primo hasta que se demuestre lo contrario

bandera = True #El numero es primo

#12 -> 12/2 -> 6
#12 -> 12/3 -> 4
#12 -> 12/4 -> 3
#12 -> 12/6 -> 2

numero = int(input("Ingrese un numero: "))
#2-3-4-5-6-7-8-9-10-11 Siguiendo ejemplo del 12

for i in range (2,numero,1):
    if numero % i == 0: #Si entra a este IF -> No es primo
        # print(f"{numero} / {i} me da un resultado entero")
        bandera = False # Si la vandera es false el numero no es primo
        break #Coloco un break para que no siga iterando una vez que se que ya no es primo 

if bandera == True and numero >= 1:
    print(f"El {numero} es primo")
else:
    print(f"El {numero} no es primo")