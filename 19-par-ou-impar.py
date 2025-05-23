def verificar_par_impar():

    print("\n" + "="*40)
    print("VERIFICADOR PAR/ÍMPAR".center(40))
    print("="*40)
    print("Digite números inteiros ou 'fim' para encerrar.")
    print("="*40)
    
    pares = 0
    impares = 0
    
    while True:
        entrada = input("Digite um número: ")
        
        if entrada.lower() == 'fim':
            break
        
        try:
            numero = int(entrada)
            if numero % 2 == 0:
                print(f"O número {numero} é PAR.")
                pares += 1
            else:
                print(f"O número {numero} é ÍMPAR.")
                impares += 1
        except ValueError:
            print("ERRO: Digite um número inteiro válido ou 'fim'.")
    
    print("\n" + "="*40)
    print("RESULTADO FINAL".center(40))
    print("="*40)
    print(f"Total de números pares: {pares}")
    print(f"Total de números ímpares: {impares}")
    print(f"Total de números digitados: {pares + impares}")
    print("="*40)

if __name__ == "__main__":
    verificar_par_impar()