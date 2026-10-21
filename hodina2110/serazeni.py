a = int(input("Zadej první číslo: "))
b = int(input("Zadej druhé číslo: "))
c = int(input("Zadej třetí číslo: "))

# např. 7, 10, 2
if a > b:
    p=a
    a=b
    b=p
# (1): 7,10,2
if b > c:
    p=b
    b=c
    c=p
# (2): 7,2,10
if a > b:
    p=a
    a=b
    b=p
# (3): 2,7,10

print (f"{a}<{b}<{c}")
