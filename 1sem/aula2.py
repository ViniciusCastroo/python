'''
salario = float(input("Digite seu salario"))
reducao = (salario * 5)/100
salariofinal = (salario - reducao)
print(salariofinal)

//------------------------------------------------------------------------------------------------------------------
a = 10
b = 20
c = a
a = b
b = c

tipo = type(a)

print(tipo)
print(b)

//------------------------------------------------------------------------------------------------------------------


tempo = 87426
hora = tempo / 60 / 60
minuto = (hora * 60) - 24 * 60
segundos = tempo % 60

print(f"Os segundos foram {segundos}\nOs minutos foram {minuto:.0f}\nHoras foram para {hora:.0f}")

//------------------------------------------------------------------------------------------------------------------


a = 5
b = 6

print(a > b)

//------------------------------------------------------------------------------------------------------------------



nt1 = float(input("Digite sua nota"))
nt2 = float(input("Digite sua nota"))
nt3 = float(input("Digite sua nota"))

media = (nt1 + nt2 +nt3)/3

media1 = media >= 6

if media > 6:
    print(media1)
else:
    print(media1)

//------------------------------------------------------------------------------------------------------------------
    
salario = float(input("Digite seu salario: "))

salario1 = salario >= 1500

if salario >= 1500:
    print(f"Você pode contartar o emprestimo, {salario1}")
else:
    print(f"Voce não pode contratar o emprestimo, {salario1}")

//------------------------------------------------------------------------------------------------------------------

print(9/3 == 3*3 and 2*3-1>=8)

//------------------------------------------------------------------------------------------------------------------

idade = int(input("Digite sua idade: "))
salario = float(input("Digite seu salario: "))

maioridade = (salario >= 1500 and idade >= 18)

if salario >= 1500 and idade >= 18:
    print(f"Você está liberado para o empréstimo {maioridade}")
else:
    print(f"Você não está liberado para o empréstimo {maioridade}")

//------------------------------------------------------------------------------------------------------------------

'''
