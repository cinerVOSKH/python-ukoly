import random

# Krok 1: Vygenerovani cisla
tajne_cislo = random.randint(1, 20)

# promenne
pokusy = 0
max_pokusu = 5
tip = 0

print("Ahoj! Vitej ve hre.")
print("Myslim si cislo od 1 do 20. Mas na to maximalne {max_pokusu} pokusy.")

# Hlavni cyklus hry 
while tip != tajne_cislo and pokusy < max_pokusu:
    try:
    except ValueError:
        print("To neni latne cele cislo! Zkus to znovu")
        continue

    # Vyzva B: Kontrola rozsahu vstupu 
    if tip < 1 or tip > 20:
        print("Zadal jsi cislo mimo rozsah (1-20)!")
        continue

