a = 5
b = 2
c = 7

x = float(input("Zadej číslo: "))

a=float (input("Zadej číslo a: "))
b=float (input("Zadej číslo b: "))
c=float (input("Zadej číslo c: "))

min = a
max = a
if b < min:
    min = b
if c < min:
    min = c
else:
    if c > max:
        max = c
print(f'Minimum: {min}\nMaximum: {max}')

