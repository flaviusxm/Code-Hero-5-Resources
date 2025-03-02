prieteni_varste = {
    "Alice": 25,
    "Bob": 30,
    "Charlie": 22,
    "Diana": 28
}

for cheie, valoare in prieteni_varste.items():
    print(cheie + ": " + str(valoare))


#######################################
def afiseaza_dictionar(dictionar):
    nume = ["Alice", "Bob", "Charlie", "Diana"]
    varste = [25, 30, 22, 28]
    perechi = zip(nume, varste)
    
    for k, v in perechi:
        dictionar[k] = v
    
    print(dictionar)

# Dicționar inițial
dictionar = {}
afiseaza_dictionar(dictionar)

#####################################

fruits = ["apple", "banana", "grapes"]
fruits.insert(1, "orange")
print(fruits)

###########################################


sentence = "the cat sat on the mat"
new = sentence.split()
print(new)
