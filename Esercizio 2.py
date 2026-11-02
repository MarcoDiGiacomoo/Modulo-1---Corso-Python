# Chieda all’utente di inserire un numero intero. 
# Converta questo numero in numero decimale (float) e lo stampi. 
# Converta lo stesso numero in stringa e lo stampi insieme a un messaggio

num = int(input("Inserisci un numero intero"))
num = float(num)
print(num, type(num))
try:
    num = str(num)
    print(num, type(num))
except ValueError:
    print("Non si può convertire")