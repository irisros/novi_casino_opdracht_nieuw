from main import *

round_number = 1
spin = (round_number * 7) % 37

def choose_guess():
    choice = int(input(f"""Kies één van de volgende opties (0 om te stoppen):
        1: rood
        2: zwart
        3: even
        4: oneven
        0: stop
                  """))
    return choice

def choice_check(choice, saldo):
    if choice == 1:
        exit(1)
    stake = float(input("Hoeveel geld wil je inzetten?: "))
    if stake <= 0:
        print("Dit mag niet. Probeer opnieuw.")
        choice_check(choice, saldo)
    if stake > saldo:
        print("Te weinig saldo. Probeer opnieuw.")
        choice_check(choice, saldo)


def spin_roulette(kleur, odd_even, saldo, stake):
    if spin == 0:
        kleur = "groen"
        odd_even = "geen"
    elif spin <= 18:
        if spin % 2 == 0:
            kleur = "zwart"
            odd_even = "even"
        else:
            kleur = "rood"
            odd_even = "oneven"
    elif spin > 18:
        if spin % 2 == 0:
            kleur = "rood"
            odd_even = "even"
        else:
            kleur = "zwart"
            odd_even = "oneven"
    return kleur, odd_even

def win_decision(win, saldo):
        win = False
        if choice == 1 and kleur == "rood":
            win = True
        elif choice == 2 and kleur == "zwart":
            win = True
        elif choice == 3 and odd_even == "even":
            win = True
        elif choice == 4 and odd_even == "oneven":
            win = True

        if win == True:
            saldo += stake
            print(f'''Je hebt {stake} gewonnen. Je saldo is nu {saldo}''')
        if win == False:
            saldo -= stake
            print(f'''Je hebt {stake} verloren. Je saldo is nu {saldo}''')

        round_number += 1

def play_roulette_main(balance):
    choice = choose_guess()


