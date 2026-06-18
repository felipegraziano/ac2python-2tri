produto= {
    "nome": input("Nome do produto: "),
    "preco": float(input("Preço do produto: ")),
    "quantidade": int(input("Quantidade do produto: "))
}

opcao= 0

while opcao!= 5:

    print("\nMenu:")
    print("1 - Exibir produto")
    print("2 - Alterar preço")
    print("3 - Alterar quantidade")
    print("4 - Calcular valor total em estoque")
    print("5 - Encerrar sistema")

    opcao= int(input("Escolha uma opção: "))

    if opcao== 1:

        print("\nDados do produto")

        for chave, valor in produto.items():
            print(f"{chave}: {valor}")


    elif opcao== 2:

        produto["preco"]= float(input("Digite o novo preço: "))
        print("Preço alterado.")


    elif opcao== 3:

        produto["quantidade"]= int(input("Digite a nova quantidade: "))
        print("Quantidade alterada.")


    elif opcao== 4:

        total= produto["preco"] * produto["quantidade"]
        print(f"Valor total em estoque: {total:.2f} reais")


    elif opcao== 5:
        
        print("Sistema encerrado.")

    else:

        print("Opção inválida. Digite um número de 1 a 5.")