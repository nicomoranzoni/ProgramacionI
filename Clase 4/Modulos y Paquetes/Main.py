#Main Ejecutará las funciones que determine 

#Manera que existes de importar funciones al main 
import Funciones #Importo todas dentro del modulo funciones 

Funciones.saludar
print(Funciones.sumar(10,5))

#----------------------------------------


from Funciones import saludar
# Solo importo la funcion que quiero utilizar
saludar()

#-----------------------------
from Funciones import saludar, sumar #voy seleccionando las que quiero 

#-----------------------------

from Funciones import * # El * es equivalente a todas las funciones que encuentre dentro del modulo funciones 

