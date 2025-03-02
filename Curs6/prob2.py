#media a 3 numere prin functie 
def media_celor_trei(a,b,c):
    
    return (a+b+c)/3


numarx=int(input("Introduceti numarul 1: "))
numary=int(input("Introduceti numarul 2: "))
numarz=int(input("Introduceti numarul 3: "))
rezultat=media_celor_trei(numarx,numary,numarz)

print(f"Media celor 3 numere introduse de la tastatura este: {rezultat:.6f}")