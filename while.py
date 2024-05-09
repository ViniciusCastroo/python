'''
a = 0

while(a <=10):
    print(a)
    a += 1

/////////////////////////////////////////////////////////////////////////////////////////////////
a = 10
while(0 <= a):
    print(a)
    a-= 1
    
print("Fogo")

//////////////////////////////////////////////////////////////////////////////////////////////////////
numero = int(input("Digite um valor: "))
a = 1

while (a <= numero):
    if a % 2 != 0:
        print(a)
    a += 1 

///////////////////////////////////////////////////////////////////////////////////////////////////
numero = int(input("Digite um valor: "))
a = 1

while (a <= numero):
    if a % 2 == 0:
        print(a)
    a += 1 

//////////////////////////////////////////////////////////////////////////////////////////////
inicio = int(input("digite o inicio dos numero: "))
fim = int(input("digite o fim dos numero: "))

soma = 0
contador = inicio

while(contador <= fim):
    if contador % 2 == 0:
        print(contador)
        soma += contador
    contador+=1
print(soma)
/////////////////////////////////////////////////////////////////////////////////////////////////

total = int(input("Digite total de notas: "))

media = 0
totalmedia = total

while(1 <= total):
    nota = int(input("Digite a notas: "))
    total -= 1
    media += nota
totalmedia = media/totalmedia
print(totalmedia)

///////////////////////////////////////////////////////////////////////////////
a = 0
n = int(input("Digite um numero até 10: "))

while(a <=10):
    print(a)
    a += 1
    if a == n:
        break
//////////////////////////////////////////////////////////////////////////////////////

while (True):
    n = int(input("Digite um numero: "))
    if n == 0:
        print("Fim do programa")
        break

//////////////////////////////////////////////////////////////////////////////////////////////////
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


////////////////////////////////////////////////////////////////////////////////////////////////
print("Codigo: 1 Preço 0,50")
print("Codigo: 2 Preço 1,00")
print("Codigo: 3 Preço 4,00")
print("Codigo: 5 Preço 7,00")
print("Codigo: 9 Preço 8,00")

codigo1 = 0
codigo2 = 0
codigo3 = 0
codigo5 = 0
codigo9 = 0

totaln = 0


while(True):
    n = int(input("Digite um codigo: "))
    if n == 1:
        codigo1 += 0.50 
    elif n == 2:
        codigo2 += 1.00
    elif n == 3:
        codigo3 += 4.00
    elif n == 5:
        codigo5 += 7.00
    elif n == 9:
        codigo9 += 8.00
    elif n == 0:
        soma = (codigo1 + codigo2 + codigo3 + codigo5 + codigo9)
        print(f"O valor total da compra foi de: {soma}")
        break
    else:
        print("Digite uma das opções")
        continue

'''