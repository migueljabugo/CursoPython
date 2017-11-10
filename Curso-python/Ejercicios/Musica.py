class Instrumento:
	
	def __init__(self, marca, tipo, material, fechaInvencion, afinado=True):
		self.marca = marca
		self.tipo = tipo
		self.material = material
		self.afinado = afinado
		self. fechaInvencion = fechaInvencion

	def afinar(self):
		self.afinado = True

	def sonar(self):
		print("...")


class Piano(Instrumento):

	def __init__(self, marca, tipo, material, fechaInvencion, afinado, numero_teclas, electrico):
		super().__init__(marca, tipo, material, fechaInvencion, afinado)
		self.numero_teclas = numero_teclas
		self.electrico = electrico
	
	def sonar(self):
		print("Din dan dun!")


class Trompeta(Instrumento):
	def __init__(self, marca, tipo, material, fechaInvencion, afinado, tonalidad, atril_includo):
		super().__init__(marca, tipo, material, fechaInvencion, afinado)
		self.tonalidad = tonalidad
		self.atril_includo = atril_includo

	def sonar(self):
		print("prrrrfprrrf")


