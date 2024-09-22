'''
INTEGRADOR

La división de higiene está trabajando en un control de stock para productos sanitarios. 
Debemos realizar la carga de 5 (cinco) productos de prevención de contagio, de cada una debe obtener los siguientes datos: 
1. El tipo (validar "barbijo", "jabón" o "alcohol") 
2. El precio: (validar entre 100 y 300) 
3. La cantidad de unidades ( no puede ser 0 ni negativo y no debe superar las 1000 unidades) 
4. La marca y el Fabricante. 

Se debe informar lo siguiente: 
A. Del más caro de los barbijos, la cantidad de unidades y el fabricante. 
B. Del ítem con más unidades, el fabricante. 
C. Cuántas unidades de jabones hay en total.

'''

for i in range(6):

    tipo_producto = input("Ingrese tipo de producto: ")
    
    while tipo_producto != "barbijo" and tipo_producto != "jabon" and tipo_producto != "alcohol":
        tipo_producto = input("Vuelva a ingresar tipo de producto: ")
    
    precio = float(input("Ingrese el precio del producto: Entre 100 y 300: "))

    while precio < 100 or precio > 300:
        precio = float(input("Vuelva a ingresar el precio del producto: "))

    cantidad_unidades = int(input("Ingrese la cantidad de unidades: "))
