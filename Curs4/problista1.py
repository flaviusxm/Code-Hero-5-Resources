#Scrieți un program care să solicite utilizatorului introducerea de la tastatură până când este introdus 0 (zero). 
#Adăugați elementele introduse în listă.
#Tipăriți lista. 
# Creează o listă goală în care vor fi adăugate numerele introduse de utilizator
lista_numere = []

# Inițializează variabila `numar` cu o valoare nenulă pentru a intra în bucla `while`
numar = 1

# Repetă cererea de introducere a unui număr până când utilizatorul introduce 0
while numar != 0:
    # Solicită utilizatorului să introducă un număr și îl convertește într-un număr întreg
    numar = int(input("Introduceți un număr (0 pentru a opri): "))
    
    # Verifică dacă numărul introdus nu este 0
    if numar != 0:
        # Adaugă numărul la listă dacă nu este 0
        lista_numere.append(numar)

# Afișează lista de numere introduse de utilizator, excluzând 0
print("Lista numerelor introduse este:", lista_numere)
