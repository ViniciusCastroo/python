frase = "Pedro"
contador = {}
for i in frase:
    if i in contador:
        contador[i] += 1
    else:
        contador[i] = 1


