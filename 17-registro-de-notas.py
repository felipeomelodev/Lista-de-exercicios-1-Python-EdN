def registrar_notas():
   
    print("\n" + "="*40)
    print("REGISTRO DE NOTAS DA TURMA".center(40))
    print("="*40)
    print("Digite as notas (0 a 10) ou 'fim' para terminar")
    print("="*40)
    
    notas = []
    
    while True:
        entrada = input("Digite uma nota: ")
        
        if entrada.lower() == 'fim':
            if len(notas) == 0:
                print("Nenhuma nota foi registrada.")
                return
            else:
                break
        
        try:
            nota = float(entrada)
            if 0 <= nota <= 10:
                notas.append(nota)
                print(f"Nota {nota} registrada com sucesso!")
            else:
                print("ERRO: A nota deve estar entre 0 e 10.")
        except ValueError:
            print("ERRO: Digite um número válido ou 'fim' para terminar.")
    
    media = sum(notas) / len(notas)
    
    print("\n" + "="*40)
    print(f"Total de notas registradas: {len(notas)}")
    print(f"Média da turma: {media:.2f}")
    print("="*40)

if __name__ == "__main__":
    registrar_notas()