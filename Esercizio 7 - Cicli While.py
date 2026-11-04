#stampa numeri da 1 a 10
i = 1
while i <= 10:
    print(i)
    i += 1

#stampa solo i numeri pari da 0 a 20
i = 0
while i <= 20:
    print(i)
    i += 2

#somma i numeri da 1 a 10
i = 1
somma = 0

while i <= 10:
    somma += i
    i += 1

print(somma)

#stampa la tabellina del numero 7
num = 7
i = 1
while i <= 10:
    print(f"{num} x {i}: {num * i}")
    i += 1

#calcolare la somma di numeri inseriti dall'utente finchè non digita 0
somma = 0
n = int(input("Inserisci un numero, 0 per uscire:"))

while n != 0:
    somma += n
    n = int(input("Inserisci un numero, 0 per uscire:"))
print("Somma: ", somma)

#indovina il numero
segreto = 7
tentativo = int(input("Indovina il numero: "))
while tentativo != segreto:
    tentativo = int(input("Sbagliato, riprova: "))
print("Hai indovinato!")

#stampa solo numeri dispari fino a 15
i = 1
while i <= 15:
    print(i)
    i += 2

#calcola la somma delle cifre di un numero
n = str(int(input("Inserisci un numero:")))
i = 0
somma = 0
while i < len(n):
    somma += int(n[i])
    i += 1
print(somma)