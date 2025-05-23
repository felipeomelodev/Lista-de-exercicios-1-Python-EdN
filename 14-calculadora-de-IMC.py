def calcular_imc():
    
    print("\n" + "="*40)
    print("CALCULADORA DE IMC".center(40))
    print("="*40)

    try:
        peso = float(input("Digite seu peso em kg: "))
        altura = float(input("Digite a sua altura em metros: "))

        if peso <=0 or altura <= 0:
            print("ERRO: Peso e altura devem ser valores positivos.")
            return
        
        imc = peso / (altura ** 2)

        if imc < 18.5:
            classificacao = "Abaixo do peso"
        elif 18.5 <= imc < 25:
            classificacao = "Peso adequado"
        elif 25 <= imc < 30:
            classificacao = "Sobrepeso"
        elif 30 <= imc < 35:
            classificacao = "Obesidade Grau I"
        elif 35 <= imc < 40:
            classificacao = "Obesidade Grau II"
        else:
            classificacao = "Obesidade Grau III (Mórbida)"

        print("\n" + "=" * 40)
        print(f"IMC: {imc:.1f}")
        print(f"CLASSIFICAÇÃO: {classificacao}")
        print("-"*40)

    except ValueError:
        print("ERRO: Digite valores numéricos válidos para peso e altura.")

if __name__ == "__main__":
    calcular_imc()