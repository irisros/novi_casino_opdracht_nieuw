#Dit zijn de gebruiker inputs
voornaam = input("Voornaam: ").title()
achternaam = input("Achternaam: ").title()
geboortedatum = input("Geboortedatum(in format: dd-mm-yyyy): ")
geslacht = input("Geslacht: ").lower()
startbudget = float(input("Startbudget: "))

#Dit zijn de variabelen die leeftijd checken
geboorte_dag, geboorte_maand, geboorte_jaar = geboortedatum.split("-")
MIN_LEEFTIJD = 18
leeftijd = 2026 - int(geboorte_jaar)

#Dit zijn de variabelen voor de kosten.
TOEGANGSTICKET = float(10)
VERPLICHTDRANKJE = float(5)
GOKBELASTING = float(5)
VASTEKOSTEN = float(TOEGANGSTICKET + VERPLICHTDRANKJE + GOKBELASTING)
saldo = float(startbudget - VASTEKOSTEN)

#Dit zijn de variabelen voor het roulette spel
round_number = 1
spin = (round_number * 7) % 37

#dit is een conditie structuur om via de inputs te checken welke aanspreekvorm van toepassing is.
if geslacht == 'vrouw':
    aanspreekvorm = 'mevrouw'
elif geslacht == 'man':
    aanspreekvorm = 'meneer'
else: aanspreekvorm = ''

#Dit is een conditie structuur om te checken of de gebruiker oud genoeg is. Zo niet, sluit het gehele programma af.
if leeftijd < MIN_LEEFTIJD:
    print("Je bent niet oud genoeg om toegang te krijgen tot een casino!")
    exit(1)

#Dit is wat de gebruiker ziet zodra diegene
print(f'''Casino de Gouden Driehoek
-------------------------------------
Welkom, {aanspreekvorm} {voornaam} {achternaam}

Startbudget: €{startbudget:.2f}
Vaste kosten: €{VASTEKOSTEN:.2f}
Saldo: €{saldo:.2f}
''')


if saldo > 0:
    print("Je hebt nog genoeg budget voor toegang tot het casino.")
elif saldo < 0:
    print("Je hebt niet genoeg budget voor toegang tot het casino")

while True:
    print(f"""Kies één van de volgende opties:
    1: rood
    2: zwart
    3: even
    4: oneven
    0: stop
          """)
    kleur = ""
    odd_even = ""
    choice = int(input("Kies je gok! (0 om te stoppen): "))
    if choice == 0:
        break
    stake = float(input("Hoeveel geld wil je inzetten?: "))
    if stake <= 0:
        print("Dit mag niet. Probeer opnieuw.")
        continue
    if stake > saldo:
        print("Te weinig saldo. Probeer opnieuw.")
        continue
    saldo -= stake
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

    round_number +=1

print(f'''Je eindsaldo is {saldo}. Tot ziens.''')
























