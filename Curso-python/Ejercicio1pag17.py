#Ejercicio 1 pag 17
mi_tupla = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")
numero_usuario = input("Introduce un numero: ")
if int(numero_usuario)>=0 and int(numero_usuario)<=len(mi_tupla):
    print(mi_tupla[int(numero_usuario)-1])
else:
	print("Numero incorrecto")

