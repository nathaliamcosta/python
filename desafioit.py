#desafio itflex cadastro
nome = input("Digite seu nome")
setor = input("Digite seu setor")
ramal = input("Digite seu ramal")
listasetor = ["marketing", "compras", "financeiro", "logistica", "diretoria", "rh"]
print("Olá {}, seu setor é o {} e seu ramal é {}".format(nome, setor, ramal))


print("Os setores disponíveis são: {}".format(listasetor))
l = input("Digite o setor que deseja conectar")
s = input("Digite o ramal que deseja conetar do setor {}".format(l))
print("{}, você deseja conectar com o ramal {} do setor {}, estamos completando sua solicitação".format(nome,s,l))
