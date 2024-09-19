frutas = {
    "Morango":"Vermelho",
    "Uva Verde":"Verde",
    "Banana":"Amarelo"
}
'''
print(frutas) imprimindo chave e valor

print(frutas["Morango"]) Imprimindo valor da fruta

frutas["Mamao"] = "Laranja" adicionando uma nova chave e valor no meu dicionario
print(frutas["Mamao"])

frutas["Mamao"] = "Roxo"
print(frutas["Mamao"])

frutas.pop("Morango") removendo uma chave do meu dicionario
print(frutas.keys())

for i in frutas.keys(): mostrando apenas as chaves do meu dicionario
    print(i)

for i in frutas.values(): mostrando apenas meus valores no meu dicionario
    print(i)

for i in frutas.items(): mostra um tupla com chave e valor
    print(i)


if "Morango" in frutas: verificando se existe essa chave no meu dicionario
    print(frutas["Morango"])
else:
    print("Morango nao exite no dicionario")


'''
frutasB = {
    "Pessego":"Amarelo",
    "Tomate":"Vermelho"
}

frutas.update(frutasB) #Juntando outro dicionario
'''
print(frutas)

print(len(frutas)) Mostrando todos os valores do dicionario
'''

print(frutas)
frutasC = frutas.copy

frutas["Pessego"] = "Roxo"
print(frutas)
print(frutasC)