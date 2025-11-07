saida = ""
def adicao (num1, num2):
    return num1 + num2

def subtracao (num1, num2):
    return num1 - num2

def multiplicacao (num1, num2):
    return num1 * num2

def divisao (num1, num2):
    if num2 == 0:
        return "Impossível dividir por zero"
    else:
        return num1 / num2

def calculadora(num1, num2, opcao):
    if opcao == opcao.lower() == "soma" or opcao == "+":
        return adicao(num1, num2)
    elif opcao == opcao.lower() == "subtracao" or opcao == "subtração" or opcao == "-":
        return subtracao(num1, num2)
    elif opcao == opcao.lower() == "multiplicacao" or opcao == "multiplicação" or opcao == "*":
        return multiplicacao(num1, num2)
    elif opcao == opcao.lower() == "divisao" or opcao == "divisão" or opcao == "/":
        return divisao(num1, num2)
    else:
        resultado = "Opção inválida, escolha uma das opções: soma (+), subtracao (-), multiplicacao (*) ou divisao (/)"
    return resultado

while saida.lower() != "n":
    print("Calculadora v2")
    num1 = int(input("Digite o primeiro numero: "))
    num2 = int(input("Digite o segundo numero: "))
    print("Operações possíveis: Soma (+), Subtracao (-), Multiplicação (*) ou Divisão (/)")
    opcao = input("Digite a opção desejada: ")
    resultado = calculadora(num1, num2, opcao)
    print("Resultado da operação:", resultado)
    saida = input("Deseja sair? (s/n)")