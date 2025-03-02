#verificam fructele disponibile dintr un magazin
ananas=True
banane=False
mere=True
zmeura=False

fructe_disponibile=0

if ananas==True :
    fructe_disponibile=fructe_disponibile+1
    #fructe_disponibile+=1 atribuire identica cu cea de mai sus
    
if banane==True:
    fructe_disponibile+=1
    
if mere==True:
    fructe_disponibile=fructe_disponibile+1

if zmeura==True:
    fructe_disponibile+=1

print(f"NR. fructe disponibile : {fructe_disponibile}")