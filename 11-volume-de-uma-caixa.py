def calcular_volume_caixa(comprimento, largura, altura):

    volume = comprimento * largura * altura
    return volume

def main():

    comprimento = float(input("Digite o comprimento da caixa em metros: "))
    largura = float(input("Digite a largura da caixa em metros: "))
    altura = float(input("Digite a altura da caixa em metros: "))

    volume = calcular_volume_caixa(comprimento, largura, altura)

    print(f"O volume da caixa é: {volume} m³")

if __name__ == "__main__":
    main()