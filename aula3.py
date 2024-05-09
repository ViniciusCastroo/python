'''
materia1 = float(input("Digite a nota da primeira materia: "))
materia2 = float(input("Digite a nota da segunda materia: "))
materia3 = float(input("Digite a nota da terceira materia: "))
podersupremo = 1


media = (materia1 + materia2 + materia3)/3


if (media >= 7):
    print(f"O aluno foi aprovado, {media:.2f}")
else:
    print(f"O aluno foi reprovado, {media:.2f}")


resultado = (materia1 >= 7 and materia2 >=7 and materia3 >= 7) or podersupremo == 1
print(resultado)

//--------------------------------------------------------------------------------------------------



a = "bom dia!"

print(a[:7])

//--------------------------------------------------------------------------------------------------
a = "Bom"
b = " Dia!"

print(a + b)

//--------------------------------------------------------------------------------------------------

nome = input("Digite seu nome: ")

print(nome[0])
print(len(nome))

//--------------------------------------------------------------------------------------------------

palavra = "maximo"

print(palavra[::-1])
print(palavra[::2])
print(palavra[1::2])

//--------------------------------------------------------------------------------------------------

palavra1 = "Bom"
palavra2 = "Dia"

print(palavra1[1:] + palavra2[1:])

//--------------------------------------------------------------------------------------------------

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
precoCantina = float(input("Digite o preco do lanche da cantina: "))

print(f"Meu nome é {nome}, tenho {idade} anos e o preco do lanche da cantina é de: {precoCantina:.2f}")

//--------------------------------------------------------------------------------------------------

n1 = int(input("Digite um numero: "))
n2 = int(input("Digite outro numero"))

soma = (n1 + n2)

print(f"A soma dos numeros é: {soma}")

'''

dia = int(input("Digite a quantidade de dias: "))
horas = int(input("Digite a quantidade de horas: "))
segundos = int(input("Digite quantos segundos: "))

horas1 = (dia *1 24)
print(horas1)