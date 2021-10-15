#Nivel do cliente
nome_assinatura = input("Digite o nivel de sua assinatura")
valor_faturamento = input("Informe o valor do faturamento anual")

if nome_assinatura == "basic":
    valor_total= float(valor_faturamento) * 0.3
    print ("Você deverá pagar um bônus de {}" .format(valor_total))

if nome_assinatura == "silver":
    valor_total= float(valor_faturamento) * 0.2
    print ("Você deverá pagar um bônus de {}" .format(valor_total))

if nome_assinatura == "gold":
    valor_total= float(valor_faturamento) * 0.1
    print ("Você deverá pagar um bônus de {}" .format(valor_total))

if nome_assinatura == "platinum":
    valor_total= float(valor_faturamento) * 0.05
    print ("Você deverá pagar um bônus de {}" .format(valor_total))



