def escribirEnFichero(fichero, texto):
	#w => sobrescribe
	#a => Agrega
	file = open(str(fichero), 'w') 
	file.write(str(texto))
	file.close()

def leerFichero(fichero):
	file = open(str(fichero), 'r')
	result = file.read()
	file.close()
	return result
