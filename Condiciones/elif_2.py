# Calculadora
print("Bienvenido a la calculadora")
print("A que modo deseas ingresar")
modo = input("[1]. Operaciones Basicas \n[2]. Par o Impar\n>>")
if modo == "1":
    var1 = int(input("Ingresa el primer numero"))
    var2 = int(input("Ingresa el segundo numero"))
    oper = int(input("[1]. Suma\n[2]. Resta\n[3]. Multiplicacion\n[4]. Division\n[5]. Potencia"))

# Suma
    if oper == 1:
        suma = var1 + var2
        print(f"El resultado de la Suma es {suma}")

# Resta
    elif oper == 2:
        resta = var1 - var2
        print(f"El resultado de la Resta es {resta}")
# Multiplicacion
    elif oper == 3:
        Multiplicacion = var1 * var2
        print(f"El resultado de la Multiplicacion es {Multiplicacion}")
# Division
    elif oper == 4:
        Division = var1 / var2
        print(f"El resultado de la Division es {Division}")
# Potencia
    elif oper == 5:
        Potencia = var1**var2
        print(f"El resultado de la Potencia es {Potencia}")
elif modo == "2":
    var = int(input("Ingrese un numero:"))
    if var % 2 == 0:
        print(f"El numero {var} es par")
    else:
        print(f"El numero {var} es impar")
else:
    print("Opción no válida. Por favor, seleccione 1 o 2.")