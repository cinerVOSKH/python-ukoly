# Pozdrav podle zadané hodiny
hodina = int(input("Zadejte hodinu (0-23): "))


if hodina < 0:
    print("Hodina nemůže být záporná.")


elif hodina > 23:
    print("Dobrou noc")

# Samotné pozdravy
elif hodina >= 5 and hodina <= 8:
    print("Dobré ráno")

elif hodina >= 9 and hodina <= 12:
    print("Dobré dopoledne")

elif hodina >= 13 and hodina <= 17:
    print("Dobré odpoledne")

elif hodina >= 18 and hodina <= 21:
    print("Dobrý večer")

