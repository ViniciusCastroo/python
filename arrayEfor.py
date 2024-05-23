# lista = [10, 20, 30]

# print(lista[-1::-1])

# a  = []
# print(a)
# b = list("Pedro")
# print(b)



# texto = "u sapo nao lava o pe"
# vogal_substituta = "u"
# vogais = ["a", "e", "i", "o", "u"]

# for vogal in vogais:
#     texto = texto.replace(vogal, vogal_substituta)

# print(texto)


# texto = "o sapo nao lava o pe"
# vogal = "i"
# a = list(texto)
# i = 0
# textoFinal = ""
# while i < len(a):
#     if a[i] == "a" or a[i] == "e" or a[i] == "i" or a[i] == "o" or a[i] == "u":
#         a[i] = vogal
#     textoFinal += a[i]    
#     i += 1

# print(textoFinal)

# escrever = int(input("Quantas notas deseja inserir: "))
# notas = []

# while escrever >= 1:
#     digite = float(input("Digite a nota: "))
#     notas.append(digite)
#     escrever -= 1
# print(notas)

# a = [1, 2, 3, 4]
# b = a
# print(a)
# print(b)

fila = [] 


adicionar_primeira_pessoa = input("Deseja adicionar uma pessoa à fila? (s/n): ")

if adicionar_primeira_pessoa.lower() == 's':

    primeira_pessoa = input("Nome da primeira pessoa a entrar na fila: ")
    fila.append(primeira_pessoa)


while True:
 
    if len(fila) > 0:
  
        pessoa_atual = fila.pop(0)
        print(f"Atendendo a pessoa {pessoa_atual}")
    else:
        print("Fila vazia. Nenhuma pessoa para atender.")
        break  


    adicionar = input("Deseja adicionar mais pessoas à fila? (s/n): ")
    
    if adicionar.lower() == 's':
      
        nova_pessoa = input("Nome da próxima pessoa a entrar na fila: ")
        fila.append(nova_pessoa)
    else:
        print("Fila encerrada. Todas as pessoas foram atendidas.")
        break 
