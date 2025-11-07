print ("Benvenuto al gioco del quiz!")

playing = input ("Vuoi giocare?" )
print (playing)

if playing.lower() != "si":
    quit()
print ("Ottimo! Iniziamo il gioco :)!")   
score = 0
answer = input ("Qual è la capitale d'Italia?" )
if answer.lower() == "roma":
    print ("Corretto!")
    score += 1
else:
    print ("Sbagliato!")

answer = input ("Ti piace la pasta?" )
if answer.lower() == "si":
    print ("Anche a me")
    score += 1
else:
    print ("Che strano..")

answer = input ("Quanto fa 5 + 7?" )
if answer.lower() == "12":  
    print ("Corretto!")
    score += 1
else:
    print ("Sbagliato!")     
answer = input ("Ti piace il sushi?" )
if answer.lower() == "si":  
    print ("Fai bene! ")
    score += 1
answer = input ("Ti piace la musica?")
if answer.lower() == "si":
    print ("Ci mancherebbe...")
    

print ("Hai totalizzato" + str(score)+ "domande giuste!") 
print ("Hai totalizzato" + str((score/3) * 100)+ "% di risposte corrette!")

