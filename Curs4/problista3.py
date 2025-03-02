#Având în vedere lista de mai jos:
#my_list= [5, 2, 8, 10, 15, 6, 7, 12, 20, 1, 9, 14, 3, 18, 4, 11, 19, 17, 13, 16]
#Tipăriți toate numerele impare din lista.

# Lista dată conține mai multe numere întregi
my_list = [5, 2, 8, 10, 15, 6, 7, 12, 20, 1, 9, 14, 3, 18, 4, 11, 19, 17, 13, 16]

# Inițializează variabila `index` cu valoarea 0 pentru a parcurge lista de la început
index = 0

# Buclă `while` pentru a parcurge fiecare element din listă până la final
while index < len(my_list):
    # Verifică dacă elementul curent este impar (restul împărțirii la 2 este diferit de 0)
    if my_list[index] % 2 != 0:
        # Afișează elementul curent dacă este impar
        print(my_list[index])
    
    # Crește indexul pentru a trece la elementul următor din listă
    index += 1

