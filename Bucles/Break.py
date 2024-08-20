#Un numero es par impar con todos los numeros anteriores pares o impares separados con coma
#Par = True, False = False
numero = 0
impares = ""
pares = ""

while numero < 1:
    numero = int(input("Ingrese un numero positivo:"))

if numero%2 == 0:
    for i in range (1, numero+1):
        if i%2 == 0:
            impares = impares + str(i) + ","
    print(impares[: -1])
else:
    for i in range (1, numero+1):
        if i%2 == 1:
            pares = pares + str(i) + ","
    print(pares[:-1])
