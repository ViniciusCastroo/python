'''
Faça um programa para imprimir de 1 até o número digitado pelo usuário, mostrando
apenas os números pares

numero = int(input("Digite um valor: "))
a = 1

while (a <= numero):
    if a % 2 == 0:
        print(a)
    a += 1 

'''
'''
Faça um programa para imprimir de 1 até o número digitado pelo usuário, mostrando
apenas os números ímpares.

numero = int(input("Digite um valor: "))
a = 1

while (a <= numero):
    if a % 2 != 0:
        print(a)
    a += 1 
'''
'''
Faça um programa para somar todos os pares dentro de um intervalo numérico
passado pelo usuário

inicio = int(input("digite o inicio dos numero: "))
fim = int(input("digite o fim dos numero: "))

soma = 0
contador = inicio

while(contador <= fim):
    if contador % 2 == 0:
        print(contador)
        soma += contador
    contador+=1
print(f"Soma dos numeros pares: {soma}")
'''
'''
Faça um programa para exibir os resultados da tabuada de um número digitado pelo
usuário. Ex.: 2x1 = 2, 2x2 = 4, …

tabuada = (int(input("Digite o valora da tabuada: ")))
a = 1

while(a <= 10):
    print(f"{a} X {b} = {a * tabuada}")
    a += 1
'''


'''
Faça um programa que após a inserção de n números contendo as notas de uma
turma de alunos, retorne a média dessas notas.

total = int(input("Digite total de notas: "))

media = 0
totalmedia = total

while(1 <= total):
    nota = int(input("Digite a notas: "))
    total -= 1
    media += nota
totalmedia = media/totalmedia
print(totalmedia)
'''
'''
Modifique o programa anterior de forma que o usuário também digite o início e o
fim da tabuada, em vez de começar com 1 e terminar com 10.

numero = int(input("Digite o número da tabuada: "))
inicio = int(input("Digite o início da tabuada: "))
fim = int(input("Digite o fim da tabuada: "))
i = inicio

print(f"Tabuada de {numero} de {inicio} até {fim}:")
while i <= fim:
    print(f"{numero} x {i} = {numero * i}")
    i += 1
'''
'''
Escreva um programa que leia números inteiros do teclado. O programa deve ler os
números até que o usuário digite 0 (zero). No final da execução, exiba a quantidade
de números digitados, assim como a soma e a média aritmética.

i = 0
soma = 0
media = 0

while(True):
    n = int(input("Digite um valor: "))
   

    if n == 0:
        break
    i += 1
    soma = soma + n
    media = soma/i
print("Fim programa")
print(f"quantidade de valor digitado {i}")
print(f"A soma dos valores digitados é de: {soma}")
print(f"A media dos numeros é de {media:.2f}")
'''
'''
Faça um programa para contar o número de pares e ímpares dentro de um intervalo
numérico passado pelo usuário

inicio = int(input("digite o inicio dos numero: "))
fim = int(input("digite o fim dos numero: "))

a = inicio
par = 0
impar = 0

while (a <= fim):
    if a % 2 == 0:
        par += 1
    else:
        impar += 1
    a +=1
print(par)
print(impar)
'''
'''
Escreva um programa que exiba uma lista de opções (menu): adição, subtração,
divisão, multiplicação e sair. Imprima a tabuada da operação escolhida. Repita até
que a opção saída seja escolhida.



while True:
    print("Digite uma das opções:(1) - Adição\n(2)- Subtração\n(3) - divisão\n(4)- Multiplicação\n(0)-Sair")
    opcao = int(input())
    num1 = float(input("digite um numero:"))
    num2 = float(input("Digite outro numero: "))
    if opcao == 1:
        soma = num1 +num2
        print(soma)
    elif opcao == 2:
        sub = num1 - num2
        print(sub)
    elif opcao == 3:
        div = num1/num2
        print(div)
    elif opcao == 4
        mult = num1*num2
        print(mult)
    elif opc == 0:
        break
    else:
        print("opção invalida")
        continue


numero = int(input("Digite um numero: "))
a = 1
soma = 0

while(a <= numero):
    soma += a
    a +=1
print(soma)
'''
'''
Fibonacci
'''

a1 = 0
a2 = 1

n = 10
i = 1
n-=2

print(a1)
print(a2)
while i <= n:
    proximoTermo = a1 + a2 
    a1 = a2
    a2 = proximoTermo
    i+= 1
    print(proximoTermo)

