import random
from random import choice
import itertools

#Ejercicio 1
'''Crea una funcion que dada una secuencia de numeros determine si todos 
los numeros son diferentes entre ellos. Tiene que devolver True o False
'''
def sonTodosDiferentes(lista):
	for x in lista:
		cont = 0
		for y in lista:
			if (x == y):
			    cont +=1
		if (cont > 1):
			return False
	return True

#correccion ejercicio 1
def todosDiferentes(lista):
	conjunto = set(lista)
	return len(lista)==len(conjunto)


#Ejercicio 2
'''Crea una funcion que dada una secuencia de numero que devuelva la misma 
secuencia eliminando antes el 3 elemento
'''
def eliminaTercerElemento(lista):
	if len(lista)>=3:
	    lista.pop(2)
	return lista
	    

#Ejercicio 3
'''Crea una funcion que dado un numero devuelva una lista con todos los 
divisores de ese numero
'''
def divisoresDeUnNumero(numero):
	divisor = 0
	lista = []
	if numero % 2 == 0:
		iterar = numero / 2
	else:
		iterar = (numero - 1) / 2
	for i in range(1, int(iterar) + 1):
		if numero % i == 0:
			aux = numero / i
			if aux != divisor:
				divisor = aux
			if i == iterar:
				lista.append(int(divisor))
			else:
				lista.append(int(divisor))
	return lista


#Ejercicio 4 
'''Crea una funcion que dadas dos listas devuelva otra que contenga solo 
los elementos que tienen en comun (sin duplicados)
'''
def elementosEnComun(lista1, lista2):
	result = []
	for elementoLista1 in lista1:
		for elementoLista2 in lista2:
			if (elementoLista1==elementoLista2):
				if elementoLista1 not in result:
					result.append(elementoLista1)
	return result

#Ejercicio 5
'''Crea una funcion que simule el juego Piedra, Papel y Tijeras. Debe preguntar 
(usando input) la eleccion de los 2 jugadores y devolver un mensaje que diga 
que jugador ha ganado("Jugador 1" o "Jugador 2 gana")
'''
def juegoPiedraPapelTijeras():
	texto = "\n-> Piedra\n-> Papel\n-> Tijeras\nIntroduzca su elección: "
	jugador1 = input("Jugador 1: "+ texto).lower()
	jugador2 = input("Jugador 2: "+ texto).lower()
	result = ""
	piedra = "piedra"
	papel = "papel"
	tijeras = "tijeras"

	if (jugador1 == jugador2):
	    result = "Empate, Los dos jugadores eligieron "+ str(jugador1)
	else:
		result = "Gana el jugador "
		if (jugador1 == piedra and jugador2 == papel):
			result += "2"
		elif (jugador1 == piedra and jugador2 == tijeras):
			result += "1"
		elif (jugador1 == papel and jugador2 == piedra):
			result += "1"
		elif (jugador1 == papel and jugador2 == tijeras):
			result += "2"
		elif (jugador1 == tijeras and jugador2 == papel):
			result += "1"
		elif (jugador1 == tijeras and jugador2 == piedra):
		    result += "2"
	print(result)


#Ejercicio 6
'''Crea una funcion que simule el juego Adivina el número. Debe generar 
aletatoriamente un numero del 1 al 10 (ambos inclusive) en secreto, el jugador 
debe adivinar el numero introduciendo (usando input) uno que el crea que es el 
elegido. El programa debe decir si el numero introducido por el jugador es 
"demasado bajo", "demasiado alto" o "¡Acertaste!"
'''
def adivinaElNumero():
	numero = random.randint(0,11)
	jugando = True
	while (jugando):
		numero_usuario = int(input("Introduce un numero del 0 al 10: "))
		if (numero < numero_usuario):
			print("Demasiado alto")
		elif (numero > numero_usuario):
			print("Demasiado bajo")
		else:
			print("¡Acertaste!")
			print(numero)
			jugando = False


#Ejercicio 7
'''Crea una funcion que dada una lista devuelva una nueva solo con el primer 
y el ultimo elemento de la lista dada
'''
def primerUltimoElemento(lista):
	result = []
	result.append(lista.pop(0))
	result.append(lista.pop(len(lista)-1))
	return result

#Ejercicio 8
'''Crea una función que dada una frase (con mas de dos palabras) devuelva 
otra frase con las palabras en orden inverso
'''
def reordenaFrase(frase):
	palabras = frase.split(' ')
	nueva_frase = ""
	while (len(palabras)>1):
	    nueva_frase += palabras.pop(random.randint(0, len(palabras)-1))+" "
	return nueva_frase


def invierteFrase(frase):
	nueva_frase = ""
	palabras = frase.split(' ')
	palabras = list(palabras)
	palabras.reverse()
	while (len(palabras)>1):
	    nueva_frase += palabras.pop(0)+" "
	return nueva_frase
	

	
#Ejercicio 9
'''Crea una funcion que dado 3 numeros de un digito (0 a 9 ambos inclusive) 
devuelva una lista con todas las conbinaciones posibles
'''
def combinacionesPosibles(num1, num2, num3):
    return list(itertools.permutations(str(num1) + str(num2) + str(num3), 3))
	

#Ejercicio 10
'''Crea una funcion que dada una frase devuelva un diccionario con el numero 
de veces que aparece cada caracter
'''
def repeticionDeCaracteres(frase):
	diccionario = {}
	caracteres = list(frase)
	'''for caracter in caracteres:
	    if diccionario.get:
			print('a')
		else:
			print('b')'''




#Ejercicio 20
'''Crea una funcion que genere aleatoriamente una contraseña robusta. La contraseña
debe tener numeros, letras(mayusculas y minusculas) y al menos 1 caracter especial.
La longitud minima es de 8 y maxima 20.
'''
def generaClaveAleatoria():
	caracteres = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
	longitud = random.randint(8, 21)
	clave = ""
	clave = clave.join([choice(caracteres) for i in range(longitud)])
	return clave





