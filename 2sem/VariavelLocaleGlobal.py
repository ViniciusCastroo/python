valor = 10 # "valor" é uma variavel global(pode ser acessada em qualquer lugar)

def soma(a, b):
    valor = 4 #criou uma nova variavel chamada valor != da variavel valor global
    c = a + b + valor # "c" é uma variavel local(so pode ser usada nesta funcao)
    return c

print(soma(10, 2))

#Variavel criada na funcao1 nao pode ser usada na funcao2, a nao ser que ela seja uma variavel global
#listas sao alteradas de formas globalmente, caso queira modificar uma lista localmente duplique ela e 
# modifique a lista duplicada, mantendo a lista original intacta


