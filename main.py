import os # Importa o módulo os para limpar a tela do console (os.system).

# Função que realiza cálculos com base no operador e nos números fornecidos.
def Calculator(operator, num1, num2):
    # Verifica qual operação deve ser realizada e imprime o resultado.
    if operator == "+":
        print(f">>> {num1} + {num2} = {num1+num2}") 
    if operador == "-":
        print(f">>> {num1} - {num2} = {num1-num2}") 
    if operador == "/":
        print(f">>> {num1} / {num2} = {num1/num2}") 
    if operador == "*":
        print(f">>> {num1} x {num2} = {num1*num2}") 
    if operador == "^":
        print(f">>> {num1} ^ {num2} = {num1**num2}") 
    
# Exibe o cabeçalho do programa.
print('=' * 30)
print("\tCALCULADORA")
print('=' * 30)

# Dicionário que mapeia operadores aos seus nomes.
operadores = {"+": "Soma", "-": "Subtração", "*": "Multiplicação", "/": "Divisão", "^": "Exponenciação"}

# Loop principal do programa.
while True:

    # Exibe as operações disponíveis.
    print("Operações Disponíveis:")
    for op, desc in operadores.items():
        print(f"{op} : {desc}")
    
    # Solicita ao usuário que escolha uma operação.
    operador = input("Digite a operação que deseja realizar: ")
    if operador not in operadores:
        print("\nDigite uma operação válida!") # Mensagem de erro para operador inválido.
        continue # Reinicia o loop.
    
    try:
        n1 = float(input("Digite o primeiro número: "))
        n2 = float(input("Digite o segundo número: "))
    except ValueError:
        print("O valor deve ser  um número inteiro.")
        continue # Reinicia o loop caso a entrada seja inválida.

    print("\n=========== RESULTADO ===========")
    Calculator(operador, n1, n2)
    print("\n")

    # Inicializa a variável de resposta do usuário.          
    resp = input("Deseja realizar uma nova operação (N ou S)? ").strip().upper()
    # Verifica se a resposta do usuário é válida.
    while resp not in ["S", "N", "s", "n"]:
            print("Digite S ou N")
            resp = input("Deseja realizar uma nova operação (N ou S)? ").strip().upper()
    # Se o usuário digitar "N", encerra o programa.
    if resp == "N":
        os.system("cls") # Limpa a tela.
        break
    # Caso o usuário escolha continuar, limpa a tela e reinicia o loop.
    elif resp == "S":
        os.system("cls")