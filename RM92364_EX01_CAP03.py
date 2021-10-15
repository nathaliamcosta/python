alimento = 0.0
caloria = 0.0

while alimento != 6:
    print("PROGRAMA HEALTHTRACK")
    print("1 - 1 Alimento")
    print("2 - 2 Alimentos")
    print("3 - 3 Alimentos")
    print("4 - 4 Alimentos")
    print("5 - 5 Alimentos")
    print("6 - Sair do programa")

    alimento = int(input("Informe a quantidade de alimentos ingeridos hoje: "))

    if alimento == 1:
       caloria = float(input("Digite quantas calorias seu alimento teve"))
       print("Você ingeriu 1 alimento com {} calorias hoje".format(caloria))

    elif alimento == 2:
        caloria1 = float(input("Digite quantas calorias seus alimentos teve"))
        caloria2 = float(input("Digite quantas calorias seus alimentos teve"))
        soma = caloria1 + caloria2
        print("Você ingeriu 2 alimentos com {} calorias hoje".format(soma))

    elif alimento == 3:
        caloria1 = float(input("Digite quantas calorias seus alimentos teve"))
        caloria2 = float(input("Digite quantas calorias seus alimentos teve"))
        caloria3 = float(input("Digite quantas calorias seus alimentos teve"))
        soma = caloria1 + caloria2 + caloria3
        print("Você ingeriu 3 alimentos com {} calorias hoje".format(soma))

    elif alimento == 4:
        caloria1 = float(input("Digite quantas calorias seu alimento teve"))
        caloria2 = float(input("Digite quantas calorias seus alimentos teve"))
        caloria3 = float(input("Digite quantas calorias seus alimentos teve"))
        caloria4 = float(input("Digite quantas calorias seus alimentos teve"))
        soma = caloria1 + caloria2 + caloria3 + caloria4
        print("Você ingeriu 3 alimentos com {} calorias hoje".format(soma))

    elif alimento == 5:
        caloria1 = float(input("Digite quantas calorias seus alimentos teve"))
        caloria2 = float(input("Digite quantas calorias seus alimentos teve"))
        caloria3 = float(input("Digite quantas calorias seus alimentos teve"))
        caloria4 = float(input("Digite quantas calorias seus alimentos teve"))
        caloria5 = float(input("Digite quantas calorias seus alimentos teve"))
        soma = caloria1 + caloria2 + caloria3 + caloria4 + caloria5
        print("Você ingeriu 3 alimentos com {} calorias hoje".format(soma))

    else:
        print("OK! O programa está encerrado...")





