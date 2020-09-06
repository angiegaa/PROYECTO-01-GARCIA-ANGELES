from lifestore_file import lifestore_products
from lifestore_file import lifestore_sales
from lifestore_file import lifestore_searches

#usuario = "Admin"
#password = "23456"

usuarios = [["Harry_Potter", "23456"], ["Ron_Weasley", "23456"], ["Hermione_Granger", "23456"]]

print("This is La casa de Gryffindor Sales data")
print("Ingrese su usario y contraseña para inciar sesión")
usr_login = input('Usuario: ')
pass_login = input('Contraseña: ')

es_worker = 0
for usuario in usuarios:
    if usuario[0] == usr_login and usuario[1] == pass_login:

        es_worker = 1
        print("Bienvenido a La casa de Gryffindor Sales Data")
        break

if es_worker == 1:
    print("Confirmación de usuario: ", usr_login, "\n En breve se presentará el informe de la empresa")
else:
    print("Ops! Debes ser Draco Malfoy queriendo acceder...  ¡Datos incorrectos!")
   

#Agregar Menú
if es_worker == 1:
 print("Las opciones que verás a continuación son:   \n 1. Productos menos vendidos \n 3. Categorías más vendidas \n 4. Categorías menos vendidas \n 5. Búsquedas \n 6. raitings \n 7. ventas anuales \n 8. ventas mensuales")
else:
  print("Ops! ya lo dijimos, no podemos darte acceso al informe, debes ser de la competencia")

contador = 0
total_ventas = []

for producto in lifestore_products:
    for venta in lifestore_sales:
        if producto[0] == venta[1]:
            contador += 1

    formato_ideal2 = [producto[0], contador]
    total_ventas.append(formato_ideal2)
    contador = 0

#print(total_ventas)

# """
#   formato_ideal = [producto[0], producto[1], contador]
#   total_ventas.append(formato_ideal)
#   contador = 0
# """

ventas_ord_menor = []

while total_ventas:
    minimo = total_ventas[0][1]
    lista_actual = total_ventas[0]
    for venta in total_ventas:
        if venta[1] < minimo:
            minimo = venta[1]
            lista_actual = venta
    ventas_ord_menor.append(lista_actual)
    total_ventas.remove(lista_actual)



#Para imprimir los datos de mayor a menor

ventas_ord_mayor = []

while total_ventas:
    minimo = total_ventas[0][1]
    lista_actual = total_ventas[0]
    for venta in total_ventas:
        if venta[1] > minimo:
            minimo = venta[1]
            lista_actual = venta
    ventas_ord_mayor.append(lista_actual)
    total_ventas.remove(lista_actual)



""""
if es_worker == 1:
  for venta in ventas_ord_mayor:
    if venta[1] != 0:
      continue
    else:
      print(venta[0:21])
"""
if es_worker == 1:
  for venta in ventas_ord_menor:
    if venta[1]==0:
      continue
    else:
      print(venta)


# orden por categorías
lista_categorias = []

for categoria in lifestore_products:
    if categoria == lifestore_products[3]:
        continue
    else:
        lista_categorias.append(categoria[3])

categorias = []

for i in lista_categorias:
    if i not in categorias:
        categorias.append(i)

#print(categorias)

# Composición de categorías por producto

total_categorias0 = []

for category in lifestore_products:
    if category[3] == categorias[0]:
        total_categorias0.append(category)
    else:
        continue

# for categoria in total_categorias0:
#   print(categoria)

total_categorias1 = []
for category in lifestore_products:
    if category[3] == categorias[1]:
        total_categorias1.append(category)
    else:
        continue

#for categoria in total_categorias1:
#print(categoria)

total_categorias2 = []
for category in lifestore_products:
    if category[3] == categorias[2]:
        total_categorias2.append(category)
    else:
        continue

#for categoria in total_categorias2:
#print(categoria)

total_categorias3 = []
for category in lifestore_products:
    if category[3] == categorias[3]:
        total_categorias3.append(category)
    else:
        continue

#for categoria in total_categorias3:
#print(categoria)

total_categorias4 = []
for category in lifestore_products:
    if category[3] == categorias[4]:
        total_categorias4.append(category)
    else:
        continue

#for categoria in total_categorias4:
#print(categoria)

total_categorias5 = []
for category in lifestore_products:
    if category[3] == categorias[5]:
        total_categorias5.append(category)
    else:
        continue

#for categoria in total_categorias5:
#print(categoria)

total_categorias6 = []
for category in lifestore_products:
    if category[3] == categorias[6]:
        total_categorias6.append(category)
    else:
        continue

#for categoria in total_categorias6:
#print(categoria)

total_categorias7 = []
for category in lifestore_products:
    if category[3] == categorias[7]:
        total_categorias7.append(category)
    else:
        continue

#for categoria in total_categorias7:
#print(categoria)
comp_categoria = []

if es_worker == 1:
  comp_categoria = int(input("SELECCIONA UNA CATEGORÍA PARA CONOCER SUS BÚSQUEDAS POR ID \n 0= procesadores\n 1= tarjetas de video\n 2= tarjetas madre\n 3= discos duro\n 4= memorias usb\n 5= pantallas\n 6=bocinas\n 7= audifonos\n Categoria:  "))

if comp_categoria == 0:
  comp_categoria = total_categorias0
  #print(total_categorias0)
elif comp_categoria == 1:
  comp_categoria = total_categorias1
  #print(total_categorias1)
elif comp_categoria == 2:
  comp_categoria = total_categorias2
  #print(total_categorias2)
elif comp_categoria == 3:
  comp_categoria = total_categorias3
  #print(total_categorias3)
elif comp_categoria == 4:
  comp_categoria = total_categorias4
  #print(total_categorias4)
elif comp_categoria == 5:
  comp_categoria = total_categorias5
  #print(total_categorias5)
elif comp_categoria == 6:
  comp_categoria = total_categorias6
  #print(total_categorias6)
elif comp_categoria == 7:
  comp_categoria = total_categorias7
  #print(total_categorias7)
else:
  print("Ops! en algo te equivocaste, vuelve a introducirlo")

suma = 0 
#ordenar la lista de menor a mayor
for id_producto in ventas_ord_menor:
  for producto in comp_categoria:
    if id_producto[0] == producto[0]:
      print("ID_PRODUCT: ", id_producto[0], "venta: ", id_producto[1])  
    else:
      continue 

#Busquedas de menor a mayor

contador = 0
busquedas = []

for producto in lifestore_products:
    for id_producto in lifestore_searches:
        if producto[0] == id_producto[1]:
            contador += 1

    formato_ideal3 = [producto[0], contador]
    busquedas.append(formato_ideal3)
    contador = 0

ord_menor_busq = []

while busquedas:
    minimo = busquedas[0][1]
    lista_actual = busquedas[0]
    for producto in busquedas:
        if producto[1] < minimo:
            minimo = producto[1]
            lista_actual = producto
    ord_menor_busq.append(lista_actual)
    busquedas.remove(lista_actual)

if es_worker == 1:
  for busqueda in ord_menor_busq:
    print("ID_PRODUCT: ", busqueda[0], "searches", busqueda[1])

#busquedas de mayor a menor 
ord_menor_busq1 = []

while busquedas:
    minimo = busquedas[0][1]
    lista_actual = busquedas[0]
    for producto in busquedas:
        if producto[1] > minimo:
            minimo = producto[1]
            lista_actual = producto
    ord_menor_busq1.append(lista_actual)
    busquedas.remove(lista_actual)

if es_worker == 1:
  for busqueda in ord_menor_busq1:
    print("ID_PRODUCT: ", busqueda[0], "searches", busqueda[1])

#Raitings de los productos

raiting_m = []

for producto in lifestore_products:
  contador = 0
  raitings = 0
  promedio = 0
  for id_producto in lifestore_sales:
    if producto[0] == id_producto[1]:
       contador += 1
       raitings += id_producto[2]
    else:
       continue
  if contador != 0:
    promedio = raitings/contador
    lista_raiting = [producto[0], contador, promedio]
    raiting_m.append(lista_raiting)

#Ordenar de mayor a menor 
      
raitings_ord = []

while raiting_m:
    minimo = raiting_m[0][2]
    lista_actual = raiting_m[0]
    for promedio in raiting_m:
        if promedio[2] > minimo:
            minimo = promedio[2]
            lista_actual = promedio
    raitings_ord.append(lista_actual)
    raiting_m.remove(lista_actual)

if es_worker == 1:
  for calificacion in raitings_ord:
    print("ID y calificación usuario: ", calificacion)    



#Ventas anuales

contador_income = 0
contador_sales = 0

for producto in lifestore_products:
  for ventas in lifestore_sales:
    if producto[0] == ventas[1]:
      contador_sales += 1  
      if ventas[4] != 1:
        contador_income += producto[2]
    
if es_worker == 1:
  print("Ingreso anual fue de: ", contador_income)
  print("Ventas totales: ", contador_sales)

promedio_men = contador_income/8
if es_worker == 1:
  print("El promedio de ventas mensuales es: ", promedio_men)


#Ventas mensuales

#Lista de meses con ventas mensuales
#enero
fecha = lifestore_sales[0][3]
contar = slice(3,5,1)

fecha01 = "01"
contador_01 = 0
contador_ingresos01 = 0
for valor_venta in lifestore_sales:
  if fecha01 == valor_venta[3][contar]:
    contador_01 += 1
    for precio in lifestore_products:
       if valor_venta[1] == precio[0]:
        contador_ingresos01 += precio[2]
if es_worker==1:
  print("En el mes ", fecha01, "se vendió un total de", contador_ingresos01)

#febrero
fecha = lifestore_sales[0][3]
contar = slice(3,5,1)

fecha02 = "02"
contador_02 = 0
contador_ingresos02 = 0
for valor_venta in lifestore_sales:
  if fecha02 == valor_venta[3][contar]:
    contador_02 += 1
    for precio in lifestore_products:
       if valor_venta[1] == precio[0]:
        contador_ingresos02 += precio[2]
if es_worker == 1:
  print("En el mes ", fecha02, "se vendió un total de", contador_ingresos02)

#marzo 
fecha = lifestore_sales[0][3]
contar = slice(3,5,1)

fecha03 = "03"
contador_03 = 0
contador_ingresos03 = 0
for valor_venta in lifestore_sales:
  if fecha03 == valor_venta[3][contar]:
    contador_03 += 1
    for precio in lifestore_products:
       if valor_venta[1] == precio[0]:
        contador_ingresos03 += precio[2]
if es_worker == 1:
  print("En el mes ", fecha03, "se vendió un total de", contador_ingresos03)

#abril
fecha = lifestore_sales[0][3]
contar = slice(3,5,1)

fecha04 = "04"
contador_04 = 0
contador_ingresos04 = 0
for valor_venta in lifestore_sales:
  if fecha04 == valor_venta[3][contar]:
    contador_04 += 1
    for precio in lifestore_products:
       if valor_venta[1] == precio[0]:
        contador_ingresos04 += precio[2]
if es_worker == 1:
  print("En el mes ", fecha04, "se vendió un total de", contador_ingresos04)

#mayo
fecha = lifestore_sales[0][3]
contar = slice(3,5,1)

fecha05 = "05"
contador_05 = 0
contador_ingresos05 = 0
for valor_venta in lifestore_sales:
  if fecha05 == valor_venta[3][contar]:
    contador_05 += 1
    for precio in lifestore_products:
       if valor_venta[1] == precio[0]:
        contador_ingresos05 += precio[2]
if es_worker == 1:
  print("En el mes ", fecha05, "se vendió un total de", contador_ingresos05)

#junio 
fecha = lifestore_sales[0][3]
contar = slice(3,5,1)

fecha06 = "06"
contador_06 = 0
contador_ingresos06 = 0
for valor_venta in lifestore_sales:
  if fecha06 == valor_venta[3][contar]:
    contador_06 += 1
    for precio in lifestore_products:
       if valor_venta[1] == precio[0]:
        contador_ingresos06 += precio[2]
if es_worker == 1:
  print("En el mes ", fecha06, "se vendió un total de", contador_ingresos06)

#julio

fecha = lifestore_sales[0][3]
contar = slice(3,5,1)

fecha07 = "07"
contador_07 = 0
contador_ingresos07 = 0
for valor_venta in lifestore_sales:
  if fecha07 == valor_venta[3][contar]:
    contador_07 += 1
    for precio in lifestore_products:
       if valor_venta[1] == precio[0]:
        contador_ingresos07 += precio[2]
if es_worker == 1:
  print("En el mes ", fecha07, "se vendió un total de", contador_ingresos07)

#agosto
fecha = lifestore_sales[0][3]
contar = slice(3,5,1)

fecha08 = "08"
contador_08 = 0
contador_ingresos08 = 0
for valor_venta in lifestore_sales:
  if fecha08 == valor_venta[3][contar]:
    contador_08 += 1
    for precio in lifestore_products:
       if valor_venta[1] == precio[0]:
        contador_ingresos08 += precio[2]
if es_worker == 1:
  print("En el mes ", fecha08, "se vendió un total de", contador_ingresos08)

if es_worker == 1:
  print("Fin del programa, ver informe PDF para información más detallada")
  print("La casa de Gryffindor agradece tu visita :)")















  






 







