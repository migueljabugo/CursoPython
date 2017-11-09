#Ejercicio 3
mi_tupla=(0,0,5,0,0,1,1,1,1,2,2,2,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,6,6,6,8,1,8,9,9,9,9,7,9)
entrada= int(input("Introduce un numero: "))
result=0
for numero in mi_tupla:
    if numero==entrada:
        result +=1
print(result)
