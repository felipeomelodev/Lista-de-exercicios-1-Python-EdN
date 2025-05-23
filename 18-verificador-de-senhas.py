def verificar_senha():

    print("\n" + "="*40)
    print("VERIFICADOR DE SENHA FORTE".center(40))
    print("="*40)
    print("Critérios para senha forte:")
    print("- Mínimo 8 caracteres.")
    print("- Pelo menos 1 número.")
    print("Digite 'sair' para encerrar.")
    print("="*40)
    
    while True:
        senha = input("\nDigite uma senha: ")
        
        if senha.lower() == 'sair':
            print("Programa encerrado.")
            return
        
        if len(senha) < 8:
            print("ERRO: A senha deve ter pelo menos 8 caracteres.")
            continue
        
        tem_numero = any(caractere.isdigit() for caractere in senha)
        if not tem_numero:
            print("ERRO: A senha deve conter pelo menos 1 número.")
            continue
        
        print("\n" + "="*40)
        print("✔ Senha forte cadastrada com sucesso!")
        print("="*40)
        break

if __name__ == "__main__":
    verificar_senha()