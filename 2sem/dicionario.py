'''
dic = {
    "nome": 'pedro', 
    "idade": 18,
    "estado": "sp"
}
print(dic["nome"])

if "cidade" in dic:
    print(dic["cidade"])
else:
    print("Cidade nao existente no dicionario")
print("cidade" in dic)
'''
totalCp = 3
Pedro = {}
while totalCp != 0:
    cp = input("Qual cp é: ")
    notas = float(input("digite sua nota: "))
    Pedro[cp] = notas
    totalCp -= 1
print(Pedro)
