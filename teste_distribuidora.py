valores = {
    'SP': 67.83643,
    'RJ': 36.67866,
    'MG': 29.22988,
    'ES': 27.16548,
    'Outros': 19.84953
}

total = sum(valores.values())
print(total)

for estado, valor in valores.items():
    percentual = (valor / total) * 100
    print(f'{estado}: {percentual:.2f}%')