#Cautam intr o lista si intr un interval dat  == > numerele pare 
def lista_numere_pare():
    lista_numere=[]
    print("Introduceti numere de la tastatura: ")
    while True :
        numar_introdus=input("Introduceti numarul: ")
        if numar_introdus.lower()=="stop":  #STOP => stop 
            break
        #variabila=int(numar_introdus)
        lista_numere.append(int(numar_introdus))
    print(f"Lista de numere introduse de la tastatura este : {lista_numere} ")
    
    print("!!! WARNING !!! Aveti grija sa va incadrati in lungimea listei introduse: ")
    
    print(f" Lungime lista {len(lista_numere)}")
    
    inceput=int(input("Introduceti capatul inferior al intervalului: "))
    sfarsit=int(input("Introduceti capatul superior al intervalului: "))
    
    lista_interval=lista_numere[inceput:sfarsit]
    
    lista_pare=[]
    contor=0
    while contor<len(lista_interval):
        
        if lista_interval[contor]%2==0:
            lista_pare.append(lista_interval[contor])
            
        contor+=1
    print(f"Lista cu numerele pare este: {lista_pare}")
    
    
    
lista_numere_pare()