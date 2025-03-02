def numara_ap_din_cuvant(word):
    verificare = []  
    
    for litera in word:
        if litera not in verificare:  
            contor = 0
            for k in word:  
                if litera == k:
                    contor += 1
            verificare.append(litera)  
            print(f"Litera '{litera}' apare de {contor} ori")

cuvant = input("Introduceti un cuvant de la tastatura: ")

numara_ap_din_cuvant(cuvant)
