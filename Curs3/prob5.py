#Cere utilizatorului numere până când se introduce 6.
#Calculați media numerelor introduse.
numar = 0
suma = 0
index = 0
while numar != 6 :
    numar = int(input("Introduceti orice numar diferit de 6: "))
    suma = suma + numar
    index = index + 1

print(suma/index)
#sau 
#print(suma//index) numar int