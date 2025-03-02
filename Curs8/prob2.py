# 5 nume 
# 5 valori 

def lipeste_liste(nume,varste):
    result={}
    perechi=zip(nume,varste)
    for num , varst in perechi:
        if (len(num)>4 and varst%2==1):
            result[num]=varst
    print(result)

nume=["Mihai","Andrei","Matei","Teodor","Alex"]
varste=[20,23,19,22,19]

lipeste_liste(nume,varste)