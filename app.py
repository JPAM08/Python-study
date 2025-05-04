def add (a,b):
    return a+b

def subtract (a,b):
    return a-b

def get_number (prompt):
    while True:
        return float (input(prompt))
    
def show_menu ():
    print("\n escolha operação")
    print("1 add")
    print("2 subtract")
    print("3 sair")
    return input("digite sua opção:")

def main ():
    print("=== Calculadora Simples com Funções ===\n")
    número = get_number("Qual número você quer começar?")
    while True:
        opcao = show_menu()
        if opcao == "1":
            outro = get_number("Digite o valor para adicionar: ")
            número = add(número,outro)
            print(f"Resultado atual: {número}")
        elif opcao == "2":
            outro = get_number("Digite o valor para subtrair: ")
            número = subtract(número,outro)
            print(f"Resultado atual: {número}")
        elif opcao == "3":
            print("Encerrando o programa. Até a próxima!")
            break  
        else: 
            print("Opção inválida. Tente novamente.")          

if __name__ == "__main__":
    main()