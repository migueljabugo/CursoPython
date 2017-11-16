# -*- coding: utf-8 -*-
from Ejercicios.Musica import *
from Ejercicios.ficheros import *
from Ejercicios.Ejercicios13Noviembre import *
import io
'''
print(funciones.sucesionPadovan1())
print(funciones.sucesionFibonacci(10))
'''
'''
theWitcher3 = VideoJuego("The Witcher 3", "CD Projeckt Red", 2015)

print(theWitcher3)
theWitcher3.jugar()
print(theWitcher3)
'''
'''
piano = Piano("Yamaha", "Cuerda percutida", "madera", 1695, False, 88, False)
trompeta = Trompeta("Yamaha", "Viento", "Laton", 1607, True, "Bb", True)

piano.sonar()
trompeta.sonar()
'''

'''
escribirEnFichero("Hola.txt", "Hola mundo")
print(leerFichero("Hola.txt"))
'''

lista = [4,5,6,8,7,10]
lista2 =[1,2,3,4,5,5,6,9]
frase = "hola esto es una prueba"
diccionario = {
	1:"Hola",
	0:"esto",
	2:"una",
	3:"es",
	4:"prueba"
	}
dic1 = {
	"a":"Hola",
	"b":"esto",
	"c":"una",
	"d":"es",
	"e":"prueba"
	}
dic2 = {
	"f":"Hola",
	"g":"esto",
	"h":"una",
	"i":"es",
	"j":"prueba"
	}
dic3 = {
	"k":"Hola",
	"l":"esto",
	"m":"una",
	"n":"es",
	"0":"prueba"
	}

#print(divisoresDeUnNumero(46))
#adivinaElNumero()
#print(invierteFrase("Esto es una prueba, seguro que funciona todo correcto"))
#print(combinacionesPosibles(1,2,3))
#repeticionDeCaracteres("hola")
#print(generaClaveAleatoria())
#print(repeticionDeCaracteres(frase))
#print(sumaElementos(lista))
#print(multiplicaElementos(lista))
#print(mayor(lista))
#print(menor(lista))
#print(ordena(lista))
#print(ordenaDiccionario(diccionario))
#print(unificaDiccionarios(dic1, dic2, dic3))
print(generaDiccionario(5))
