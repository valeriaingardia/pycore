import math
 # importo la libreria math

def distanza(x1, y1, x2, y2):
    return math.sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2))

# definisco una funzione def distanza
# cui return è il modo di calcolo di distanza cartesiana, la risoluzione;
# elevo ciascuna differenza al quadrato con pow(x1-x2, 2) e + (sommo) (y1-y2,2) quest'ultima differenza elevato con pow a 2 
def main():
    print("Distanza tra punti")
    x1 = float(input("Inserisci x1: "))
    y1 = float(input("Inserisci y1: "))
    x2 = float(input("Inserisci x2: "))
    y2 = float(input("Inserisci y2: "))

# dichiaro un'altra funzione main 
# chiedo all'utente di inserire: x1,y1,x2,y2


    print("La distanza tra i due punti è:", distanza(x1, y1, x2, y2))

    # stampo a schermo la risoluzione 

main()
# chiamo la funzione main.

