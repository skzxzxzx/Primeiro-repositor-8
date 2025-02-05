def variar_menu():
    """Exibe o menu de opções para o usuário."""
    print("\n=== Calculadora Inteligente ===")
    print("1. Adição (+)")
    print("2. Subtração (-)")
    print("3. Multiplicação (*)")
    print("4. Divisão (/)")
    print("5. Sair")

def calcular(opcao, num1, num2):
    """Executa a operação escolhida pelo usuário."""
    if opcao == 1:
        return num1 + num2
    elif opcao == 2:
        return num1 - num2
    elif opcao == 3:
        return num1 * num2
    elif opcao == 4:
        if num2 != 0:
            return num1 / num2
        else:
            return "Erro: Divisão por zero não é permitida."

# Programa principal
while True:
    variar_menu()

    # Solicite a escolha do usuário
    try:
        opcao = int(input("\nEscolha uma opção (1-5): "))
    except ValueError:
        print("Opção inválida! Por favor, insira um número entre 1 e 5.")
        continue

    # Verifique se o usuário escolheu sair
    if opcao == 5:
        print("Saindo da calculadora. Até logo!")
        break

    # Verifique se a opção é válida
    if opcao not in [1, 2, 3, 4]:
        print("Opção inválida! Por favor, escolha uma opção válida.")
        continue

    # Solicite os números do usuário
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
    except ValueError:
        print("Entrada inválida! Por favor, insira números válidos.")
        continue

    # Realizar o cálculo
    resultado = calcular(opcao, num1, num2)

    # Exibir o resultado
    print(f"Resultado: {resultado}")
