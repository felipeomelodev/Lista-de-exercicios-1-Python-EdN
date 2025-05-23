def classificar_idade():

    try:
        idade = int(input("Digite a sua idade: "))

        if idade < 0:
            print("ERRO: Idade não pode ser negativa.")
        elif idade <= 12:
            print("CLASSIFICAÇÃO: Criança (0 -> 12 anos)")
        elif idade <= 17:
            print("CLASSIFICAÇÃO: Adolescente (13 -> 17 anos)")
        elif idade < 59:
            print("CLASSIFICAÇÃO: Adulto(a) (18 -> 59 anos)")
        else:
            print("CLASSIFICAÇÃO: Idoso(a) (60 anos ou mais)")


    except ValueError:
        print("ERRO: Digite um número inteiro válido.")


if __name__ == "__main__":
    classificar_idade()