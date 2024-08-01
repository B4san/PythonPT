print ("Bienvenidos a la calculadora que solo suma")

numero1 = int(input("Ingrese el primer valor:"))

numero2 = int(input("Ingrese el segundo valor:"))

suma = numero1 + numero2

#3 Formas de mostrarlo

print( "La suma de " + str(numero1) + " mas " + str(numero2) + " Es igual a: " + str(suma) )
print("La suma de {} mas {} es igual a {}".format(numero1,numero2,suma))
print(f"La suma de {numero1} mas {numero2} es igual a {suma}")