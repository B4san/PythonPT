# Minijuego de lucha utilizando todos los modulos basicos de Python
import sys
import ataque
import stats

def inicio():
    print("Bienvenido al minijuego de lucha!")
    print("Antes de iniciar es necesario que eligas una dificultad")
    print("1. Facil")
    print("2. Medio")
    print("3. Dificil")
    print("#. Salir")
    numero = int(input("=>"))
    return numero

def dificultad(num):
    if num == 1:
        print("Dificultad fácil seleccionada. Pelearas contra un Paladin")
        return 100
    elif num == 2:
        print("Dificultad media seleccionada. Pelearas contra un Ogro")
        return 200
    elif num == 3:
        print("Dificultad difícil seleccionada. Pelearas contra un Mago")
        return 300
    else:
        print("Opción no válida.")

def main():
    numero = inicio()
    hp_enemy = dificultad(numero)
    print("**************")
    hp = 100
    turno = True
    print("Tu batalla comienza!")
    while hp_enemy > 0 and hp > 0:
        ataque_enemigo = ataque.atk_enemy(numero)
        print("El ataque de tu enemigo fue de {}".format(ataque_enemigo))
        hp = hp - ataque_enemigo
        if hp > 0:
            if turno == True:
                stats.stats(hp, hp_enemy)
                print("Es tu turno de atacar")
                print("Elige tu ataque:")
                print("1. Ataque fuerte (20-60 de daño, 50% de probabilidad de acertar)")
                print("2. Ataque normal (10-30 de daño, 100% de probabilidad de acertar)")
                mi_atque = int(input("=>"))
                ataques = ataque.atk_player(mi_atque)
                mi_dano = ataques[0]
                turno = ataques[1]
                print("Tu ataque fue de {}".format(mi_dano))
                hp_enemy = hp_enemy - mi_dano
                if hp_enemy <= 0:
                    exit("Has derrotado a tu enemigo!")
                else:
                    stats.stats(hp, hp_enemy)
                    pass

        else:
            exit("Has perdido la batalla")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(0)






