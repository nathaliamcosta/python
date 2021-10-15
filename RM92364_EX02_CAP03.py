qts = 0.0
valor = 0.0

while qts != 6:
    print("PROGRAMA HEALTHTRACK")
    print("1 - 1 Transação")
    print("2 - 2 Transações")
    print("3 - 3 Transações")
    print("4 - 4 Transações")
    print("5 - 5 Transações")
    print("6 - Sair do programa")

    qts = int(input("Informe a quantidade de transações feitas hoje: "))

    if qts == 1:
       valor = float(input("Digite o valor da transação"))
       print("Você fez 1 transação no valor de {} hoje".format(valor))

    elif qts == 2:
        valor1 = float(input("Digite o valor da transação"))
        valor2 = float(input("Digite o valor da transação"))
        soma = valor1 + valor2
        media = soma/2
        print("Você fez 2 transações e gastou {} reais hoje e a média de gasto é {}".format(soma,media))

    elif qts == 3:
        valor1 = float(input("Digite o valor da transação"))
        valor2 = float(input("Digite o valor da transação"))
        valor3 = float(input("Digite o valor da transação"))
        soma = valor1 + valor2 + valor3
        media = soma/3
        print("Você fez 3 transações e gastou {} reais hoje e a média de gasto é {}".format(soma,media))

    elif qts == 4:
        valor1 = float(input("Digite o valor da transação"))
        valor2 = float(input("Digite o valor da transação"))
        valor3 = float(input("Digite o valor da transação"))
        valor4 = float(input("Digite o valor da transação"))
        soma = valor1 + valor2 + valor3 + valor4
        media = soma/4
        print("Você fez 4 transações e gastou {} reais hoje e a média de gasto é {}".format(soma,media))

    elif qts == 5:
        valor1 = float(input("Digite o valor da transação"))
        valor2 = float(input("Digite o valor da transação"))
        valor3 = float(input("Digite o valor da transação"))
        valor4 = float(input("Digite o valor da transação"))
        valor5 = float(input("Digite o valor da transação"))
        soma = valor1 + valor2 + valor3 + valor4 + valor5
        media = soma/5
        print("Você fez 5 transações e gastou {} reais hoje e a média de gasto é {}".format(soma,media))



    else:
        print("OK! O programa está encerrado...")
