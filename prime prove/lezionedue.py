#lezione due
#liste 
voti = [6, 8, 5, 8, 7]

voti.append(9)
voti.insert(0, 4)
print(voti)

print(voti[0], voti[-1])
print(voti[1:4])

voti.sort()
print(voti)

print(len(voti), 8 in voti)

voti=[8,8,3,10,5]

voti.append(6)
voti.insert(1,6)
print(voti)

print(voti[0], voti[-1])
print(voti[1:5])

voti.sort()
print(voti)
print(len(voti), 6 in voti)

#set
presenze = ["Luca", "Sara", "Marco", "Luca", "Sara"]
unici = set(presenze)

print(len(presenze), "voci registrate")
print(len(unici), "persone diverse")
print(sorted(unici))

ingredienti=["patate", "pomodori", "pomodori", "basilico", "prezzemolo", "patate"]
unico= set(ingredienti)

print(len(ingredienti), "ingredienti nella lista")
print(len(unico), "ingredienti che bisogna comprare")
print(sorted(unico))

#tuple
week = ("lun", "mar", "mer", "gio", "ven")
print(week)
print(week[0], week[-1])
print(len(week))

try:
    week[0] = "dom"
except TypeError as errore:
    print("TypeError:", errore)

#dizionari
capitali = {"Italia": "Roma", "Francia": "Parigi", "Spagna": "Madrid"}

print(capitali["Italia"])
print(len(capitali))

capitali["Germania"] = "Berlino"
del capitali["Spagna"]
print(capitali)

for paese, citta in capitali.items():
    print(paese, "->", citta)

print(list(capitali.keys()))
print(list(capitali.values()))


capitali = {"Italia": "Roma", "Francia": "Parigi"}

print(capitali.get("Francia"))
print(capitali.get("Germania"))
print(capitali.get("Germania", "non in elenco"))
print("Germania" in capitali)


#esercizi:
#1.Scrivi conta_unici(nomi) che riceve una lista di nomi, anche ripetuti, e restituisce quante persone diverse contiene. Provala su ["Luca", "Sara", "Marco", "Luca", "Giulia", "Sara", "Luca"].

persone=  ["Luca", "Sara", "Marco", "Luca", "Giulia", "Sara", "Luca"]
unici = set(persone)

print(len(unici), "persone diverse")
print(sorted(unici))


#2.Parti dal dizionario {"Italia": "Roma", "Francia": "Parigi", "Spagna": "Madrid"}. Scrivi capitale(paese) che restituisce la capitale, e la stringa "paese non in elenco" se il paese non c'è.
#La funzione non deve mai andare in errore, qualunque cosa le passi.

capitali={"Italia": "Roma", "Francia": "Parigi", "Spagna": "Madrid"}
def capitale(paese):
    return capitali.get(paese, "paese non in elenco") #diz.get("chiave", val)

print(capitale("Italia"))
print(capitale("Francia"))
print(capitale("Spagna"))
print(capitale("Portogallo"))

#4. Scrivi senza_duplicati(elementi) che elimina i doppioni mantenendo l'ordine di prima comparsa. Su ["Sara", "Luca", "Sara", "Marco", "Luca", "Giulia"] deve restituire ['Sara', 'Luca', 'Marco', 'Giulia'].
#Il set da solo non basta: leggi bene perché.

def senza_duplicati(elementi):
    visti = set()
    risultato = []
    for e in elementi:
        if e not in visti:
            visti.add(e)
            risultato.append(e)
    return risultato

nomi = ["Sara", "Luca", "Sara", "Marco", "Luca", "Giulia"]
print(senza_duplicati(nomi))
print(sorted(set(nomi)))

#5.Scrivi conta_parole(frase) che restituisce quante volte compare ogni parola. Ignora le maiuscole. Poi stampa la parola più frequente e il suo conteggio.
#Provala su "il gatto dorme il cane dorme il topo corre". La struttura da usare devi sceglierla tu.

def conta_parole(frase):
    conteggio = {}
    for parola in frase.lower().split():
        conteggio[parola] = conteggio.get(parola, 0) + 1
    return conteggio

frase = "il gatto dorme il cane dorme il topo corre"
risultato = conta_parole(frase)
print(risultato)

piu_frequente = max(risultato, key=risultato.get)
print(piu_frequente, risultato[piu_frequente])