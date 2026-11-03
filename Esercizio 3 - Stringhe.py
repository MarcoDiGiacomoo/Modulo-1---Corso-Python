testo = "python"
print("Primi due caratteri:",testo[0:2])

testo = "ComPUteR"
print(testo.upper())
print(testo.lower())
print(testo.capitalize())

testo = "programmazione"
lettera = "a"
conteggio = testo.count(lettera)
print(f"La lettera {lettera} appare {conteggio} volte")

testo = "fantastico"
print(testo.startswith("f"))
print(testo.endswith("o"))

testo = "python"
print(testo[::-1])

testo = " Ciao Mondo "
print(testo.strip())
print(testo.lstrip())
print(testo.rstrip())

parola = "Programmazione"
print(parola[0:3]*3)