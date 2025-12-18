#1) Escreva um programa que peça dois números inteiros e imprima todos os números inteiros entre eles.
num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))
if num1 < num2:
    for i in range(num1 + 1, num2):
        print(i)

#2) Escreva um programa para calcular quantos dias levará para a colônia de uma bactéria A ultrapassar ou igualar a colônia de uma bactéria B, 
# com base nas taxas de crescimento de 3% e 1,5% respectivamente. Considere que a colônia A inicia com 4 elementos e a B com 10.
colonia_A = 4
colonia_B = 10
dias = 0
while colonia_A < colonia_B:
    colonia_A += colonia_A * 0.03
    colonia_B += colonia_B * 0.015
    dias += 1
print(f"A colônia A ultrapassará ou igualará a colônia B em {dias} dias.")


#3) Para tratar uma quantidade de 15 dados de avaliações de pessoas usuárias de um serviço da empresa, 
# precisamos verificar se as notas são válidas. Então, escreva um programa que vai receber a nota 
# de 0 a 5 de todos os dados e verificar se é um valor válido. Caso seja inserido uma nota acima de 5 ou 
# abaixo de 0, repita até que a pessoa usuária insira um valor válido.

for i in range(15):
    nota = float(input("Digite a nota (de 0 a 5): "))
    while nota < 0 or nota > 5:
        print("Nota inválida. Tente novamente.")
        nota = float(input("Digite a nota (de 0 a 5): "))
    print(f"Nota {i+1} registrada: {nota}")
    
#4) Desenvolva um programa que leia um conjunto indeterminado de temperaturas em
# Celsius e informe a média delas. A leitura deve ser encerrada ao ser enviado o valor -273°C.
soma_temperaturas = 0
contador = 0
while True:
    temperatura = float(input("Digite a temperatura em Celsius (-273 para encerrar): "))
    if temperatura == -273:
        break
    soma_temperaturas += temperatura
    contador += 1
if contador > 0:
    media_temperaturas = soma_temperaturas / contador
    print(f"A média das temperaturas é: {media_temperaturas:.2f} °C")
else:
    print("Nenhuma temperatura válida foi inserida.")
    

#5) Escreva um programa que calcule o fatorial de um número inteiro fornecido pela pessoa usuária. 
# Lembrando que o fatorial de um número inteiro é a multiplicação desse número por todos os seus 
# antecessores até o número 1. Por exemplo, o fatorial de 5 é 5 x 4 x 3 x 2 x 1 = 120.
numero = int(input("Digite um número inteiro para calcular o fatorial: "))
fatorial = 1
for i in range(1, numero + 1):
    fatorial *= i
print(f"O fatorial de {numero} é: {fatorial}")  

#6) Escreva um programa que gere a tabuada de um número inteiro de 1 a 10, de acordo com a escolha da pessoa usuária.
#Como exemplo, para o número 2, a tabuada deve ser mostrada no seguinte formato:
#
#Tabuada do 2:
#2 x 1 = 2
#2 x 2 = 4
#[...]
#2 x 10 = 20

numero = int(input("Digite um número inteiro para ver a tabuada: "))
print(f"Tabuada do {numero}:") 
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")

#7) Os números primos possuem várias aplicações dentro da Ciência de Dados em criptografia e segurança, 
# por exemplo. Um número primo é aquele que é divisível apenas por um e por ele mesmo. Assim, faça 
# um programa que peça um número inteiro e determine se ele é ou não um número primo.

num = int(input("Digite um número inteiro para verificar se é primo: "))
if num > 1:
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            print(f"{num} não é um número primo.")
            break
    else:
        print(f"{num} é um número primo.")
else:
    print(f"{num} não é um número primo.")
    
#8) Vamos entender a distribuição de idades de pensionistas de uma empresa de previdência. 
# Escreva um programa que leia as idades de uma quantidade não informada de clientes e mostre 
# a distribuição em intervalos de [0-25], [26-50], [51-75] e [76-100]. Encerre a entrada de dados com um número negativo.
idades = []
while True:
    idade = int(input("Digite a idade do pensionista (número negativo para encerrar): "))
    if idade < 0:
        break
    idades.append(idade)
intervalo_0_25 = sum(1 for idade in idades if 0 <= idade <= 25)
intervalo_26_50 = sum(1 for idade in idades if 26 <= idade <= 50)
intervalo_51_75 = sum(1 for idade in idades if 51 <= idade <= 75)
intervalo_76_100 = sum(1 for idade in idades if 76 <= idade <= 100)
print(f"Distribuição de idades dos pensionistas:")
print(f"[0-25]: {intervalo_0_25} pensionistas")
print(f"[26-50]: {intervalo_26_50} pensionistas")
print(f"[51-75]: {intervalo_51_75} pensionistas")
print(f"[76-100]: {intervalo_76_100} pensionistas")

#9) Em uma eleição para gerência em uma empresa com 20 pessoas colaboradoras, existem quatro candidatos(as). Escreva um 
# programa que calcule o(a) vencedor(a) da eleição. A votação ocorreu da seguinte maneira:
#Cada colaborador(a) votou em uma das quatro pessoas candidatas (que representamos pelos números 1, 2, 3 e 4).
#Também foram contabilizados os votos nulos (representados pelo número 5) e os votos em branco (representados pelo número 6).
#Ao final da votação, o programa deve exibir o número total de votos para cada candidato(a), os nulos e os votos em branco. 
# Além disso, deve calcular e exibir a porcentagem de votos nulos em relação ao total de votos e a porcentagem de votos em branco em relação ao total de votos.

candidatos = {1: 0, 2: 0, 3: 0, 4: 0}
votos_nulos = 0
votos_brancos = 0
total_votos = 20
for i in range(total_votos):
    voto = int(input("Digite o número do candidato (1-4), 5 para nulo, 6 para branco: "))
    if voto in candidatos:
        candidatos[voto] += 1
    elif voto == 5:
        votos_nulos += 1
    elif voto == 6:
        votos_brancos += 1
    else:
        print("Voto inválido. Tente novamente.")
print("\nResultado da eleição:")
for candidato, votos in candidatos.items():
    print(f"Candidato {candidato}: {votos} votos")