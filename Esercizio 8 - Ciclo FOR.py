#stampa una lista di nomi con un indice
lista = ["Marco", "Luca", "Giovanni", "Fiks"]
for i, nome in enumerate(lista):
    print(f"Indice: {i}; Nome: {nome}")

#stampa numeri da 1 a 10
for i in range(1, 11):
    print(i)

#stampa i numeri pari da 1 a 15
for i in range(2, 21, 2):
    print(i)

#stampa ogni lettera di una parola
parola = "parola"
for lettera in parola:
    print(lettera)

#somma numero da 1 a 100
somma = 0
for i in range(1, 101):
    somma += i
print(somma)

#stampa tabellina del 3
num = 3
for i in range(1, 11):
    print(f"{num} x {i} ", num * i)

#calcolo vocali in una parola
parola ="programmazione"
vocali =["a", "e", "i", "o", "u"]
somma = 0
for c in parola:
    if c in vocali:
        somma += 1
print(somma)