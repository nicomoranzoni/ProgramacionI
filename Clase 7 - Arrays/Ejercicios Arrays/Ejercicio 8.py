import random

#Porcentaje = (Parte/Total)*100

lista = [0,0,0,0,0,0,0,0,0,0] #Defino la lista 
acumulador_sueldos = 0


for i in range (10):
    numero = random.randint(350000, 1250000)
    acumulador_sueldos += numero
    lista[i] = numero # Cargo los sueldo a la lista 

sueldo_promedio = acumulador_sueldos /len(lista) #Promedio de sueldos

superan_promedio = 0

for i in range(len(lista)):
    if lista[i] > sueldo_promedio:
        superan_promedio += 1

porcentaje = (superan_promedio / len(lista)) * 100

print(lista)
print(f"El sueldo promedio es {sueldo_promedio}")
print(f"Los que superan el sueldo promedio son: {sueldo_promedio}")
print(f"El porcentaje es: {porcentaje}")