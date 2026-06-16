meses= (
    "Janeiro", "Fevereiro", "Março", "Abril",
    "Maio", "Junho", "Julho", "Agosto",
    "Setembro", "Outubro", "Novembro", "Dezembro"
)

vendas= []

for i in range(len(meses)):
    venda= float(input(f"Digite a venda de {meses[i]}: "))
    vendas.append(venda)

vendas= tuple(vendas)

maiorVenda= max(vendas)
menorVenda= min(vendas)

print(f"\nMaior venda: {maiorVenda}")
print(f"Menor venda: {menorVenda}")

print(f"Mês da maior venda: {meses[vendas.index(maiorVenda)]}")
print(f"Mês da menor venda: {meses[vendas.index(menorVenda)]}")

soma= 0

for venda in vendas:
    soma= soma + venda

media= soma / len(vendas)

print(f"Média anual: {media:.2f}")

print("\nMESES ACIMA DA MÉDIA")

for i in range(len(vendas)):
    if vendas[i]> media:
        print(meses[i])