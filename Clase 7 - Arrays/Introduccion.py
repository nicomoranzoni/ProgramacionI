'''
Arreglo -> estructura de datos que me permite organizar un conjunto de elementos bajo el mismo nombre. 
-> Tendra un conjunto de datos determinados bajo un nombre

2 tipos:
1- Unidimensionales -> Los elementos se organizan uno tras otro en una misma dimensión. Ej Vectores
2- Bidimensionales -> Los elementos se organizan uno tras otro en dos dimensiones. Ej Matrices

Los arreglos distinguen a cada uno de sus elementos mediante un indice correspondiente (i)

En python los arreglos se expresan como listas 

'''

mi_arreglo = [] #Creacion de un arreglo vacio

mi_arreglo = [2,4,5,3,6] #Arreglo con elementos 

#Acceder al Array

print("----------------------Accedo elemento Array---------------------------------")
print(f"Pirmer elemento: {mi_arreglo[0]}") #-> Accedo al primer elemento 

print(f"Segundo elemnto: {mi_arreglo[1]}") # -> Accedo al segundo elemento
print("-----------------------Cantidad elementos Array------------------------------------")

cantidad_elementos = len(mi_arreglo) #-> Funcion len para obtener la cantidad de elementos del Array
print(f"La cantidad de elementos del Array es: {cantidad_elementos}")

print("---------------------Acceder a un elemento particular---------------------------")
print(f"Ultimo elemento: {mi_arreglo[4]}") # -> Accedo al ultimo elemento 
print(f"Ultimo elemento: {mi_arreglo [cantidad_elementos - 1]}") # -> Accedo al ultimo elemento - RECOMENDADA
print(f"Ultimo elemento: {mi_arreglo[-1]}") # -> El indice -1 me va a mostrar ultimo elemento del Array (SOLO FUNCIONA EN PYTHON - RECOMIENDA NO USAR)
print("---------------- Mostrar elementos Array -----------------------------------------")
#Formas de mostrar los elementos del Array
#1
for i in range(len(mi_arreglo)):
    print(mi_arreglo[i]) #Va mostrando lo que hay en el Array en la posicion i
print("--------------- Mostrar elementos del Array -------------------------------------")
#2
for elemento in mi_arreglo: #-> For each
    print(elemento) 

print("----------------- Operaciones con Array -------------------------------")

suma_elementos = 0

# for i in range(len(mi_arreglo)):
#     suma_elementos += mi_arreglo[i]

for elemento in mi_arreglo:
    suma_elementos += elemento 

promedio_elementos = suma_elementos / len(mi_arreglo)

print(f"La suma de los elementos es {suma_elementos} y el promedio es {promedio_elementos}")

