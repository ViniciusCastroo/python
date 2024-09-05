def transposta(a):
    matriz = []
    for j in range(len(a[0])):
        linha = []
        for i in range(len(a)):
            linha.append(a[i][j])
        matriz.append(linha)
    return matriz

m = [
        [1, 2, 3],
        [4, 5, 6]
     ]

print(transposta(m))

m = [[1, 2 ,3], 
     [4, 5, 6],
     [7, 8, 9]]
traco = 0
if len(m) == len(m[0]):
    for i in range(m[0]):
        traco += m[i][j]
    print(traco)
else:
    print("matriz nao quadrada")