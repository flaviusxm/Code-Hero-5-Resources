an = int(input("Introduceți un an: "))

# Verificăm dacă anul este bisect folosind un singur if
if (an % 4 == 0 and (an % 100 != 0 or an % 400 == 0)):
    print(f"{an} este an bisect.")
else:
    print(f"{an} nu este an bisect.")
