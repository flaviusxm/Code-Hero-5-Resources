def joc_general():
    DEX = {
        "Care este capitala Romaniei?": "Bucuresti",
        "Cate zile are o saptamana?": "7",
        "Care este cel mai mare mamifer din lume?": "Balena albastra",
        "Cine a pictat Mona Lisa?": "Leonardo da Vinci",
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
