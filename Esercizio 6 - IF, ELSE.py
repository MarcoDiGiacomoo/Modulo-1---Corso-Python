x = -10
if x >= 0:
    print("positivo")
else:
    print("negativo")

a = 3
b = 7
if a > b:
    print("A > B")
elif a == b:
    print("A = B")
else:
    print("B > A")

#chiedo numero in input e verifico se positivo, negativo o 0
numero = float(input("Inserisci un numero:"))

if numero > 0:
    print(f"{numero} è positivo")
elif numero == 0:
    print("Il tuo numero è Zero")
else:
    print(f"{numero} è negativo")

#valuto il voto
voto = int(input("Inserisci il voto da 0 a 100: "))

if voto < 60:
    print("Insufficiente")
elif voto >=60 and voto < 80:
    print("Sufficiente")
elif voto >=80 and voto < 90:
    print("Buono")
else:
    print("Ottimo")

eta = int(input("Inserisci la tua età: "))
if eta < 12:
    print("Prezzo 5$")
elif eta >=12 and eta <= 64:
    print("Prezzo 10$")
else:
    print("Prezzo 7$")