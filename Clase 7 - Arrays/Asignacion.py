arreglo_numeros = [1,3,5]

# arreglo_numeros_dos = arreglo_numeros # Se guarda el mismo id que la variable arreglo_numeros, esto no funciona si quiero que sean independientes

arreglo_numeros_dos = arreglo_numeros.copy() #Creo una copia de los valores del Array original guardandolos en un espacio de memoria diferente, diferentes id

print(f"""
Arreglo_numeros = {arreglo_numeros}
arreglo_numeros_dos = {arreglo_numeros_dos}
""")

arreglo_numeros[0] = 2 #Cambio primer elemento de un 1 a un 2


print(f"""
Arreglo_numeros = {arreglo_numeros}
arreglo_numeros_dos = {arreglo_numeros_dos} #Matiene los valores orignales ya que tienen diferente espacio de memoria
""")