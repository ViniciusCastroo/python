#questao 1
def f(x):
    if x < -2:
        return x**2 + 3 * x - 4
    elif x < 0:
        return 2 * x + 5
    elif  x < 4:
        return x**(1/2)
    elif x < 6:
        return x **3 - 3 *x ** 2- 10 * x
    elif x < 8:
        return 3 * x ** 2 - 4 * x- 20
    else:
        return 10

#questao 2
def leituraMatriz(x, y):
    matriz = []
    for j in range(l):
        linha = []
        for i in range(c):
            linha.append(input(""))
        matriz.append(linha)
    return matriz

#questao 3
def tamanho(matriz):
    linhas = len(matriz)
    colunas = len(matriz[0])
    return [linhas, colunas]


#questao 4
def sub(a, b):
    if len(a) == len(b) and len(a[0]) == len(b[0]):
        matriz = []
        for j in range(len(a)):
            linha = []
            for i in range(len(a[0])):
                linha.append(a[j][i] - b [j][i])
            matriz.append(linha)
        return matriz


#questao 5
def esparsa(matriz):
    elem = len(matriz) * len(matriz[0])
    qtde = 0

    for j in range(len(matriz)):
        for i in range(len(matriz[0])):
            if matriz[j][i] == 0:
                qtde += 1
        if qtde > elem / 2:
            return True
        return False