#Aquecimento
#1. Escreva um código que lê a lista abaixo e faça:

#lista = [16, 14, 63, 65, 17, 99, 70, 11, 20, 48, 79, 32, 17, 89, 12, 25, 66]
#Copiar código
#A leitura do tamanho da lista
#A leitura do maior e menor valor
#A soma dos valores da lista
#Ao final exiba uma mensagem dizendo:

#"A lista possui [tam] números em que o maior número é [maior] e o menor número é [menor]. A soma dos valores presentes nela é igual a [soma]"
#Copiar código
#Dica: use as funções embutidas presentes na documentação do Python.
lista = [16, 14, 63, 65, 17, 99, 70, 11, 20, 48, 79, 32, 17, 89, 12, 25, 66]
tamanho = len(lista)
maior = max(lista)
menor = min(lista)
soma = sum(lista)
print(f"A lista possui {tamanho} números em que o maior número é {maior} e o menor número é {menor}. A soma dos valores presentes nela é igual a {soma}")
#

#2. Escreva uma função que gere a tabuada de um número inteiro de 1 a 10, de acordo com a 
# escolha da pessoa usuária. Como exemplo, para o número 7, a tabuada deve ser mostrada no seguinte formato:

#Tabuada do 7:
#7 x 0 = 0
#7 x 1 = 7
#[...]
#7 x 10 = 70
def tabuada(numero):
    print(f"Tabuada do {numero}:")
    for i in range(11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")
num = int(input("Digite um número inteiro de 1 a 10 para ver a tabuada: "))
tabuada(num)
#Copiar código

#3. Crie a função que leia a lista abaixo e retorne uma nova lista com os múltiplos de 3:

#[97, 80, 94, 88, 80, 1, 16, 53, 62, 32, 24, 99]
#Copiar código
#Utilize o return na função e salve a nova lista na variável mult_3.
def multiplos_de_3(lista):
    mult_3 = [num for num in lista if num % 3 == 0]
    return mult_3
lista_numeros = [97, 80, 94, 88, 80, 1, 16, 53, 62, 32, 24, 99]
mult_3 = multiplos_de_3(lista_numeros)
print("Múltiplos de 3 na lista:", mult_3)

#4. Crie uma lista dos quadrados dos números da seguinte lista [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]. 
# Lembre-se de utilizar as funções lambda e map() para calcular o quadrado de cada elemento da lista.
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
quadrados = list(map(lambda x: x**2, numeros))
print("Lista dos quadrados dos números:", quadrados)


#5. Você foi contratado(a) como cientista de dados de uma associação de skate.
#Para analisar as notas recebidas de skatistas em algumas competições ao longo do ano, 
#você precisa criar um código que calcula a pontuação dos(as) atletas. Para isso, o
#seu código deve receber 5 notas digitadas pelas pessoas juradas.
#
#Para calcular a pontuação de um(a) skatista, você precisa eliminar a maior e a menor 
#pontuação dentre as 5 notas e tirar a média das 3 notas que sobraram. Retorne a média para apresentar o texto:
#
#"Nota da manobra: [media]"
notas = []
for i in range(5):
    nota = float(input(f"Digite a nota {i+1} do(a) skatista: "))
    notas.append(nota)
notas.remove(max(notas))
notas.remove(min(notas))
media = sum(notas) / len(notas)
print(f"Nota da manobra: {media}")

#6. Para atender a uma demanda de uma instituição de ensino para a análise do desempenho 
# de seus(suas) estudantes, você precisa criar uma função que receba uma lista de 4 notas e retorne:

#maior nota
#menor nota
#média
#situação (Aprovado(a) ou Reprovado(a))
#Para testar o comportamento da função, os dados podem ser exibidos em um texto:

#"O(a) estudante obteve uma média de [media], com a sua maior nota de [maior] pontos e a menor nota de [menor] pontos e foi [situacao]"

def analisar_notas(notas):
    maior = max(notas)
    menor = min(notas)
    media = sum(notas) / len(notas)
    situacao = "Aprovado(a)" if media >= 7 else "Reprovado(a)"
    return maior, menor, media, situacao

notas_estudante = []
for i in range(4):
    nota = float(input(f"Digite a nota {i+1} do(a) estudante: "))
    notas_estudante.append(nota)
maior, menor, media, situacao = analisar_notas(notas_estudante)
print(f"O(a) estudante obteve uma média de {media}, com a sua maior nota de {maior} pontos e a menor nota de {menor} pontos e foi {situacao}")


#7. Você recebeu uma demanda para tratar 2 listas com os nomes e sobrenomes de cada 
# estudante concatenando-as para apresentar seus nomes completos na forma Nome Sobrenome. As listas são:

#nomes = ["joão", "MaRia", "JOSÉ"]
#sobrenomes = ["SILVA", "souza", "Tavares"]

#"Nome completo: Ana Silva"
#Dica: utilize a função map para mapear os nomes e sobrenomes e as funções de string para tratar o texto.
nomes = ["joão", "MaRia", "JOSÉ"]
sobrenomes = ["SILVA", "souza", "Tavares"]
nomes_tratados = list(map(lambda nome: nome.capitalize(), nomes))
sobrenomes_tratados = list(map(lambda sobrenome: sobrenome.capitalize(), sobrenomes))
nomes_completos = list(map(lambda nome, sobrenome: f"{nome} {sobrenome}", nomes_tratados, sobrenomes_tratados))
for nome_completo in nomes_completos:
    print(f"Nome completo: {nome_completo}")
    
    
#8. Como cientista de dados em um time de futebol, você precisa implementar 
# novas formas de coleta de dados sobre o desempenho de jogadores e do time 
# como um todo. Sua primeira ação é criar uma forma de calcular a pontuação do 
# time no campeonato nacional a partir dos dados de gols marcados e sofridos em cada jogo.

#Escreva uma função chamada calcula_pontos que recebe como parâmetros duas listas 
# de números inteiros, representando os gols marcados e sofridos pelo time em cada 
# partida do campeonato. A função deve retornar a pontuação do time e o aproveitamento 
# em percentual, levando em consideração que a vitória vale 3 pontos, o empate vale 1 ponto e a derrota 0 pontos.

#Observação: se a quantidade de gols marcados numa partida for maior que a de sofridos, o 
# time venceu. Caso seja igual, o time empatou e se for menor, o time perdeu. Para calcular 
# o aproveitamento devemos fazer a razão entre a pontuação do time pela pontuação máxima que ele poderia receber.

#Para teste, utilize as seguintes listas de gols marcados e sofridos:

gols_marcados = [2, 1, 3, 1, 0]
gols_sofridos = [1, 2, 2, 1, 3]

#Provável texto exibido:

#"A pontuação do time foi de [pontos] e seu aproveitamento foi de [aprov]%"
def calcula_pontos(gols_marcados, gols_sofridos):
    pontos = 0
    total_partidas = len(gols_marcados)
    for marcados, sofridos in zip(gols_marcados, gols_sofridos):
        if marcados > sofridos:
            pontos += 3
        elif marcados == sofridos:
            pontos += 1
    pontuacao_maxima = total_partidas * 3
    aproveitamento = (pontos / pontuacao_maxima) * 100 if pontuacao_maxima > 0 else 0
    return pontos, aproveitamento
pontos, aproveitamento = calcula_pontos(gols_marcados, gols_sofridos)
print(f"A pontuação do time foi de {pontos} e seu aproveitamento foi de {aproveitamento}%")


#9. Você recebeu o desafio de criar um código que calcula os gastos de uma viagem 
#para um das quatro cidades partindo de Recife, sendo elas: Salvador, Fortaleza, Natal e Aracaju.
#
#O custo da diária do hotel é de 150 reais em todas elas e o consumo de gasolina 
#na viagem de carro é de 14 km/l, sendo que o valor da gasolina é de 5 reais o litro.
#O gastos com passeios e alimentação a se fazer em cada uma delas por dia seria de [200, 400, 250, 300], respectivamente.
#
#Sabendo que as distâncias entre Recife e cada uma das cidades é de aproximadamente
#[850, 800, 300, 550] km, crie três funções nas quais: a 1ª função calcule os gastos
#com hotel (gasto_hotel), a 2ª calcule os gastos com a gasolina (gasto_gasolina) e a 3ª os gastos com passeio e alimentação (gasto_passeio).
#
#Para testar, simule uma viagem de 3 dias para Salvador partindo de Recife. 
#Considere a viagem de ida e volta de carro.
#
#"Com base nos gastos definidos, uma viagem de [dias] dias para [cidade] saindo de Recife custaria [gastos] reais"

def gasto_hotel(dias):
    return dias * 150
def gasto_gasolina(distancia):
    consumo = distancia / 14
    return consumo * 5 * 2  # ida e volta
def gasto_passeio(dias, custo_diario):
    return dias * custo_diario
cidade = "Salvador"
distancia = 850
custo_passeio_diario = 200
dias = 3
total_gastos = (gasto_hotel(dias) + 
                gasto_gasolina(distancia) + 
                gasto_passeio(dias, custo_passeio_diario))
print(f"Com base nos gastos definidos, uma viagem de {dias} dias para {cidade} saindo de Recife custaria {total_gastos} reais")


#10. Você iniciou um estágio em uma empresa que trabalha com processamento de linguagem natural (NLP). 
#Sua líder requisitou que você criasse um trecho de código que recebe uma frase digitada pela pessoa 
#usuária e filtre apenas as palavras com tamanho maior ou igual a 5, exibindo-as em uma lista. Essa 
#demanda é voltada para a análise do padrão de comportamento de pessoas na escrita de palavras acima
#dessa quantidade de caracteres.
#
#Dica: utilize as funções lambda e filter() para filtrar essas palavras. Lembrando que a função
#embutida filter() recebe uma função (no nosso exemplo uma função lambda) e filtra um iterável
#de acordo com a função. Para tratar a frase use replace() para trocar a ',' '.', '!' e '?' por espaço.
#
#Use a frase "Aprender Python aqui na Alura é muito bom" para testar o código.

frase = "Aprender Python aqui na Alura é muito bom"
frase_tratada = frase.replace(',', ' ').replace('.', ' ').replace('!', ' ').replace('?', ' ')
palavras = frase_tratada.split()
palavras_filtradas = list(filter(lambda palavra: len(palavra) >= 5, palavras))
print("Palavras com tamanho maior ou igual a 5:", palavras_filtradas)
