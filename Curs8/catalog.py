# Exercitiu 1
# Realizam un catalog virtual
lista=[] #lista
catalog={} #dictionar
nume=input("Va rugam introduceti numele elevilor prin spatiu ( separate ): ").split()

for copil in nume:
    note=input("Va rugam introduceti notele elevilor prin spatiu ( separate ): ").split()
    note_catalog=[]
    
    for i in note:
        note_catalog.append(int(i))
        
    catalog[copil]=note_catalog

print("Catalogul este: ",catalog)