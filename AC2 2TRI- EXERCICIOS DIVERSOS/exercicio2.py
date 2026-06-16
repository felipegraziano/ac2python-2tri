assentos= []

for i in range(20):
    status= input(f"Digite o status do assento {i+1} (LIVRE/OCUPADO): ")
    assentos.append(status)

assentos= tuple(assentos)

print("\nASSENTOS")

for i in range(len(assentos)):
    print(f"Assento {i+1}: {assentos[i]}")

print(f"\nQuantidade de assentos livres: {assentos.count('LIVRE')}")
print(f"Quantidade de assentos ocupados: {assentos.count('OCUPADO')}")

consulta= int(input("\nDigite o número do assento que deseja consultar: "))

if consulta>= 1 and consulta<= 20:
    print(f"Status: {assentos[consulta-1]}")
else:
    print("Assento inválido.")