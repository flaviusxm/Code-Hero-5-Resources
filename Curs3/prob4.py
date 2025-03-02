# Cere două numere, primul mai mare decât al doilea. 
# Înmulțiți al doilea număr cu 3 până când este mai mare decât primul număr.
numarul_1 = int(input(" Introduceti numarul1: "))
numarul_2 = int(input(" Introduceti numarul2: "))

while numarul_2 < numarul_1 :
    numarul_2 = numarul_2 * 3
    
print(f"Rezultatul final este: {numarul_2}")