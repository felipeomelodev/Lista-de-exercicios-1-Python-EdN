def verificar_ano_bissexto():

    print("\n" + "=" *40)
    print("VERIFICADOR DE ANO BISSEXTO".center(40))
    print("="*40)

    try:
        ano = int(input("Digite um ano (ex: 2009): "))

        if ano <= 0:
            print("ERRO: O ano deve ser um valor positivo.")
            return
        
        if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
            print(f"\nO ano {ano} é bissexto.")

        else:            
            print(f"\nO ano {ano} não é bissexto." )

        print("\n" + "-" *40)
        print("REGRAS:")
        print("- Divisível por 4.")
        print("- Exceto se divisível por 100.")
        print("- A menos que seja divisível por 400.")
        print("="*40)

    except ValueError:
        print("ERRO: Digite um número inteiro válido.")

if __name__ == "__main__":
    verificar_ano_bissexto()