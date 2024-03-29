#kreiranje matrice 
A=[[2,3],[4,2]]
print(A[1])
print(A[-1][-1])

#nula matrcia za zadate dimenzije od strane korisnika 
dimenzije=int(input("unesite dimenziju 0 matrcie: "))
matrica=[]
for i in range(dimenzije):
    vrsta=[]
    for j in range(dimenzije):
        vrsta.append(0)
    matrica.append(vrsta)
print(matrica)

#menjamo elemente na dijagonali svi moraju da budu 1
for i in range(dimenzije):
    for j in range(dimenzije):
        if i==j:
            matrica[i][j]=1
print(matrica)

#stamapti sve elemente matrcie , redom vrsta--> kolona
for i in range(dimenzije):
    for j in range(dimenzije):
        print(matrica[i][j])

#da seberemo sve elemente matrice
suma=0
for i in range(dimenzije):
    for j in range(dimenzije):
        suma+=matrica[i][j]
print(suma)

#sabirati sve elemnete sa glavne dijagonale matrice 
suma=0
for i in range(dimenzije):
    for j in range(dimenzije):
        if i==j:
            suma+=matrica[i][j]
print(suma)