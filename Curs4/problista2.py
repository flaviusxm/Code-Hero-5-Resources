#Scrieți un program care cere utilizatorului să introducă numere pare până când este introdus 0. Programul va verifica dacă numărul este par și îl va adăuga la o listă.
#Când programul se va termina, tipăriți lista.

# Creează o listă goală în care vor fi adăugate numerele pare introduse de utilizator
lista_pare = []

# Solicită utilizatorului să introducă un număr par și îl convertește într-un număr întreg
numar = int(input("Introduceți un număr par (0 pentru a termina): "))

# Continuă să ceară numere până când utilizatorul introduce 0
while numar != 0:
    # Verifică dacă numărul este par (divizibil cu 2 fără rest)
    if numar % 2 == 0:
        # Adaugă numărul la listă dacă este par
        lista_pare.append(numar)
    else:
        # Afișează un mesaj de eroare dacă numărul introdus nu este par
        print("Numărul nu este par. Încercați din nou.")
    
    # Cere un nou număr pentru a continua sau a încheia programul dacă este 0
    numar = int(input("Introduceți un număr par (0 pentru a termina): "))

# Afișează lista finală cu toate numerele pare introduse
print("Lista numerelor pare introduse:", lista_pare)
