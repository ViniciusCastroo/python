'''
def quadrado(x):
    print("executando a função")
    resultado = x * x
    return resultado

a = 2
print(quadrado(2))
'''
'''
def dobro(i):
    return i * 2

b = int(input("Informe um numero: "))
print(dobro(b))
'''
'''
def soma(x, y):
    return x + y
a = int(input("Digite um valor: "))
b = int(input("Digite outro valor: "))

print(soma(a, b))
'''
'''
def soma(x, y, z):
    return x + y + z
a = int(input("Digite um valor: "))
b = int(input("Digite outro valor: "))
c = int(input("Digite outro valor: "))

print(soma(a, b, c))
'''
'''
def maior(a, b):
    if a > b:
        return a
    else:
        return b
i = int(input("Digite um valor: "))
j = int(input("Digite outro valor: "))

print(f"O numero maior é: {maior(i, j)}")
'''
def main():
    print("digite uma das opções: +, -, *, /")
    opc = input("")
    a = float(input("Digite um valor: "))
    b = float(input("Digite outro valor: "))

    if opc == "+":
        resultado = soma(a, b)
    elif opc == "-":
        resultado = sub(a, b)
    elif opc == "/":
        resultado = div(a, b)
    elif( opc == "*"):
        resultado = div(a, b)
    else:
        resultado = "opcao invalida"
    print(resultado)

def soma (x, y):
    return x + y

def sub(x, y):
    return x - y

def div(x, y):
    return x/y

def mult(x, y):
    return x * y

main()

