# Scrieți un program care permite utilizatorului să introducă informațiile despre mai mulți copii.
# Pentru fiecare copil, utilizatorul va introduce: Nume, Prenume, Școala și Vârstă.
# Procesul de introducere continuă până când utilizatorul introduce exact "stop" în loc de nume, moment în care se finalizează.
# Programul va afișa apoi lista completă a copiilor înregistrați, cu toate informațiile lor.

# Inițializăm lista pentru a stoca informațiile copiilor
copii = []

# Mesaj pentru a informa utilizatorul despre modul de introducere a datelor
print("Introduceți informațiile dvs (introduceți 'stop' pentru a termina):")

# Inițializăm `nume` cu un șir gol (sau orice altă valoare) pentru a începe bucla
nume = ""

# Bucla continuă până când `nume` devine exact "stop"
while nume != "stop":
    # Solicită utilizatorului să introducă numele copilului
    nume = input("Nume: ")
    # Verifică dacă numele este "stop" pentru a termina introducerea
    if nume == "stop":
        break

    # Solicită prenumele, școala și vârsta copilului dacă numele nu este "stop"
    prenume = input("Prenume: ")
    scoala = input("Școala: ")
    varsta = input("Vârstă: ")

    # Adăugăm informațiile copilului într-o listă și o stocăm în lista principală `copii`
    copil = [nume, prenume, scoala, varsta]
    copii.append(copil)

# Mesaj care marchează începerea afișării listei cu informațiile copiilor
print("\nLista copiilor înregistrați:")

# Inițializează un index pentru a parcurge fiecare copil din listă folosind o buclă `while`
index = 0
while index < len(copii):
    # Preia informațiile copilului aflat la poziția `index` în lista `copii`
    copil = copii[index]
    # Afișează informațiile copilului, folosind accesarea pe baza indexului fiecărui atribut
    print(f"Nume: {copil[0]}, Prenume: {copil[1]}, Școala: {copil[2]}, Vârstă: {copil[3]}")
    # Incrementează indexul pentru a trece la următorul copil din listă
    index += 1
