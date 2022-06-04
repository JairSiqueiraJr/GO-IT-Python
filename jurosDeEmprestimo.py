totalJuros = 0
print("-           Banco do Sul              -")
print("---------------------------------------")
print("-         Opção de Credito            -")
print("Juros     Valores dos Empréstimos     -")
print(" 3%       Até R$10.000,00             -")
print(" 5%       R$10.001,00 até R$20.000,00 -")
print(" 7%       R$20.001,00 até R$30.000,00 -")
print("10%       Mais de R$30.001,00")
print("---------------------------------------")
nomeCliente = input("Nome do Cliente: ")
valorCredito = int(input("Digite O valor do Empréstimo:    -"))
print("---------------------------------------")

print("Forma de pagamento:                   -")
print("1 -        Em 6 meses juros de 8%     -")
print("2 -        Em 10 meses juros de 14%   -")
print("3 -        Em 15 meses juros de 20%   -")
print("4 -        Em 24 meses juros de 30%   -")
print("---------------------------------------")

valor1 = int(input("Digite a opção de parcela:        -"))
print("---------------------------------------")

#estrutura para valor menor que 10 mil e parcelas com juros.
if valorCredito <= 10000 and valor1 == 1:
    totalJuros = valorCredito + (valorCredito * 0.11)
    print("Cliente: ", nomeCliente)
    print("Pagamento total: ",totalJuros)
    totalJuros = totalJuros/6
    print("Preço das parcelas: ",totalJuros)
    print("---------------------------------------")
if valorCredito <= 10000 and valor1 == 2:
    totalJuros = valorCredito +(valorCredito * 0.17)
    print("Cliente: ", nomeCliente)
    print("Pagamento total: ",totalJuros)
    totalJuros = totalJuros/10
    print("Preço das parcelas: ",totalJuros)
    print("---------------------------------------")

    
if valorCredito <= 10000 and valor1 == 3:
    totalJuros = valorCredito +(valorCredito * 0.23)
    print("Cliente: ", nomeCliente)
    print("Pagamento total: ",totalJuros)
    totalJuros = totalJuros/15
    print("Preço das parcelas: ",totalJuros)
    print("---------------------------------------")

    
if valorCredito <= 10000 and valor1 == 4:
    totalJuros = valorCredito +(valorCredito * 0.33)
    print("Cliente: ", nomeCliente)
    print("Pagamento total: ",totalJuros)
    totalJuros = totalJuros/24
    print("Preço das parcelas: ",totalJuros)
    print("---------------------------------------")
    
#Estrutura para o valor acima de 10 mil e menor que 20 mil com seus juros.

if valorCredito > 10000 and valorCredito < 20000 and valor1 == 1:
    totalJuros = valorCredito + (valorCredito * 0.13)
    print("Cliente: ", nomeCliente)
    print("Pagamento total: ",totalJuros)
    totalJuros = totalJuros/6
    print("Preço das parcelas: ",totalJuros)
    print("---------------------------------------")
if valorCredito > 10000 and valorCredito < 20000 and valor1 == 2:
    totalJuros = valorCredito +(valorCredito * 0.19)
    print("Cliente: ", nomeCliente)
    print("Pagamento total: ",totalJuros)
    totalJuros = totalJuros/10
    print("Preço das parcelas: ",totalJuros)
    print("---------------------------------------")
if valorCredito > 10000 and valorCredito < 20000 and valor1 == 3:
    totalJuros = valorCredito +(valorCredito * 0.25)
    print("Cliente: ", nomeCliente)
    print("Pagamento total: ",totalJuros)
    totalJuros = totalJuros/15
    print("Preço das parcelas: ",totalJuros)
    print("---------------------------------------")
if valorCredito > 10000 and valorCredito < 20000 and valor1 == 4:
    totalJuros = valorCredito +(valorCredito * 0.35)
    print("Cliente: ", nomeCliente)
    print("Pagamento total: ",totalJuros)
    totalJuros = totalJuros/24
    print("Preço das parcelas: ",totalJuros)
    print("---------------------------------------")
    
#estrutura para maior que 20 mil e menor que 30 mil.

if valorCredito > 20000 and valorCredito < 30000 and valor1 == 1:
    totalJuros = valorCredito + (valorCredito * 0.15)
    print("Cliente: ", nomeCliente)
    print("Pagamento total: ",totalJuros)
    totalJuros = totalJuros/6
    print("Preço das parcelas: ",totalJuros)
    print("---------------------------------------")
if valorCredito > 20000 and valorCredito < 30000 and valor1 == 2:
    totalJuros = valorCredito +(valorCredito * 0.21)
    print("Cliente: ", nomeCliente)
    print("Pagamento total: ",totalJuros)
    totalJuros = totalJuros/10
    print("Preço das parcelas: ",totalJuros)
    print("---------------------------------------")
if valorCredito > 20000 and valorCredito < 30000 and valor1 == 3:
    totalJuros = valorCredito +(valorCredito * 0.27)
    print("Cliente: ", nomeCliente)
    print("Pagamento total: ",totalJuros)
    totalJuros = totalJuros/15
    print("Preço das parcelas: ",totalJuros)
    print("---------------------------------------")
if valorCredito > 20000 and valorCredito < 30000 and valor1 == 4:
    totalJuros = valorCredito +(valorCredito * 0.37)
    print("Cliente: ", nomeCliente)
    print("Pagamento total: ",totalJuros)
    totalJuros = totalJuros/24
    print("Preço das parcelas: ",totalJuros)
    print("---------------------------------------")
    
if valorCredito > 30000 and valor1 == 1:
    totalJuros = valorCredito + (valorCredito * 0.18)
    print("Cliente: ", nomeCliente)
    print("Pagamento total: ",totalJuros)
    totalJuros = totalJuros/6
    print("Preço das parcelas: ",totalJuros)
    print("---------------------------------------")
if valorCredito > 30000 and  valor1 == 2:
    totalJuros = valorCredito +(valorCredito * 0.24)
    print("Cliente: ", nomeCliente)
    print("Pagamento total: ",totalJuros)
    totalJuros = totalJuros/10
    print("Preço das parcelas: ",totalJuros)
    print("---------------------------------------")
if valorCredito > 30000 and valor1 == 3:
    totalJuros = valorCredito +(valorCredito * 0.30)
    print("Cliente: ", nomeCliente)
    print("Pagamento total: ",totalJuros)
    totalJuros = totalJuros/15
    print("Preço das parcelas: ",totalJuros)
    print("---------------------------------------")
if valorCredito > 30000 and valor1 == 4:
    totalJuros = valorCredito +(valorCredito * 0.40)
    print("Cliente: ", nomeCliente)
    print("Pagamento total: ",totalJuros)
    totalJuros = totalJuros/24
    print("Preço das parcelas: ",totalJuros)
    print("---------------------------------------")
    