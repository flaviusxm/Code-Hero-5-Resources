def minicalculator():
    print("Salut! Hai sa calculam!")
    while True:
        print("\nMeniu:")
        print("1. Adunare")
        print("2. Scadere")
        print("3. Inmultire")
        print("4. Impartire")
        print("5. Exit")
        optiune = int(input("Alege o optiune (1-4) sau apasa 5 pentru iesire: "))
        
        if 1 <= optiune <= 4:
            a = float(input("Introdu primul numar: "))
            b = float(input("Introdu al doilea numar: "))
            if optiune == 1:
                print(f"Rezultatul este: {a + b}")
            elif optiune == 2:
                print(f"Rezultatul este: {a - b}")
            elif optiune == 3:
                print(f"Rezultatul este: {a * b}")
            elif optiune == 4:
                if b != 0:
                    print(f"Rezultatul este: {a / b}")
                else:
                    print("Impartirea la zero nu este permisa aici!")
        elif optiune == 5:
            print("La revedere! O zi frumoasa!")
            break
        else:
            print(" Incearca din nou !!! ")

minicalculator()
