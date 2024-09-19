dados = {}

total = int(input("Digite quantos dados quer inserir: "))

while total != 0:
    nome = input("Digite o nome: ")
    info = []
    idade = int(input("Digite a idade: "))
    info.append(idade)

    sexo = input("Digite o sexo da pessoa: ")
    info.append(sexo)
    
    dados[nome] = info
    total -= 1


for i in dados.items():
    print(i)

