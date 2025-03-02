def varsta_prieteni(dictionar):
    for parametru, element in dictionar.items():
        if element %2 ==0:
            print(parametru + " : " + str(element))

dictionar={
    "Mihai":20,
    "Andrei":23,
    "Matei":19
}

varsta_prieteni(dictionar)