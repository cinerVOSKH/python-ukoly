import random

# Krok 1: Příprava náhodného čísla a proměnných
tajne_cislo = random.randint(1, 20)
pokusy = 0
max_pokusu = 5  # Výzva A

print("Vítej ve hře Hádej číslo! Myslím si číslo od 1 do 20.")
print(f"Máš celkem {max_pokusu} pokusy na uhádnutí.\n")

# Krok 2: Hlavní cyklus hry
tip = 0
while tip != tajne_cislo and pokusy < max_pokusu:
  # Načtení vstupu 
  try:
    tip = int(input("Zadej svůj tip: "))
  except ValueError:
    print("To není platné celé číslo!")
    continue

  # Výzva B
  if tip < 1 or tip > 20:
    print("Zadal jsi číslo mimo rozsah (1–20)!")
    continue

  # Krok 3: Počítadlo pokusů 
  pokusy += 1

  # Porovnání tipu s tajemným číslem
  if tip < tajne_cislo:
    print("Moje číslo je VĚTŠÍ!")
  elif tip > tajne_cislo:
    print("Moje číslo je MENŠÍ!")
  else:
    # Jakmile hráč uhodne, cyklus skončí a vypíše se gratulace
    print(f"Gratuluji! Uhodl jsi číslo {tajne_cislo} na {pokusy}. pokus.")

# Výzva A kontrola
if tip != tajne_cislo and pokusy >= max_pokusu:
  print(f"\nBohužel ti došly pokusy! Tajné číslo bylo {tajne_cislo}.")

