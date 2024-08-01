#Esta sentencia nos permite ejecutar un bloque de codigo multiples veces. Nos permite realizar iteraciones  cuantas veces definamos el bucle. Asi mismo, a diferencia de muchos lenguajes de programacion que suelen realizar las iteraciones sobre progresiones aritmeticas, Python  nos permite realizar estas iteraciones sobre items de una secuencia como listas o cadenas de texto

#nombres = ["Pedro", "Juan", "Joel"]

#for nombre in nombres:
    #print(nombre)


#Con cadenas de texto

#oracion = " Bienvenidos a LionGuard Academy".lower()
#oracion_sin_vocales = ""

#for letra in oracion:
 #   if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
 #      pass
  #  else:
  #      oracion_sin_vocales += letra

#print(oracion_sin_vocales)

#Aplicado a un ejemplo de ataque fuerza bruta

usuarios = ["admin","root","administrator"]
passwords = ["toor","qwerty","12345","contraseña"]

for usuario in usuarios:
    print("usuario:",usuario)
    for password in passwords:
        print ("contraseña:",password)
        if usuario == "administrator" and password == "qwerty":
            print ("Se encontraron las credencialees")
            print (f">>{usuario}:{password}")







    
