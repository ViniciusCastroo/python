dados = [
    {"dia":12, "mes":2, "ano":2019, "tempo": 25},
    {"dia":19, "mes":6, "ano":2019, "tempo": 27},
    {"dia":27, "mes":12, "ano":2019, "tempo": 22},
    {"dia":6, "mes":2, "ano":2019, "tempo": 30.6}
]

for i in dados:
    print(f"{i["dia"]}/{i["mes"]}/{i["ano"]}/{i["tempo"]}")