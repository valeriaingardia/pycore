# try if/elif/else 
# f string
# input all'utente 
# revisione 

def salvadanio():
    saldo = 0.0

    print("1. Aggiungi denaro")
    print("2. Mostra l'importo disponibile")
    print("3. Preleva denaro")

    scelta = input("Scegli un'opzione (1-3): ")

    if scelta == "1":
        aggiunta = float(input("Quanto denaro vuoi aggiungere? "))
        saldo += aggiunta
        print(f"Hai aggiunto: {aggiunta:.2f}€")
        print(f"Il tuo nuovo saldo è di: {saldo:.2f}€")

    elif scelta == "2":
        print(f"Saldo disponibile: {saldo:.2f}€")

    elif scelta == "3":
        prelievo = float(input("Quanto denaro vuoi prelevare? "))
        if prelievo <= saldo:
            saldo -= prelievo
            print(f"Hai prelevato: {prelievo:.2f}€")
            print(f"Saldo attuale: {saldo:.2f}€")
        else:
            print("Saldo insufficiente!")

    else:
        print("Scelta non valida.")

salvadanio()


