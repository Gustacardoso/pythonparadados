#Aquecendo na programação
#1) Faça um programa que tenha a seguinte lista contendo 
# os valores de gastos de uma empresa de papel 
# [2172.54, 3701.35, 3518.09, 3456.61, 3249.38, 
# 2840.82, 3891.45, 3075.26, 2317.64, 3219.08]. 
# Com esses valores, faça um programa que calcule a
# média de gastos. Dica: use as funções built-in sum() e len().

gastos = [2172.54, 3701.35, 3518.09, 3456.61, 3249.38,
        2840.82, 3891.45, 3075.26, 2317.64, 3219.08]
media_gastos = sum(gastos) / len(gastos)
print(f'A média de gastos da empresa é: R$ {media_gastos:.2f}')

#2) Com os mesmos dados da questão anterior, defina 
# quantas compras foram realizadas acima de 3000 reais
# e calcule a porcentagem quanto ao total de compras.
compras_acima_3000 = sum(1 for gasto in gastos if gasto > 3000)
porcentagem_acima_3000 = (compras_acima_3000 / len(gastos)) * 100
print(f'Número de compras acima de R$ 3000,00: {compras_acima_3000}')
print(f'Porcentagem de compras acima de R$ 3000,00: {porcentagem_acima_3000:.2f}%')

#3) Faça um código que colete em uma lista 5 números inteiros quaisquer e imprima a lista. Exemplo: [1,4,7,2,4].
lista_inteiros = []
for i in range(5):
    numero = int(input(f'Digite o {i+1}º número inteiro: '))
    lista_inteiros.append(numero)
print('A lista de números inteiros é:', lista_inteiros)
    
#4) Colete novamente 5 inteiros e imprima a lista em ordem inversa à enviada.
numeros_inversos = []
for i in range(5):
    numero = int(input(f'Digite o {i+1}º número inteiro: '))
    numeros_inversos.append(numero)
numeros_inversos.reverse()
print('A lista de números em ordem inversa é:', numeros_inversos)

#5) Faça um programa que, ao inserir um número qualquer, cria uma lista contendo todos os números primos entre 1 e o número digitado.
numero_limite = int(input("Digite um número inteiro positivo: "))
primos = []
for num in range(2, numero_limite + 1):
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            break
    else:
        primos.append(num)
print(f'Números primos entre 1 e {numero_limite}:', primos)

#6) Escreva um programa que peça uma data informando o dia, mês e ano e determine se ela é válida para uma análise.
dia = int(input("Digite o dia: "))
mes = int(input("Digite o mês: "))
ano = int(input("Digite o ano: "))
data_valida = True
if mes < 1 or mes > 12:
    data_valida = False
if dia < 1 or dia > 31:
    data_valida = False
if data_valida:
    print("Data válida.")
else:
    print("Data inválida.")
    

#7) Para um estudo envolvendo o nível de multiplicação de bactérias em uma colônia, 
# foi coletado o número de bactérias por dia (em milhares) e pode ser observado a 
# seguir: [1.2, 2.1, 3.3, 5.0, 7.8, 11.3, 16.6, 25.1, 37.8, 56.9]. Tendo esses valores,
# faça um código que gere uma lista contendo o percentual de crescimento de bactérias por dia, 
# comparando o número de bactérias em cada dia com o número de bactérias do dia anterior. 
# Dica: para calcular o percentual de crescimento usamos a seguinte equação: 
# 100 * (amostra_atual - amostra_passada) / (amostra_passada).
bacterias = [1.2, 2.1, 3.3, 5.0, 7.8, 11.3, 16.6, 25.1, 37.8, 56.9]
percentuais_crescimento = []
for i in range(1, len(bacterias)):
    crescimento = 100 * (bacterias[i] - bacterias[i - 1]) / bacterias[i - 1]
    percentuais_crescimento.append(crescimento)
print('Percentual de crescimento diário das bactérias:', percentuais_crescimento)


#8) Para uma seleção de produtos alimentícios, precisamos separar o conjunto 
# de IDs dados por números inteiros sabendo que os produtos com ID par são 
# doces e os com ID ímpar são amargos. Monte um código que colete 10 IDs. 
# Depois, calcule e mostre a quantidade de produtos doces e amargos.
ids = []
for i in range(10):
    produto_id = int(input(f'Digite o ID do {i+1}º produto: '))
    ids.append(produto_id)
doces = sum(1 for id in ids if id % 2 == 0)
amargos = sum(1 for id in ids if id % 2 != 0)
print(f'Quantidade de produtos doces (ID par): {doces}')
print(f'Quantidade de produtos amargos (ID ímpar): {amargos}')


#9) Desenvolva um programa que informa a nota de um(a) aluno(a) de acordo com suas respostas. 
# Ele deve pedir a resposta desse(a) aluno(a) para cada questão e é preciso verificar se 
# a resposta foi igual ao gabarito. Cada questão vale um ponto e existem as alternativas A, B, C ou D.

#Gabarito da prova:
#01 - D
#02 - A
#03 - C
#04 - B
#05 - A
#06 - D
#07 - C
#08 - C
#09 - A
#10 - B
gabarito = ['D', 'A', 'C', 'B', 'A', 'D', 'C', 'C', 'A', 'B']
nota = 0
for i in range(10):
    resposta = input(f'Digite a resposta da questão {i+1} (A, B, C ou D): ').upper()
    if resposta == gabarito[i]:
        nota += 1
print(f'A nota do aluno(a) é: {nota}/10')


#10) Um instituto de meteorologia deseja fazer um estudo de temperatura média de cada mês do ano. 
# Para isso, você precisa fazer um código que colete e armazene essas temperaturas médias em uma 
# lista. Depois, calcule a média anual das temperaturas e mostre todas as temperaturas acima da 
# média anual e em que mês elas ocorreram, mostrando os meses por extenso (Janeiro, Fevereiro, etc.).
temperaturas = []
meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
        'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
for i in range(12):
    temp = float(input(f'Digite a temperatura média de {meses[i]}: '))
    temperaturas.append(temp)

media_anual = sum(temperaturas) / len(temperaturas)
print(f'Média anual das temperaturas: {media_anual:.2f}°C')

acima_da_media = []
for i in range(12):
    if temperaturas[i] > media_anual:
        acima_da_media.append((meses[i], temperaturas[i]))

print("Temperaturas acima da média anual:")
for mes, temp in acima_da_media:
    print(f"{mes}: {temp:.2f}°C")

#11) Uma empresa de e-commerce está interessada em analisar as vendas dos seus produtos. Os dados das vendas foram armazenados em um dicionário:
#{'Produto A': 300, 'Produto B': 80, 'Produto C': 60,
# 'Produto D': 200, 'Produto E': 250, 'Produto F': 30}
#Escreva um código que calcule o total de vendas e o produto mais vendido.
vendas = {'Produto A': 300, 'Produto B': 80, 'Produto C': 60,
          'Produto D': 200, 'Produto E': 250, 'Produto F': 30}
total_vendas = sum(vendas.values())
produto_mais_vendido = max(vendas, key=vendas.get)
print(f'Total de vendas: {total_vendas} unidades')
print(f'Produto mais vendido: {produto_mais_vendido} com {vendas[produto_mais_vendido]} unidades vendidas')

#12) Uma pesquisa de mercado foi feita para decidir qual design de marca infantil mais agrada as crianças.
# A pesquisa foi feita e o votos computados podem ser observados abaixo:

#'''
#Tabela de votos da marca
#Design 1 - 1334 votos
#Design 2 - 982 votos
#Design 3 - 1751 votos
#Design 4 - 210 votos
#Design 5 - 1811 votos
#'''
#
#Adapte os dados fornecidos para uma estrutura de dicionário. A partir dele, informe o design vencedor e a porcentagem de votos recebidos.
votos = {
    'Design 1': 1334,
    'Design 2': 982,
    'Design 3': 1751,
    'Design 4': 210,
    'Design 5': 1811
}
total_votos = sum(votos.values())
design_vencedor = max(votos, key=votos.get)
porcentagem_vencedor = (votos[design_vencedor] / total_votos) * 100
print(f'Design vencedor: {design_vencedor} com {votos[design_vencedor]} votos ({porcentagem_vencedor:.2f}%)')

#13) As pessoas colaboradoras de um setor da empresa que você trabalha vão receber um abono 
# correspondente a 10% do salário devido ao ótimo desempenho do time. O setor financeiro 
# solicitou sua ajuda para a verificação das consequências financeiras que esse abono 
# irá gerar nos recursos. Assim, foi encaminhada para você uma lista com os salários 
# que receberão o abono: [1172, 1644, 2617, 5130, 5532, 6341, 6650, 7238, 7685, 7782, 7903]. 
# O abono de cada colaborador(a) não pode ser inferior a 200. Em código, transforme cada
# um dos salários em chaves de um dicionário e o abono de cada salário no elemento. 
# Depois, informe o total de gastos com o abono, quantos(as) colaboradores(as) 
# receberam o abono mínimo e qual o maior valor de abono fornecido.
salarios = [1172, 1644, 2617, 5130, 5532, 6341, 6650, 7238, 7685, 7782, 7903]
abonos = {}
for salario in salarios:
    abono = salario * 0.10
    if abono < 200:
        abono = 200
    abonos[salario] = abono
total_gastos = sum(abonos.values())
colaboradores_minimo = sum(1 for abono in abonos.values() if abono == 200)
maior_abono = max(abonos.values())
print(f'Total de gastos com abonos: R$ {total_gastos:.2f}')
print(f'Número de colaboradores(as) que receberam o abono mínimo: {colaboradores_minimo}')
print(f'Maior valor de abono fornecido: R$ {maior_abono:.2f}')
#

#14) Uma equipe de cientistas de dados está estudando a diversidade biológica em uma floresta.
# A equipe fez a coleta de informações sobre o número de espécies de plantas e animais em cada
# área dessa floresta e armazenou essas informações em um dicionário. Nele, a chave descreve 
# a área dos dados e os valores nas listas correspondem às espécies de plantas e animais nas áreas, respectivamente.
#{'Área Norte': [2819, 7236],
# 'Área Leste': [1440, 9492],
# 'Área Sul': [5969, 7496],
# 'Área Oeste': [14446, 49688],
# 'Área Centro': [22558, 45148]}
#Escreva um código para calcular a média de espécies por área e identificar a área com a maior diversidade biológica. Dica: use as funções built-in sum() e len().
diversidade_biologica = {
    'Área Norte': [2819, 7236],
    'Área Leste': [1440, 9492],
    'Área Sul': [5969, 7496],
    'Área Oeste': [14446, 49688],
    'Área Centro': [22558, 45148]
}
total_especies = 0
for especies in diversidade_biologica.values():
    total_especies += sum(especies)
media_especies = total_especies / len(diversidade_biologica)
area_maior_diversidade = max(diversidade_biologica, key=lambda area: sum(diversidade_biologica[area]))
print(f'Média de espécies por área: {media_especies:.2f}')

#15) O setor de RH da sua empresa te pediu uma ajuda para analisar as idades de colaboradores(as) 
# de 4 setores da empresa. Para isso, foram fornecidos os seguintes dados:
#{'Setor A': [22, 26, 30, 30, 35, 38, 40, 56, 57, 65],
# 'Setor B': [22, 24, 26, 33, 41, 49, 50, 54, 60, 64],
# 'Setor C': [23, 26, 26, 29, 34, 35, 36, 41, 52, 56],
# 'Setor D': [19, 20, 25, 27, 34, 39, 42, 44, 50, 65]}
#Sabendo que cada setor tem 10 colaboradores(as), construa um código que calcule a média de idade de cada setor, a 
# idade média geral entre todos os setores e quantas pessoas estão acima da idade média geral.
idades_setores = {
    'Setor A': [22, 26, 30, 30, 35, 38, 40, 56, 57, 65],
    'Setor B': [22, 24, 26, 33, 41, 49, 50, 54, 60, 64],
    'Setor C': [23, 26, 26, 29, 34, 35, 36, 41, 52, 56],
    'Setor D': [19, 20, 25, 27, 34, 39, 42, 44, 50, 65]
}
media_idades_setores = {}
total_idades = 0
total_colaboradores = 0
for setor, idades in idades_setores.items():
    media_idade = sum(idades) / len(idades)
    media_idades_setores[setor] = media_idade
    total_idades += sum(idades)
    total_colaboradores += len(idades)
media_idade_geral = total_idades / total_colaboradores
acima_media_geral = 0
for idades in idades_setores.values():
    for idade in idades:
        if idade > media_idade_geral:
            acima_media_geral += 1
print("Média de idade por setor:")
for setor, media in media_idades_setores.items():
    print(f"{setor}: {media:.2f} anos")
print(f"Média de idade geral: {media_idade_geral:.2f} anos")
print(f"Número de colaboradores(as) acima da média geral: {acima_media_geral}")
