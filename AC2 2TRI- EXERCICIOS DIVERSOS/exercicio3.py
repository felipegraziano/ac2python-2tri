nomes= set()

duplicado= False

nome= ""

while nome!= "fim":

    nome= input("Digite um nome (ou fim): ")

    if nome!= "fim":

        if nome in nomes:
            duplicado= True

        nomes.add(nome)

print(f"\nQuantidade de pessoas diferentes: {len(nomes)}")

print("\nNOMES CADASTRADOS")

for nome in nomes:
    print(nome)

if duplicado:
    print("\nHouve tentativa de cadastro duplicado.")
else:
    print("\nNão houve tentativa de cadastro duplicado.")