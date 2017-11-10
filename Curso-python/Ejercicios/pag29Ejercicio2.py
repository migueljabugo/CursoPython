import math

#Normaliza valor
def normalizarValor(numero):

	if numero in range(0, 100):
	    return numero/100
	else:
		return -1


#Devolver el area del triangulo
def areaTriangulo(base, altura):
    return (base*altura)/2

#Devolver el area del circulo
def areaCirculo(radio):
	return math.pi* math.pow(radio, 2)

#Devolver una lista de rango [a, b]
#Solo con los valores pares
def rangoPar(a, b):
	return [x if (x%2==0) else 0 for x in range(a, b+1)]






#print(normalizarValor(int(input("Introduce un numero: "))))
#print(areaTriangulo(2, 4))
#print(areaCirculo(3))
print(rangoPar(0, 10))
