dic = {"Nombre": "Juan", "Especialidad": ["Programacion", "Ciberseguridad"], "Edad": 25}

#print(dic)

#for i in dic:  #Solo me devuelve las llaves, no sus valores
    #print(i)

#print(dic["Edad"])  #Me devuelve el valor de la llave "Edad"

#for i in dic:
    #print(dic[i])  #Me devuelve los valores de las llaves 

#for key in dic:
    #value = dic[key]
    #if isinstance(value, list):
        #for i in value:               #Manera de que me retorne todos los datos con key-value
            #print(f"{key}: {i}")
    #else:
        #print(f"{key}: {value}")  

#Metodos

#dic["Nombre"] = "Pedro"
#print(dic)

#dic.clear()    
#print(dic)

#print(dic.items())

#print(dic.keys())

#print(dic.values())