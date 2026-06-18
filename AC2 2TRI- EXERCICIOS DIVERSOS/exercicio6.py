veiculo= {
    "marca": input("Digite a marca: "),
    "modelo": input("Digite o modelo: "),
    "ano": int(input("Digite o ano: ")),
    "cor": input("Digite a cor: "),
    "valor": float(input("Digite o valor: "))
}


print("\nDados do veículo")

for chave, valor in veiculo.items():
    print(f"{chave}: {valor}")


if veiculo["ano"]< 2010:
    print("\nVeículo antigo.")
else:
    print("\nVeículo moderno.")


valorFinal= veiculo["valor"]

if valorFinal> 100000:
    valorFinal= valorFinal * 0.90

print(f"Valor final: {valorFinal:.2f} reais")