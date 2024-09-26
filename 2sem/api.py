import requests
""" '''
cep = input("Digite seu cep: ")
url = f"https://viacep.com.br/ws/{cep}/json/"

r = requests.get(url)
info = r.json()

print(f"Rua: {info['logradouro']}, Bairro: {info['bairro']}, Cidade: {info['localidade']} e estado: {info['estado']}.")
'''

url = "https://pokeapi.co/api/v2/pokemon/eevee"

r = requests.get(url)
info = r.json()



#print(f"{info['id']}, {info['types']}")


print(info['types'][0]['type']['name'])
 """

""" def poke(pokemon):
    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon}'
    r = requests.get(url)
    r = r.json()
    
    id = r['id']
    tipo = r['types'][0]['type']['name']
    
    print(f'O id do {pokemon} é {id}')
    print(f'{pokemon} é do tipo {tipo}')
    
    return [id, tipo]

pokemon = 'pikachu'
var = poke(pokemon)

print(f'O id do {pokemon} é {var[0]}')
print(f'{pokemon} é do tipo {var[1]}') """

#Exercicio


""" supermercado = {
'amaciante':4.99,
' arroz':10.90,
'biscoito':1.69,
'cafe':6.98,
'chocolate':3.79,
'farinha':2.99
}
lista = ['biscoito', 'chocolate', 'farinha']
valor = 0

for i in lista:
    if i in supermercado:
        valor += supermercado[i]
    else:
        print(f'n temos o produto: {i}')    


print(valor) """

""" listas = [1,2,3,4]
tupla = (1,2,3,4)
print(listas, type(listas))
print(tupla, type(tupla))
tupla[0] """

""" tupla = (1,2,3)
tupla = list(tupla)
rem = 3
for i,j in enumerate(tupla):
    if j == rem:
        tupla.pop(i)
print(tuple(tupla)) """


