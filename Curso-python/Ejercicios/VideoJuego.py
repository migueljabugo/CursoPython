import random

class VideoJuego:
	def __init__(self, nombre, publisher, fecha):
		self.nombre = nombre
		self.publisher = publisher
		self.fecha = fecha
		self.jugado = False

	def valorarlo(self):
		return random.randint(0, 10)
	
	def jugar(self):
		self.jugado = True

	def __str__(self):
		return "Nombre: "+ self.nombre + "\nPublisher: "+self.publisher +"\nFecha: "+ str(self.fecha) + "\nJugado: "+ str(self.jugado)
