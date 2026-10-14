#comando print 
print("Ciao 4BI mi siete mancati")

#print con variabili 
nome = "Sara"
eta = 17
media = 7.5
promossa = True

print(type(nome), type(eta), type(media), type(promossa))
print(f"{nome} ha {eta} anni e una media del {media}") #stampa di più variabili nella stessa riga di codice 
print(f"Fra due anni {nome} ne avrà {eta + 2}")

#operatori
print(7 / 2)
print(7 // 2)
print(7 % 2)
print(2 ** 10)
print(int("42") + 1)
print("42" + "1")
#print("42" + 1) non si può sommare un numero ad una stringa

#if 
voto = 6.5
if voto >= 6:
    esito = "sufficiente"
elif voto >= 5:
    esito=" insufficienza lieve"
else:
    esito="insufficenza grave"
print(esito)

#ciclo for
for i in range(3):
    print(f"giro {i}")

numeri = [4, 8, 15]
for n in numeri:
    print(n * 2)

for i in range(1,11):
    print(f"giro {i}")

numeri = [4, 8, 15]
for n in numeri:
    if n==8:
        break
    print(n*2)
for n in numeri:
    if n==8:
       continue
    print(n*2)

 #funzioni
def area_rettangolo(base, altezza):
    return base * altezza

print(area_rettangolo(3, 4))  

#funzione tupla
def dividi(a, b):
    if b == 0:
        return None, "divisione per zero"
    return a / b, "ok"

risultato, stato = dividi(10, 4)
print(risultato, stato)

risultato, stato = dividi(10, 0)
print(risultato, stato)


def ciao(a,b):
    if b==0:
        return None, "divisione per zero", "non ok"
    return a//b, a%b, "ok"
risultato, stato, up = ciao(8, 6)
print(risultato, stato, up)

risultato, stato,up = ciao(7, 0)
print(risultato,stato,up)

#Parametri e default
def saluta(nome, saluto="Ciao"):
    return f"{saluto}, {nome}!"

print(saluta("Luca"))
print(saluta("Sara", "Buongiorno"))
print(saluta(saluto="Salve", nome="Marco"))

def mamma(nome, saluto = "ciao, come è andata a scuola", risposta="boh"):
    return f"{saluto}, {nome}, {risposta}"
print(mamma("Giulia"))
print(mamma("Sara", "Buongiorno"))
print(mamma(saluto="Salve", nome="Marco"))

#La trappola dei float
totale = 0.0
for _ in range(10):
    totale += 0.1

print(totale)
print(totale == 1.0)
print(round(totale, 10) == 1.0)

#esercizi
#Es 1 Conversione di temperatura
#Scrivi una funzione celsius_a_fahrenheit(gradi) che restituisce i gradi Fahrenheit. La formula è F = C × 9/5 + 32.
#Stampa il risultato per 0, 25 e 100 gradi, usando una f-string: 25°C corrispondono a 77.0°F.

def celsius_a_fahrenheit(gradi):
   return gradi*9/5 + 32
for num in [0,25,100]:
    print(f"{num}  °C corrispondono a {celsius_a_fahrenheit(num)} °F")

#Es 2 pari o dispari
#Scrivi e_pari(n) che restituisce True se n è pari. Usa l'operatore %. Poi stampa i numeri pari da 1 a 20 usando la tua funzione.

def e_pari(n):
    if n % 2 == 0:
        return True
for i in range ( 1,21): 
    if e_pari(i):
        print(i)

