#Ejercicio 1 pag 17
'''
mi_tupla = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")
numero_usuario = input("Introduce un numero: ")
if int(numero_usuario)>=0 and int(numero_usuario)<=len(mi_tupla):
    print(mi_tupla[int(numero_usuario)-1])
else:
	print("Numero incorrecto")
	'''

#Ejercicio 2 pag 17
'''
mi_lista = []
numero = int(input("Introduce un numero: "))
while (numero !=0):
	mi_lista.append(numero)
	numero = int(input("Introduce un numero: "))
i=0
while i<len(mi_lista):
	print(mi_lista[i])
	i+=1
'''

#Ejercicio 3
'''
mi_tupla=(0,0,5,0,0,1,1,1,1,2,2,2,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,6,6,6,8,1,8,9,9,9,9,7,9)
entrada= int(input("Introduce un numero: "))
result=0
for numero in mi_tupla:
    if numero==entrada:
        result +=1
print(result)
'''

#Ejercicio 4
'''
mi_tupla=(0,0,5,0,0,1,1,1,1,2,2,2,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,6,6,6,8,1,8,9,9,9,9,7,4)
print("Minimo: "+ str(min(mi_tupla)))
print("Maximo: "+ str(max(mi_tupla)))
'''










