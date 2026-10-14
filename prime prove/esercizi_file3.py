#Es 1: Il blocco note - Scrivi salva_appunto(testo) che aggiunge testo in fondo al file appunti.txt, su una riga nuova.
#Chiamala tre volte, poi rileggi il file e stampa ogni riga preceduta dal suo numero, partendo da 1. Eseguendo il programma due volte, le righe devono diventare sei.

def salva_appunto(testo):
    with open("appunti.txt", "a", encoding="utf-8") as f:
        f.write(testo + "\n")

salva_appunto("comprare il libro")
salva_appunto("ripassare i file")
salva_appunto("consegnare su GitHub")

with open("appunti.txt", "r", encoding="utf-8") as f:
    for numero, riga in enumerate(f, start=1):
        print(numero, riga.strip())

#Es 2: Contare le righe - Scrivi conta_righe(nome_file) che restituisce due valori: il numero totale di righe e il numero di righe non vuote.
#Provala su dati/parole.txt e su dati/commedia.txt.

def conta_righe(nome_file):
    totali = 0
    piene = 0
    with open(nome_file, "r", encoding="utf-8") as f:
        for riga in f:
            totali += 1
            if riga.strip() != "":
                piene += 1
    return totali, piene

for nome in ["dati/parole.txt", "dati/commedia.txt"]:
    tot, piene = conta_righe(nome)
    print(f"{nome}: {tot} righe, {piene} non vuote")

#Es 3: La parola più lunga della Commedia - Scrivi parola_piu_lunga(nome_file) che scorre il file e restituisce la parola con più caratteri. Togli la punteggiatura dalle estremità di ogni parola prima di misurarla.
#Stampa la parola e la sua lunghezza.
def parola_piu_lunga(nome_file):
    migliore = ""
    with open(nome_file, "r", encoding="utf-8") as f:
        for riga in f:
            for parola in riga.split():
                pulita = parola.strip(".,;:!?«»'\"")
                if len(pulita) > len(migliore):
                    migliore = pulita
    return migliore

p = parola_piu_lunga("dati/commedia.txt")
print(p, "-", len(p), "lettere")

#Es 4: rezzo medio per alimentazione - Scrivi prezzo_medio(nome_file, alimentazione) che legge dati/car_sales_data.csv con csv.DictReader e restituisce il prezzo medio delle sole auto con quel valore nella colonna Fuel type, arrotondato a due decimali.
#Se nessuna auto corrisponde, restituisci None. Provala con Petrol, Diesel, Hybrid e con un valore inesistente.
import csv

def prezzo_medio(nome_file, alimentazione):
    somma = 0
    quante = 0
    with open(nome_file, "r", encoding="utf-8", newline="") as f:
        for auto in csv.DictReader(f):
            if auto["Fuel type"] == alimentazione:
                somma += int(auto["Price"])
                quante += 1
    if quante == 0:
        return None
    return round(somma / quante, 2)

for tipo in ["Petrol", "Diesel", "Hybrid", "Elettrica"]:
    print(tipo, "->", prezzo_medio("dati/car_sales_data.csv", tipo))

#Es 5: Filtra e salva - Scrivi filtra(origine, destinazione, marca, anno_minimo) che legge il CSV delle auto, tiene solo quelle di una certa marca immatricolate dall'anno indicato in poi, e le salva in un nuovo file CSV con tre colonne: Model, Year, Price.
#Ordina le righe per prezzo decrescente. La funzione restituisce quante auto ha salvato. Provala con Porsche e 2015.
import csv

def filtra(origine, destinazione, marca, anno_minimo):
    selezionate = []
    with open(origine, "r", encoding="utf-8", newline="") as f:
        for auto in csv.DictReader(f):
            if auto["Manufacturer"] == marca and int(auto["Year of manufacture"]) >= anno_minimo:
                selezionate.append([auto["Model"], auto["Year of manufacture"], auto["Price"]])

    selezionate.sort(key=lambda r: int(r[2]), reverse=True)

    with open(destinazione, "w", encoding="utf-8", newline="") as f:
        scrittore = csv.writer(f)
        scrittore.writerow(["Model", "Year", "Price"])
        scrittore.writerows(selezionate)

    return len(selezionate)

quante = filtra("dati/car_sales_data.csv", "porsche.csv", "Porsche", 2015)
print("auto salvate:", quante)

with open("porsche.csv", "r", encoding="utf-8") as f:
    for i, riga in enumerate(f):
        if i == 4:
            break
        print(riga.strip())