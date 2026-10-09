# Zakladní cena vstupenky
zakladni_cena = 500

# nákup vstupenek
print ("zadejte údaje pro nákup vstupenek")
vek = int(input("Zadejte věk návštěvníka: "))
je_student = input("Je návštěvník student? (ano/ne): ")
pocet_osob = int (input("Zadejte počet osob: "))

# Podmínka pro žádnou slevu
cena_za_jednu = zakladni_cena
typ_slevy = "žádná sleva"

# Podmínka pro skupinu
if pocet_osob >= 4:
    typ_slevy = "skupinová sleva (25%)"
    cena_za_jednu = zakladni_cena * 0.75

# Podmínka pro studenta
elif je_student and vek <=26 == "ano":
     typ_slevy = "studentská sleva (30%)"  
     cena_za_jednu = zakladni_cena * 0.70

# Podmínka pro seniory
elif vek >= 65:
     typ_slevy = "seniorská sleva (20%)"
     cena_za_jednu = zakladni_cena * 0.80

# Výpočet celkové ceny
celkova_cena = cena_za_jednu * pocet_osob

print ("Typ slevy: ",typ_slevy)
print ("Cena za jednu vstupenku: ", cena_za_jednu, "Kč")
print ("Celková cena za", pocet_osob,"vstupenek:", celkova_cena, "Kč")
