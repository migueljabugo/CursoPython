#2
diccionario = {"9:00":"Quedar con Ana",
			   "11:30":"Reunion con Jose",
			   "14:30":"Almorzar con Alba",
			   "19:00":"Ir al taller",
			   }

#3
def imprimeDiccionario(diccionario):
	result = ""
	for k in diccionario:
		result += str(k)+" -> " +str(diccionario[k] +"\n")
	return result

print(imprimeDiccionario(diccionario))

#4
def imprimeFichero(fichero, texto):
	file = open(str(fichero), 'w') 
	file.write(str(texto))
	file.close()

imprimeFichero("diccionario.txt", imprimeDiccionario(diccionario))
