#1) Escreva um programa que peça à pessoa usuária para fornecer dois números e exibir o número maior.
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
if numero1 > numero2:
    print(f"O número maior é: {numero1}")
else:
    print(f"O número maior é: {numero2}")
    
#2) Escreva um programa que solicite o percentual de crescimento de produção de uma empresa e informe se houve um crescimento (porcentagem positiva) ou decrescimento (porcentagem negativa).
porcentagem = float(input("Digite o percentual de crescimento da produção (use números negativos para decrescimento): "))
if porcentagem > 0:
    print("Houve um crescimento na produção.")
else:
    print("Houve um decrescimento na produção.")
    
    
#3) Escreva um programa que determine se uma letra fornecida pela pessoa usuária é uma vogal ou consoante.
palavra = input("Digite uma letra: ").lower()
if palavra in ['a', 'e', 'i', 'o', 'u']:
    print("A letra é uma vogal.")
else:
    print("A letra é uma consoante.")
    
#4) Escreva um programa que leia valores médios de preços de um modelo de carro por 3 anos consecutivos e exiba o valor mais alto e mais baixo entre esses três anos.
valor_ano1 = float(input("Digite o valor médio do carro no primeiro ano: "))
valor_ano2 = float(input("Digite o valor médio do carro no segundo ano: "))
valor_ano3 = float(input("Digite o valor médio do carro no terceiro ano: "))
valor_mais_alto = max(valor_ano1, valor_ano2, valor_ano3)
valor_mais_baixo = min(valor_ano1, valor_ano2, valor_ano3)
print(f"O valor mais alto entre os três anos é: {valor_mais_alto}")
print(f"O valor mais baixo entre os três anos é: {valor_mais_baixo}")

#5) Escreva um programa que pergunte sobre o preço de três produtos e indique qual é o produto mais barato para comprar.
preco1 = float(input("Digite o preço do primeiro produto: "))
preco2 = float(input("Digite o preço do segundo produto: "))
preco3 = float(input("Digite o preço do terceiro produto: "))
if preco1 < preco2 and preco1 < preco3:
    print("O produto mais barato é o primeiro produto.")
elif preco2 < preco1 and preco2 < preco3:
    print("O produto mais barato é o segundo produto.")
else:
    print("O produto mais barato é o terceiro produto.")
    
#6) Escreva um programa que leia três números e os exiba em ordem decrescente.
a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))
c = float(input("Digite o terceiro número: "))
numeros = [a, b, c]
numeros.sort(reverse=True)
print(f"Números em ordem decrescente: {numeros}")

#7) Escreva um programa que pergunte em qual turno a pessoa usuária estuda ("manhã", "tarde" ou "noite") e exiba a mensagem "Bom Dia!", "Boa Tarde!", "Boa Noite!", ou "Valor Inválido!", conforme o caso.
manha = "manhã"
tarde = "tarde"
noite = "noite"
turno = input("Em qual turno você estuda (manhã, tarde ou noite)? ").lower()
if turno == manha:
    print("Bom Dia!")
elif turno == tarde:
    print("Boa Tarde!")
elif turno == noite:
    print("Boa Noite!")
else:
    print("Valor Inválido!")
    
#8) Escreva um programa que peça um número inteiro à pessoa usuária e determine se ele é par ou ímpar. Dica: Você pode utilizar o operador módulo %.
numero1 = int(input("Digite um número inteiro: "))
if numero1 % 2 == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")
    
#9) Escreva um programa que peça um número à pessoa usuária e informe se ele é inteiro ou decimal.
numero1 = float(input("Digite um número: "))
if numero1.is_integer():
    print("O número é inteiro.")
else:
    print("O número é decimal.")
    
#Momento dos projetos
#10) Um programa deve ser escrito para ler dois números e, em seguida, perguntar à pessoa usuária qual operação ele deseja realizar. O resultado da operação deve incluir informações 
# sobre o número - se é par ou ímpar, positivo ou negativo e inteiro ou decimal.
a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))
operacao = input("Qual operação você deseja realizar? (+, -, *, /): ")
if operacao == '+':
    resultado = a + b
elif operacao == '-':
    resultado = a - b
elif operacao == '*':
    resultado = a * b
elif operacao == '/':
    if b != 0:
        resultado = a / b
    else:
        print("Erro: Divisão por zero não é permitida.")
        resultado = None
else:
    print("Operação inválida.")
    resultado = None
if resultado is not None:
    print(f"O resultado da operação é: {resultado}")
    if resultado % 2 == 0:
        print("O resultado é um número par.")
    else:
        print("O resultado é um número ímpar.")
    if resultado > 0:
        print("O resultado é um número positivo.")
    elif resultado < 0:
        print("O resultado é um número negativo.")
    else:
        print("O resultado é zero.")
    if resultado.is_integer():
        print("O resultado é um número inteiro.")
    else:
        print("O resultado é um número decimal.")
        
#11) Escreva um programa que peça à pessoa usuária três números que representam os lados de um triângulo.
# O programa deve informar se os valores podem ser utilizados para formar um triângulo e, caso afirmativo, se ele é equilátero, isósceles ou escaleno. Tenha em mente algumas dicas:
#Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
#Triângulo Equilátero: três lados iguais;
#Triângulo Isósceles: quaisquer dois lados iguais;
#Triângulo Escaleno: três lados diferentes.

lado1 = float(input("Digite o valor do primeiro lado do triângulo: "))
lado2 = float(input("Digite o valor do segundo lado do triângulo: "))
lado3 = float(input("Digite o valor do terceiro lado do triângulo: "))
if (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1):
    if lado1 == lado2 == lado3:
        print("Os valores podem formar um triângulo equilátero.")
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("Os valores podem formar um triângulo isósceles.")
    else:
        print("Os valores podem formar um triângulo escaleno.")
else:
    print("Os valores não podem formar um triângulo.")
    
#12) Um estabelecimento está vendendo combustíveis com descontos variados. 
# Para o etanol, se a quantidade comprada for até 15 litros, o desconto será de 2% por litro. Caso contrário, 
# será de 4% por litro. Para o diesel, se a quantidade comprada for até 15 litros, o desconto será de 3% por litro. 
# Caso contrário, será de 5% por litro. O preço do litro de diesel é R$ 2,00 e o preço do litro de etanol é R$ 1,70. 
# Escreva um programa que leia a quantidade de litros vendidos e o tipo de combustível (E para etanol e D para diesel) 
# e calcule o valor a ser pago pelo cliente. Tenha em mente algumas dicas:
#O do valor do desconto será a multiplicação entre preço do litro, quantidade de litros e o valor do desconto.
#O valor a ser pago por um cliente será o resultado da multiplicação do preço do litro pela quantidade de litros menos o valor de desconto resultante do cálculo.
combustivel = input("Digite o tipo de combustível (E para etanol e D para diesel): ").upper()
litros = float(input("Digite a quantidade de litros vendidos: "))
if combustivel == 'E':
    preco_litro = 1.70
    if litros <= 15:
        desconto = 0.02
    else:
        desconto = 0.04
elif combustivel == 'D':
    preco_litro = 2.00
    if litros <= 15:
        desconto = 0.03
    else:
        desconto = 0.05
else:
    print("Tipo de combustível inválido.")
    preco_litro = 0
    desconto = 0
if preco_litro != 0:
    valor_desconto = preco_litro * litros * desconto
    valor_a_pagar = (preco_litro * litros) - valor_desconto
    print(f"O valor a ser pago pelo cliente é: R$ {valor_a_pagar:.2f}") 


#13) Em uma empresa de venda de imóveis você precisa criar um código que analise os dados de vendas anuais para 
# ajudar a diretoria na tomada de decisão. O código precisa coletar os dados de quantidade de venda durante os 
# anos de 2022 e 2023 e fazer um cálculo de variação percentual. A partir do valor da variação, deve ser enviada às seguintes sugestões:

#Para variação acima de 20%: bonificação para o time de vendas.
#Para variação entre 2% e 20%: pequena bonificação para time de vendas.
#Para variação entre 2% e -10%: planejamento de políticas de incentivo às vendas.
#Para variação abaixo de -10%: corte de gastos.

vendas_2022 = float(input("Digite o valor das vendas em 2022: "))
vendas_2023 = float(input("Digite o valor das vendas em 2023: "))
variacao_percentual = ((vendas_2023 - vendas_2022) / vendas_2022) * 100
print(f"A variação percentual das vendas é: {variacao_percentual:.2f}%")
if variacao_percentual > 20:    
    print("Sugestão: bonificação para o time de vendas.")
elif 2 < variacao_percentual <= 20:
    print("Sugestão: pequena bonificação para time de vendas.")
elif -10 <= variacao_percentual <= 2:
    print("Sugestão: planejamento de políticas de incentivo às vendas.")
else:
    print("Sugestão: corte de gastos.")
    