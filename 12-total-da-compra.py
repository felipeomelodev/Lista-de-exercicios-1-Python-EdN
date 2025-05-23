def calcular_total_compra():

    nome_do_produto = input("Digite o nome do produto: ")
    preco_unitario = float(input("Digite o preço unitário do produto R$: "))
    quantidade = int(input("Digite a quantidade comprada: "))

    total = preco_unitario * quantidade

    print("\n" + "=" * 40)
    print("RECIBO DE COMPRA".center(40))
    print("=" * 40)
    print(f"Produto: {nome_do_produto.upper()}")
    print(f"Preço unitário: R$ {preco_unitario:.2f}")
    print(f"Quantidade: {quantidade}")
    print("-" * 40)
    print(f"TOTAL: R$ {total:.2f}".rjust(40))
    print("=" * 40)

if __name__ == "__main__":
    calcular_total_compra()