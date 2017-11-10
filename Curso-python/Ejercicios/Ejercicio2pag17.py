#Ejercicio 2 pag 17
mi_lista = []
numero = int(input("Introduce un numero: "))
while (numero !=0):
	mi_lista.append(numero)
	numero = int(input("Introduce un numero: "))
i=0
while i<len(mi_lista):
	print(mi_lista[i])
	i+=1

