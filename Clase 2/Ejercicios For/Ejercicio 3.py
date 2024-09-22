'''
3.Ingresar dos números mostrar desde el primer número hasta el segundo que ingresaron de manera ascendente, en caso de que el primer número sea mayor al segundo mostrarlos en orden descendente, si los números son iguales, mostrar sólo ese número.
Por ejemplo: Si ingresaron 5 como primer número y 7 como segundo mostrar (5-6-7), si el primer número que ingresaron es 7 y el segundo un 5 mostrar (7-6-5)

'''

primer_numero = int(input("Ingrese un numero: "))
segundo_numero = int(input("ingrese segundo numero: "))

if primer_numero < segundo_numero:
    for i in range (primer_numero, segundo_numero +1, 1):
        print(i)
elif primer_numero > segundo_numero:
    for i in range (primer_numero, segundo_numero -1, -1):
        print(i)
else:
    print(primer_numero)    


#Otra opcion mas simplificada
primer_numero = int(input("Ingrese un numero: "))
segundo_numero = int(input("ingrese segundo numero: "))
rango = range(primer_numero, segundo_numero -1, -1)


if primer_numero > primer_numero:
    rango = range(primer_numero, segundo_numero -1, -1)
# elif primer_numero <= segundo_numero:
#     rango = range(primer_numero, segundo_numero +1 , -1)

for i in rango:
    print(i)