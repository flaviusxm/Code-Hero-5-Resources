# Verifică dacă un număr este mai mare decât celălalt.
# Dacă da, afișează diferența dintre numere.
# Altfel, dacă numărul este mai mic, afișează suma numerelor.
# În caz contrar, afișează mesajul „numerele sunt egale”.
numarul1 = int(input("Introduceti numarul1: "))
numarul2 = int(input("Introduceti numarul2: "))

if numarul1 > numarul2:
    print (numarul1 - numarul2)
elif numarul1 < numarul2:
    print (numarul1 + numarul2)
else:
    print("Numerele introduse sunt egale")