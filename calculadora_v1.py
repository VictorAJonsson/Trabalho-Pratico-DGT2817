def calculadorav1():
    print ("Calculadora v1")

    num1= float(input("Digite o primeiro numero:"))
    num2= float(input("Digite o primeiro numero:"))

    print ("Escolha a operação:")
    print ("1 - Soma")
    print ("2 - Subtracao")
    print ("3 - Multiplicação")
    print ("4 - Divisão")

    opcao = int(input("Digite a opção desejada:"))

    if opcao == 1:
        print(f"A soma dos números: {num1} + {num2} = {num1 + num2}")
    elif opcao == 2:
        print (f"A subitração dos numeros: {num1} - {num2} = {num1 - num2}")
    elif opcao == 3:
        print (f"A multiplicação dos numeros: {num1} * {num2} = {num1 * num2}")
    elif opcao == 4:
        print (f"A divisão dos numeros: {num1} / {num2} = {num1 / num2}")
    else:
        print ("Opção inválida")

calculadorav1()
   