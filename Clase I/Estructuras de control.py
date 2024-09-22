# edad = int(input("Ingrese su edad: "))  

# print(f"Su edad es {edad}")

# '''
# Adulto > 18
# Adolescente entre 13 y 18
# Niño < 13

# '''

# if edad > 17:
#     print("Usted es adulto")
# elif edad > 12 and edad < 18:
#     print ("Usted es adolescente")
# else:
#     print("Usted es un niño")

mes = input("Ingrese un mes: ")

#El match es similar a if-elif, pero solo evalua por igualacion y tambien se pueden evaluar varias opciones en una misma evaluación (or)

match(mes):
    case "Enero" | "Marzo" | "Mayo" | "Julio" | "Agosto" | "Octubre" | "Diciembre": 
        print("Este mes tiene 31 dias")
    case "Abril" | "Junio" | "Septiembre" | "Noviembre":
        print("Este mes tiene 30 dias")
    case "Febrero":
        print("Este mes tiene 28 dias")
    case _ :
        print("Ingresó un mes no valido")
        
# Por regla general se coloca _ cuando tengo que colocar una opcion que no sea ninguna de las ingresadas anteriormente (simula un else)
        