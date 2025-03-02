def joc_general():
    DEX = {
        "Care este capitala Bulgariei?": "Sofia",
        "Ce fel de mancare este mai buna?": "Bio",
        "Care este cea mai mare soparla din lume?": "Dragonul Komodo",
        "Cine a castigat primul razboi mondial?": "Antanta",
    }
    scor = 0

    for intrebare in DEX:
        print(intrebare)
        raspuns_user = input("Raspunsul tau: ")
        if raspuns_user.strip().lower() == DEX[intrebare].lower():
            print("Corect!")
            scor += 1
        else:
            print(f"Gresit! Raspunsul corect este {DEX[intrebare]}.")
    
    print(f"Ai obtinut {scor}/{len(DEX)} puncte.")

joc_general()
