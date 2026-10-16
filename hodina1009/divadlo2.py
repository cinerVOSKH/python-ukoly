# Základní cena
zakladni_cena = 500

# Vstupy
vek = int(input("Zadejte věk: "))
pocet_osob = int(input("Zadejte počet osob: "))
je_student = input("Je student? (ano/ne): ")
den = input("Zadejte den v týdnu (např. sobota): ")

# Víkendový příplatek 
priplatek = 50 if den == "sobota" or den == "neděle" else 0
cena_za_jednu = zakladni_cena + priplatek

# Výpočet slevy
typ_slevy = "žádná sleva"

if pocet_osob >= 4:
    typ_slevy = "skupinová sleva (25%)"
    cena_za_jednu *= 0.75  
elif je_student == "ano" and vek <= 26:
    typ_slevy = "studentská sleva (30%)"  
    cena_za_jednu *= 0.70  
elif vek >= 65:
    typ_slevy = "seniorská sleva (20%)"
    cena_za_jednu *= 0.80  

# Výpočet celkové ceny
celkova_cena = cena_za_jednu * pocet_osob

# Skloňování 
slovo = "osoba" if pocet_osob == 1 else ("osoby" if 2 <= pocet_osob <= 4 else "osob")

# účtenka 
print("\n--- SHRNUTÍ NÁKUPU ---")
print("Den v týdnu:", den)
print("Víkendový příplatek:", priplatek, "Kč")
print("Uplatněná sleva:", typ_slevy)
print("Cena za 1 vstupenku:", cena_za_jednu, "Kč")
print(f"Celková cena za {pocet_osob} {slovo}: {celkova_cena} Kč")