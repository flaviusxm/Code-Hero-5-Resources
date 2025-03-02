#Având în vedere o listă de ani de naștere, creați o funcție care returnează o listă cu vârsta curentă.

def spunemicatianiam(lista):
    varsta=[]
    for an in lista:
        varsta.append(2024-an)
    for i in range(0,len(varsta)):
        print(f"{varsta[i]}")
      
lista_ani=[1980,2003,2008,1990]

    
spunemicatianiam(lista_ani)