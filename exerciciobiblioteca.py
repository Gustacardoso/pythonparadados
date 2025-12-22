#1. Escreva um código para instalar a versão 3.7.1 da biblioteca matplotlib.
#pip install matplotlib==3.7.1

#2. Escreva um código para importar a biblioteca numpy com o alias np.
import numpy as np

#3. Crie um programa que leia a seguinte lista de números e escolha um número desta aleatoriamente.
lista = [8, 12, 54, 23, 43, 1, 90, 87, 105, 77]

from random import choice
numero_sorteado = choice(lista)
print(f'O número sorteado da lista é: {numero_sorteado}')


#4. Crie um programa que sorteia, aleatoriamente, um número inteiro positivo menor que 100.
#Dica: use a função randrange() da biblioteca random. Essa função recebe como parâmetro o
#valor limite para a escolha aleatória ou um intervalo se passado o limite mínimo e máximo. 
#Por exemplo, randrange(5) gera valores inteiros menores que 5

from random import randrange
numero_aleatorio = randrange(100)
print(f'O número inteiro positivo menor que 100 sorteado é: {numero_aleatorio}')

#5. Crie um programa que solicite à pessoa usuária digitar dois números inteiros e calcular a potência do 1º número elevado ao 2º.
#Dica: use a função pow() da biblioteca math

import math
base = int(input("Digite o primeiro número inteiro (base): "))
expoente = int(input("Digite o segundo número inteiro (expoente): "))
resultado = math.pow(base, expoente)
print(f"O resultado de {base} elevado a {expoente} é: {resultado}")

#6. Um programa deve ser escrito para sortear uma pessoa seguidora de uma 
# rede social para ganhar um prêmio. A lista de participantes é numerada e 
# devemos escolher aleatoriamente um número de acordo com a quantidade de 
# participantes. Peça à pessoa usuária para fornecer o número de 
# participantes do sorteio e devolva para ela o número sorteado.

num_participantes = int(input("Digite o número de participantes do sorteio: "))
numero_sorteado = randrange(1, num_participantes + 1)
print(f'O número sorteado do sorteio é: {numero_sorteado}')
#

#7. Você recebeu uma demanda para gerar números de token para acessar o aplicativo 
# de uma empresa. O token precisa ser par e variar de 1000 até 9998. Escreva um 
# código que solicita à pessoa usuária o seu nome e exibe uma mensagem junto a esse token gerado aleatoriamente.
#"Olá, [nome], o seu token de acesso é [token]! Seja bem-vindo(a)!"
token = randrange(1000, 9999, 2)
nome = input("Digite o seu nome: ")
print(f"Olá, {nome}, o seu token de acesso é {token}! Seja bem-vindo(a)!")


#8. Para diversificar e atrair novos(as) clientes, uma lanchonete criou um item misterioso 
# em seu cardápio chamado "salada de frutas surpresa". Neste item, são escolhidas aleatoriamente 
# 3 frutas de uma lista de 12 para compor a salada de frutas da pessoa cliente. 
# Crie o código que faça essa seleção aleatória de acordo com a lista abaixo:

frutas = ["maçã", "banana", "uva", "pêra", 
          "manga", "coco", "melancia", "mamão",
          "laranja", "abacaxi", "kiwi", "ameixa"]
salada_surpresa = np.random.choice(frutas, size=3, replace=False)
print("A salada de frutas surpresa contém as seguintes frutas:")
for fruta in salada_surpresa:
    print(f"- {fruta}")
    

#9. Você recebeu um desafio de calcular a raiz quadrada de uma lista de números, 
# identificando quais resultaram em um número inteiro. A lista é a seguinte:

numeros = [2, 8, 15, 23, 91, 112, 256]
print("Números com raízes quadradas inteiras:")
for num in numeros:
    raiz = math.sqrt(num)
    if raiz.is_integer():
        print(f"Número: {num}, Raiz Quadrada: {int(raiz)}")
#No final, informe quais números possuem raízes inteiras e seus respectivos valores.
#Dica: use a comparação entre a divisão inteira (//) da raiz por 1 com o valor da raiz para verificar se o número é inteiro. Por exemplo:
num = 1.5
num_2 = 2
print(f'{num} é inteiro? :', num // 1 == num)
print(f'{num_2} é inteiro? :', num_2 // 1 == num_2)

#Saída:

#1.5 é inteiro? : False
#2 é inteiro? : True

#10. Faça um programa para uma loja que vende grama para jardins. Essa loja trabalha com jardins 
# circulares e o preço do metro quadrado da grama é de R$ 25,00. Peça à pessoa usuária o raio
# da área circular e devolva o valor em reais do quanto precisará pagar.

#Dica: use a variável pi e o método pow() da biblioteca math. O cálculo da área de um círculo é de: A = π*r^2 (lê-se pi vezes raio ao quadrado).

raio = float(input("Digite o raio do jardim circular em metros: "))
area = math.pi * math.pow(raio, 2)
preco_por_metro_quadrado = 25.00
custo_total = area * preco_por_metro_quadrado
print(f"O custo total para cobrir o jardim com grama é: R$ {custo_total:.2f}")
