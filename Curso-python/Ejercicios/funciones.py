#Sucesion de fibonacci
def sucesionFibonacci(n):
	f0 = 0
	f1 = 1
	sucesion = [f0, f1]
	for i in range(n):
		f2 = f0 + f1
		sucesion.append(f2)
		f0 = f1
		f1 = f2
	return sucesion

#sucesion Padovan
def sucesionPadovan1(n):
	sucesion = []
	for i in range(n):
		if i == 0 or i == 1 or i == 2:
			sucesion.append(1)
		else:
			valor = sucesion[-2] + sucesion[-3]
			sucesion.append(valor)
	return sucesion

