print("Vítej ve hře! Mysli si číslo od 1 do 100.")
print("Budu hádat a ty mi budeš odpovídat:")
print("  'v' = moje číslo je VĚTŠÍ (tvá odpověď: v)")
print("  'm' = moje číslo je MENŠÍ (tvá odpověď: m)")
print("  's' = trefil ses, je to SPRÁVNĚ (tvá odpověď: s)\n")

# Krok 1: Nastavení hranic a proměnných
dole = 1
nahore = 100
pokusy = 0
odpoved = ""

# Krok 2: Hlavní cyklus 
while odpoved != "s":
  # Počítač vezme střed aktuálního intervalu
  tip = (dole + nahore) // 2
  pokusy += 1

  # Zeptáme se uživatele
  odpoved = input(
      f"Můj tip je {tip}. Je to správně (s), větší (v), nebo menší (m)? "
  )

  # Krok 3: Úprava hranic podle odpovědi hráče
  if odpoved == "v":
    dole = tip + 1  # protože tvé číslo je větší, posuneme spodní hranici
  elif odpoved == "m":
    nahore = tip - 1  # protože tvé číslo je menší, posuneme horní hranici
  elif odpoved == "s":
    print(
        f"Super! Uhodl jsem tvé číslo {tip} celkem na {pokusy}. pokus(ů)."
    )
  else:
    print("Nerozumím, zadej prosím jen 'v', 'm' nebo 's'.")