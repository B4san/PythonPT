# 13 o mas A
# 12 o 11 B
# 10 o menos C
# VALIDACION => 0 - 20


nombre = input("Ingrese su nombre\n>>")
sexo = input("Ingrese su sexo \n[M]. Msculino\n[F]. Femenino\n[#]. Salir\n>>")
sexo = sexo.upper()


if sexo != "M" and sexo != "F":
    print("Genero Incorrecto")
else:
    nota = int(input("Ingresa tu nota:"))
    if (nota > 20 or nota < 0):
        print ("Error - Su nota debe estar en el rango de 0-20")
    else:
        if nota >= 13 and sexo == "M":
            print(f"Señor {nombre} usted ha sido aprobado")
        elif nota >= 13 and sexo == "F":
            print(f"Señorita {nombre} Usted ha sido aprobada")
        elif (nota == 12 or nota == 11) and sexo == "M":
            print (f"Señor {nombre} Usted debe ir a vacacional")
        elif (nota == 12 or nota == 11) and sexo == "F":
            print (f"Señorita {nombre} Usted debe ir a vacacional")
        elif nota <= 10 and sexo == "M":
            print (f"Señor {nombre} Usted esta reprobado")
        elif nota <= 10 and sexo == "F":
            print (f"Señorita {nombre} Usted esta reprobada")
        else:
            print ("Entrada no valida")