# for i in range (5): 
#     print ("Hola")

# for i in range (5):
#     print(i) #Ira del 0 al range -1

# for i in range (inicio,final-1, incremento) sirve para seleccionar el rango que quiero recorrer
# for i in range(1,6,1): 
#     print(i)


#For Decreciente: arranca en numero alto y termina en numero bajo
# for i in range(5,0,-1): #5-4-3-2-1
#     print(i)

# Puedo incrementar segun el numero que yo decida
# for i in range(0,10,2):#0-2-4-6-8
#     print(i)

#Break-> sale del bucle repetitivo cuando ocurre algo

# for i in range (5):
#     if i == 2:
#         break
#     print(i)

#Continue -> Permite salir de la iteracion actual cuando ocurre algo / Saltea 

for i in range (5):
    if i == 2: 
        continue #En este caso saltea el 2 
    print(i)