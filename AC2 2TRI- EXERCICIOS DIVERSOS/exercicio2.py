assentos= []

for i in range(20):
    status= input(f"Digite o status do assento {i+1} ('L' para livre/ 'O' para ocupado): ")
    assentos.append(status)

assentos= tuple(assentos)

print("\nAssentos")

for i in range(len(assentos)):
    print(f"Assento {i+1}: {assentos[i]}")

print(f"\nQuantidade de assentos livres: {assentos.count('L')}")
print(f"Quantidade de assentos ocupados: {assentos.count('O')}")


consulta=0

while(consulta!= -1):

    consulta= int(input("\nDigite o número do assento que deseja consultar (pra sair, digite -1): "))

    if(consulta==-1):
        print("Programa encerrado.")
        break

    if consulta>= 1 and consulta<= 20:
        status= assentos[consulta-1]

        if(status=="L"):
            statusTexto= "Livre"

        elif(status=="O"):
            statusTexto= "Ocupado"

        print(f"Status: {statusTexto}")
    else:
        print("Assento inválido.")
