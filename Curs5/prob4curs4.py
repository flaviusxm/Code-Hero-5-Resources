lista_numere=[]
while True:
    numar=input("Introduceti un numar (de preferat sa fie pozitiv)/ daca introduceti -1 programul se opreste: ")
    numar=int(numar)
    if numar==-1:
        break
    
    if numar==1:
        print(f"Numarul {numar} nu este prim: ")
        continue
    
    if numar>1:
        contor_divizori=1
        index=1
        while index<numar:
            if numar%index==0:
                contor_divizori=contor_divizori+1 #contor_divizori+=1 la fel la executie
            index+=1
            
        if contor_divizori==2:
            lista_numere.append(numar)
            print(f"Numarul a fost adaugat in lista")
        else:
            print(f"Numarul {numar} nu este prim ")

print(f"Lista cu numere prime este {lista_numere}")
                
        
    
    