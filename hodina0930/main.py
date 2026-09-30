# **********************************
# Kalkulačka spropitného
# 30. 9. 2026
# **********************************

print("KALKULAČKA SPROPITNÉHO")    # tisk nadpisu
celkova_cena = float(input("Zadejte celkovou cenu: "))    
# celkova_cena = float(celkova_cena)        
spropitne = int(input("Zadej spropitné v % :"))
pocet_lidi = int(input("Zadej počet lidí: "))

celkova_cena = celkova_cena + celkova_cena * spropitne / 100
print(celkova_cena)

cena_jeden = round(celkova_cena / pocet_lidi + 0.5)
print(cena_jeden)
print(f"Cena za jednoho: {cena_jeden}")
      