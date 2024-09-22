'''
Escribir una función que tome una lista y la ordene aleatoriamente 
'''

import random

def ordenar_aleatoriamente (lista :list)-> list:

    random.shuffle(lista)

    return lista

lista = [1,2,3,4,5]

print(f"""
La lista original es {lista}
La lista ordenada aleatoriamente es {ordenar_aleatoriamente(lista)}""")