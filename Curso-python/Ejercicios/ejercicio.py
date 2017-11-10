import random

#Primera parte: Crear un tupla de numeros aleatorios

lista_numeros = list()
numero_elementos = 1000
'''
for i in range(numero_elementos):
	i+=1
	aleatorio = random.randint(0, 50)
	lista_numeros.append(aleatorio)
print(lista_numeros)
'''
#Tupla por comprension
lista_numeros = tuple(random.randint(0,50) for i in range(numero_elementos))


#Segunda parte: Crear un diccionario donde las claves son los numeros de la tupla 
#y el valor son las repeticiones
diccionario = {}
for numero in lista_numeros:
	if diccionario.get(numero)==None:
		diccionario[numero]=1
	else:
		diccionario[numero]+=1

#Imprimir por consola el diccionario con el formato:
'''
0 -> 3
1 -> 5
2 -> 2
'''
for k,v in diccionario.items():
    print ("%s -> %s" %(k,v))

