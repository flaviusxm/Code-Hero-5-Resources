def vreau_prima_litera(cuvantul):
    if cuvantul:
        return cuvantul[0]
    
    
    
cuvantul=input("Introduceti un fruct pentru a returna prima lui litera :")
litera=vreau_prima_litera(cuvantul)
print(f"Prima litera este {litera}")
