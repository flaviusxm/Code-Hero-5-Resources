# Solicită utilizatorului să introducă numele primului produs
produs1 = input("Introduceti numele produsului: ")
# Solicită utilizatorului să introducă prețul primului produs și îl convertește într-un număr întreg
pret1 = int(input(f"Introduceti pretul pentru {produs1} : "))

# Solicită utilizatorului să introducă numele celui de-al doilea produs
produs2 = input("Introduceti numele produsului: ")
# Solicită utilizatorului să introducă prețul celui de-al doilea produs și îl convertește într-un număr întreg
pret2 = int(input(f"Introduceti pretul pentru {produs2} : "))

# Solicită utilizatorului să introducă numele celui de-al treilea produs
produs3 = input("Introduceti numele produsului: ")
# Solicită utilizatorului să introducă prețul celui de-al treilea produs și îl convertește într-un număr întreg
pret3 = int(input(f"Introduceti pretul pentru {produs3} : "))

# Solicită utilizatorului să introducă numele celui de-al patrulea produs
produs4 = input("Introduceti numele produsului: ")
# Solicită utilizatorului să introducă prețul celui de-al patrulea produs și îl convertește într-un număr întreg
pret4 = int(input(f"Introduceti pretul pentru {produs4} : "))

# Calculează suma totală de plată prin adunarea prețurilor celor patru produse
suma_de_plata = pret1 + pret2 + pret3 + pret4

# Afișează utilizatorului totalul de plată pentru produsele achiziționate
print(f"Totalul de plata pentru produsele {produs1}, {produs2}, {produs3}, {produs4} este {suma_de_plata}")

# Solicită utilizatorului să introducă suma cu care intenționează să achite produsele
plata_client = int(input("Introduceti suma pentru a cumpara produsele: "))

# Verifică dacă suma introdusă de client este mai mică decât suma de plată
while plata_client < suma_de_plata:
    # Calculează diferența dintre suma totală de plată și suma introdusă de client
    diferenta = suma_de_plata - plata_client
    # Informează utilizatorul despre suma suplimentară necesară
    print(f"Suma introdusa nu este suficienta. Mai trebuie {diferenta}")
    # Solicită utilizatorului să introducă restul de bani
    cat_mai_avem_de_platit = int(input("Introduceti restul de bani "))
    # Adaugă suma introdusă la totalul sumei plătite de client
    plata_client = plata_client + cat_mai_avem_de_platit

# Calculează restul de bani ce trebuie returnat clientului, dacă a plătit mai mult decât suma totală
rest_bani = plata_client - suma_de_plata
# Afișează restul de bani ce trebuie returnat
print(f"Restul de plata este : {rest_bani}")
