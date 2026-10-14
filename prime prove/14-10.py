f = open("appunti.txt", "w", encoding="utf-8")
f.write("prima riga\n")

# il file non è ancora chiuso: proviamo a rileggerlo
print("prima di close:", repr(open("appunti.txt", encoding="utf-8").read()))

f.close()
print("dopo close:  ", repr(open("appunti.txt", encoding="utf-8").read()))

#il blocco with 
try:
    with open("appunti.txt", "w", encoding="utf-8") as f:
        f.write("prima riga\n")
        print("dentro il with, chiuso?", f.closed)
except ZeroDivisionError:
    print("il programma è andato in errore")

print("fuori dal with, chiuso?", f.closed)

#mode "w"	Cancella tutto e scrive da zero	Lo crea
with open("lista.txt", "w", encoding="utf-8") as f:
    f.write("mele\n")
    f.write("pere\n")

#mode "a"	Aggiunge in fondo, lascia intatto il resto	Lo crea
with open("lista.txt", "a", encoding="utf-8") as f:
    f.write("banane\n")

#mode "r"	Legge. Non puoi scrivere	Errore FileNotFoundError
with open("lista.txt", "r", encoding="utf-8") as f:
    print(f.read())

print("--- ora riapro in 'w' e scrivo una sola riga ---")

with open("lista.txt", "w", encoding="utf-8") as f:
    f.write("kiwi\n")

with open("lista.txt", "r", encoding="utf-8") as f:
    print(f.read())

#encoding
with open("citta.txt", "w", encoding="utf-8") as f:
    f.write("Forlì")

with open("citta.txt", "r") as f:          # senza encoding
    sbagliato = f.read()

with open("citta.txt", "r", encoding="utf-8") as f:
    giusto = f.read()

print("senza encoding:", len(sbagliato), "caratteri")
print("con encoding: ", len(giusto), "caratteri")

#dataset
with open("dati/car_sales_data.csv", "r", encoding="utf-8") as f:
    intestazione = f.readline().strip().split(",")
    print(intestazione)
    print(len(intestazione), "colonne")

    for i in range(3):
        campi = f.readline().strip().split(",")
        print(campi)

#tutti i campi sono stringhe
somma = 0
quante = 0

with open("dati/car_sales_data.csv", "r", encoding="utf-8") as f:
    f.readline()                       # salta l'intestazione
    for riga in f:
        campi = riga.strip().split(",")
        somma += int(campi[6])         # Price
        quante += 1

print("auto:", quante)
print("prezzo medio:", round(somma / quante, 2))

#il modulo csv
import csv

with open("modelli.csv", "w", encoding="utf-8", newline="") as f:
    f.write('Marca,Modello,Prezzo\n')
    f.write('Ford,"Fiesta, 5 porte",3074\n')

with open("modelli.csv", "r", encoding="utf-8") as f:
    for riga in f:
        print(riga.strip().split(","))

print("--- con il modulo csv ---")
with open("modelli.csv", "r", encoding="utf-8", newline="") as f:
    for campi in csv.reader(f):
        print(campi)

#csv reader 
import csv

with open("dati/car_sales_data.csv", "r", encoding="utf-8", newline="") as f:
    lettore = csv.reader(f)
    intestazione = next(lettore)
    print("colonne:", intestazione)

    for i, campi in enumerate(lettore):
        if i == 3:
            break
        print(campi[0], campi[1], "-", campi[6], "sterline")

#dictreader
import csv

conteggio = {}

with open("dati/car_sales_data.csv", "r", encoding="utf-8", newline="") as f:
    for auto in csv.DictReader(f):
        alimentazione = auto["Fuel type"]
        conteggio[alimentazione] = conteggio.get(alimentazione, 0) + 1

for tipo, quante in conteggio.items():
    print(tipo, quante)

#scrivere un csv
import csv

voti = [
    ["Luca", 7, 6],
    ["Sara", 8, 9],
    ["Marco", 5, 6],
]

with open("voti.csv", "w", encoding="utf-8", newline="") as f:
    scrittore = csv.writer(f)
    scrittore.writerow(["Nome", "Scritto", "Orale"])
    scrittore.writerows(voti)

with open("voti.csv", "r", encoding="utf-8") as f:
    print(f.read())