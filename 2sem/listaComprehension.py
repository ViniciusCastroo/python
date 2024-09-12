lista = [] #lista normal
for i in range(10):
    lista.append(1)
print(lista)

lista = [i for i in range(10)]#lista comprehension
print(lista)

lista1 = [i for i in range(10) if i % 2 == 0] #lista comprehension com cndicional
print(lista1)

lista3 = [i for i in range (100) if i % 3 == 0]
print(lista3)

lista4 = [i * i for i in range (20) ]
print(lista4)

linha = int(input("Digite quantas linhas: "))
coluna = int(input("Digite quantas colunas: "))

lista5 = [int(input(":")) for i in range(coluna) for i in range(linha)]

print(lista5)

lista6 = lambda c, l: [int(input(":")) for i in range(c) for i in range(l)]
print(lista6(1, 2))