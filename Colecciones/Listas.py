nombres = ['Pedro', 'Luis', 'Maria']
print(nombres)

edades = [23, 45, 12,]
print(edades)

booleano = [True, False,]

lista = [["Jorge","Pedro","Maria"],[23, 21, 22]]

lista_2d = [["Jorge",24],["Luis",23]], [["Maria", 22], ["Pedro", 21]]

for i in lista_2d:
    print(i)

mix = [23, "Maria", True, ["Jorge", 24]]

for valor in mix:
    if isinstance(valor, list):
        for j in valor:
            print(j)
    else:
        print(valor)