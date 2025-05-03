
numeros = []

for i in range(5):
    numero = int(input(f"Digite o número {i + 1}: "))
    numeros.append(numero)

maior = max(numeros)
menor = min(numeros)
soma = sum(numeros)
media = soma / len(numeros)

print(f"Maior número: {maior}")
print(f"Menor número: {menor}")
print(f"Soma total: {soma}")
print(f"Média: {media:.2f}")

