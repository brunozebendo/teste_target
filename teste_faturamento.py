import json

with open('dados.json', "r") as dados:
    data = json.load(dados)

if data['valor'] > 0:
    media = sum(data['valor']) / len(data)

dias_acima_media = 0
for valor in data:
    if valor > media:
        dias_acima_media += 1

print(f"Menor valor de faturamento diário: R${min(faturamento):.2f}")
print(f"Maior valor de faturamento diário: R${max(faturamento):.2f}")
print(f"Número de dias em que o valor de faturamento diário foi superior à média mensal: {dias_acima_media}")