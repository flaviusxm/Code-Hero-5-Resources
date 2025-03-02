text=input("Introduceti un text de la tastatura : ")

print(text)

vocale="aeiouAEIOU"

i=0
contor_vocale=0

while i<len(text):
    if text[i] in vocale:
        contor_vocale+=1
    i+=1
    
print(f"Numarul de vocale din {text} este : {contor_vocale}")