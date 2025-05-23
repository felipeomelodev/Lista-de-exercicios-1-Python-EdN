def calculadora():
    
    print("\n" + "="*40)
    print("CALCULADORA BÁSICA".center(40))
    print("="*40)
    print("Operações disponíveis: +, -, *, /")
    print("="*40)
    
    while True:
        try:
            
            while True:
                try:
                    num1 = float(input("Digite o primeiro número: "))
                    break
                except ValueError:
                    print("ERRO: Digite um número válido.")
            
            while True:
                try:
                    num2 = float(input("Digite o segundo número: "))
                    break
                except ValueError:
                    print("ERRO: Digite um número válido.")
            
            while True:
                operacao = input("Digite a operação (+, -, *, /): ")
                if operacao in ('+', '-', '*', '/'):
                    break
                else:
                    print("ERRO: Operação inválida. Use +, -, * ou /")
            
            if operacao == '+':
                resultado = num1 + num2
            elif operacao == '-':
                resultado = num1 - num2
            elif operacao == '*':
                resultado = num1 * num2
            elif operacao == '/':
                try:
                    resultado = num1 / num2
                except ZeroDivisionError:
                    print("ERRO: Divisão por zero não é permitida.")
                    continue 
            
            print(f"Resultado: {num1} {operacao} {num2} = {resultado}")
            print("="*40)
            break 
            
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")
            continue

if __name__ == "__main__":
    calculadora()