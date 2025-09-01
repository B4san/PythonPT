import random



def atk_enemy(num):
    if num == 1:
        dano = random.randrange(0,20,10)
    elif num == 2:
        dano = random.randrange(5,20,5)
    elif num == 3:
        dano = random.randrange(0,30,5)
    return dano


def atk_player(atk):
    if atk == 1:
        print("Elegiste el ataque fuerte")
        dano = random.randrange(20,70,10)
        return dano, False
    elif atk == 2:
        print("Elegiste el ataque normal")
        dano = random.randrange(10,40,10)
        return dano, True

