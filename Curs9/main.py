DEX = {}

def incarcare():
        with open("DEX.txt", "r") as file:
            linie = file.readlines()
            for i in range(0, len(linie), 2):
                cuvant = linie[i].strip()
                explicatie = linie[i+1].strip()
                DEX[cuvant] = explicatie
   
def salvam():
    with open("DEX.txt", "w") as file: 
        for cuvant, explicatie in DEX.items():
            file.write(f"{cuvant}\n{explicatie}\n")

def adaugare():
    cuvant = input("Introduceti cuvantul : ")
    explicatie = input("Introduceti explicatia : ")
    DEX[cuvant] = explicatie
    print(f"Cuvantul '{cuvant}' si sensul '{explicatie}' au fost adaugate in DEX")
    salvam()

def cauta():
    cuvant = input("Introduceti cuvantul pe care il cautati : ")
    if cuvant in DEX:
        print(f"Semnificatia cuv. '{cuvant}' este '{DEX[cuvant]}'")
    else:
        print(f"Cuvantul '{cuvant}' nu a fost gasit !!!")

def afiseaza():
    if not DEX:
        print("Dictionarul este gol !!!")
    else:
        print("Cuvintele din DEX sunt : ")
        for cuvant, explicatie in DEX.items():
            print(f"{cuvant} : {explicatie}")

def afiseaza_meniu():
    print("\nMeniu:")
    print("1. Adauga cuvant")
    print("2. Cauta cuvant")
    print("3. Afiseaza DEX")
    print("4. La revedere")

def main():
    incarcare()
    while True:
        afiseaza_meniu()
        alegere = int(input("Alegeti o optiune (1-4): "))
        if alegere == 1:
            adaugare()
        elif alegere == 2:
            cauta()
        elif alegere == 3:
            afiseaza()
        elif alegere == 4:
            print("La revedere!!! Pa paaaa")
            break
        else:
            print("Optiune gresita")

if __name__ == "__main__":
    main()
