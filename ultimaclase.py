# #ENTRADAS
# 
# cat = input('Porfavor ingrese la categoria del cliente: ')
# imp = float(input('Porfavor ingrese el importe a pagar: '))
# 
# #PROCESOS Y SALIDAS
# if cat == "A" and imp >5000:
#     desc = imp -(imp*5)/100
#     print(desc)
# elif cat == "B" and imp >2500 and imp <3800:
#     desc = imp - (imp*2)/100
#     print(desc)
# 
'''Ejercicio 4'''
# 
# #Entradas
# edad1 = int(input('Ingrese la edad del primer usuario: '))
# edad2 = int(input('Ingrese la edad del segundo usuario: '))
# edad3 = int(input('Ingrese la edad del tercer usuario: '))
# #Procesos
# if edad1 < 0 or edad2 < 0 or edad3<0:
#     print('alguna es negativa')
# else:
#     print('todas son correctas')

import random
a= int(input('Ingrese a: '))
b=int(input('Ingrese b:'))
x = random.randrange(a,b)
print(x)


