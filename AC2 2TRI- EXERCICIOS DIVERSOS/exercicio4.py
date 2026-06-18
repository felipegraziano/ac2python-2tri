hashtags= set()

hashtag= ""

while hashtag!= "sair":

    hashtag= input("Digite uma hashtag (ou sair): ")

    if hashtag!= "sair":
        hashtags.add(hashtag)

print(f"\nQuantidade total de hashtags únicas: {len(hashtags)}")

print("\nLISTA DE HASHTAGS")

for hashtag in hashtags:
    print(hashtag)


pesquisa= ""

while(pesquisa!="sair"):

    pesquisa= input("\nDigite uma hashtag para pesquisar (ou sair): ")

    if(pesquisa=="sair"):
        print("Programa encerrado.")
        break

    if pesquisa in hashtags:
        print("Hashtag encontrada.")
    else:
        print("Hashtag não encontrada.")