cpfs= set()
duplicados= []

for i in range(5):

    cpf= input(f"Digite o CPF {i+1}: ")

    if cpf in cpfs:
        duplicados.append(cpf)
        print("CPF já cadastrado.")
    else:
        cpfs.add(cpf)

print(f"\nQuantidade de CPFs válidos cadastrados: {len(cpfs)}")

print("\nCPFs duplicados:")

if len(duplicados)== 0:
    print("Não houve tentativas.")
else:
    for cpf in duplicados:
        print(cpf)