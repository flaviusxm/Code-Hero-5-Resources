# Scrieți un program care permite utilizatorului să introducă o listă de numere întregi.
# Introducerea de numere continuă până când utilizatorul introduce 0, moment în care lista se finalizează.
# Programul va afișa lista completă și va determina cel mai mare număr din listă.

my_list = []  # Inițializează o listă goală în care vor fi adăugate numerele

# Afișează un mesaj pentru a informa utilizatorul cum funcționează introducerea de date
print("Introduceți numere întregi (introduceți 0 pentru a termina):")

# Bucla infinită pentru a permite introducerea de numere până la introducerea lui 0
while True:
    # Solicită un număr de la utilizator și îl convertește într-un număr întreg
    numar = int(input("Număr: "))
    # Verifică dacă numărul este diferit de 0
    if numar != 0:
        # Dacă numărul nu este 0, adaugă-l la listă
        my_list.append(numar)
    else:
        # Dacă numărul este 0, afișează lista completă și termină bucla
        print("Lista introdusă este:", my_list)
        break

# Inițializează variabila `maxim` cu ultimul element din listă, folosind `pop` pentru a-l elimina din listă
maxim = my_list.pop()  

# Bucla `while` pentru a parcurge elementele rămase din listă și a găsi maximul
while my_list: 
    # Scoate ultimul element din listă pentru comparare
    numar = my_list.pop()
    # Verifică dacă acest element este mai mare decât `maxim` și, dacă da, actualizează valoarea lui `maxim`
    if numar > maxim:
        maxim = numar

# Afișează cel mai mare număr găsit în listă
print("Cel mai mare număr este:", maxim)
