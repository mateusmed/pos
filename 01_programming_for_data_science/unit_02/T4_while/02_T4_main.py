def while_simple_example():
    lista_idades = []
    lista_pessoas = []

    nome = input("Digite um nome: ")
    while (nome.lower() != 'fim'):
        idade = int(input("Digite uma idade: "))
        lista_idades.append(idade)
        lista_pessoas.append(nome)
        nome = input("Digite um nome: ")

    print("\n\nNomes digitados\n===============")
    print(lista_pessoas)
    print("\nIdades\n===============")
    print(lista_idades)