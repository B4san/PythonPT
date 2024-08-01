#Esta sentencia nos permite ejecutar un bloque de codigo multiples veces. ESto siempre y cuando la condicion definida en el bucle sea VERDADERA.

# contraseña = "XYZ" y 3 intentos


pass_Obt = input("Ingresa tu contraseña:")
contador = 1



while pass_Obt != "XYZ" and contador < 3:
    contador += 1
    print("La contraseña es incorrecta")
    pass_Obt = input("Ingresa tu contraseña:")

if pass_Obt == "XYZ":
    print ("Ingresaste al sistema")
else:
    print ("No tienes acceso")
