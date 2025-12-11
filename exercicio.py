#Crie um programa que solicite à pessoa usuária digitar seu nome, e imprima “Olá, [nome]!”
nome = input("Digite seu nome: ")
print(f"Olá, {nome}!")
#Crie um programa que solicite à pessoa usuária digitar seu nome e idade, e imprima “Olá, [nome], você tem [idade] anos.”.

idade = input("Digite sua idade: ")
print(f"Olá, {nome}, você tem {idade} anos.")

#Crie um programa que solicite à pessoa usuária digitar seu nome, idade e altura em metros, e imprima “Olá, [nome], você tem [idade] anos e mede [altura] metros!”.
altura = input("Digite sua altura em metros: ")
print(f"Olá, {nome}, você tem {idade} anos e mede {altura} metros!")

#Calculadora com operadores
#Crie um programa que solicite dois valores numéricos à pessoa usuária e imprima a soma dos dois valores.
a = float(input("Digite o primeiro valor numérico: "))
b = float(input("Digite o segundo valor numérico: "))
soma = a + b
print(f"A soma dos dois valores é: {soma}")


#Crie um programa que solicite três valores numéricos à pessoa usuária e imprima a soma dos três valores.
c = float(input("Digite o terceiro valor numérico: "))
soma_tres = a + b + c
print(f"A soma dos três valores é: {soma_tres}")

#Crie um programa que solicite dois valores numéricos à pessoa usuária e imprima a subtração do primeiro pelo o segundo valor.
subtracao = a - b
print(f"A subtração do primeiro pelo segundo valor é: {subtracao}")

#Crie um programa que solicite dois valores numéricos à pessoa usuária e imprima a multiplicação dos dois valores.
multiplicacao = a * b
print(f"A multiplicação dos dois valores é: {multiplicacao}")

#Crie um programa que solicite dois valores numéricos, um numerador e um denominador, e realize a divisão entre os dois valores. Deixe claro que o valor do denominador não pode ser 0.
numerador = float(input("Digite o numerador: "))
denominador = float(input("Digite o denominador (não pode ser 0): "))
if denominador != 0:
    divisao = numerador / denominador
    print(f"O resultado da divisão é: {divisao}")
else:
    print("Erro: O denominador não pode ser 0.")


#Crie um programa que solicite dois valores numéricos, um operador e uma potência, e realize a exponenciação entre esses dois valores.
valorPotencia = float(input("Digite o valor da base: "))
expoente = float(input("Digite o valor do expoente: "))
potenciacao = valorPotencia ** expoente
print(f"O resultado da exponenciação é: {potenciacao}")

#Crie um código que solicita 3 notas de um estudante e imprima a média das notas.
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
media_notas = (nota1 + nota2 + nota3) / 3
print(f"A média das notas é: {media_notas}")

#Crie um código que calcule e imprima a média ponderada dos números 5, 12, 20 e 15 com pesos respectivamente iguais a 1, 2, 3 e 4.
media_ponderada = (5*1 + 12*2 + 20*3 + 15*4) / (1 + 2 + 3 + 4)
print(f"A média ponderada é: {media_ponderada}")

#Editando textos
#Crie uma variável chamada “frase” e atribua a ela uma string de sua escolha. Em seguida, imprima a frase na tela.
frase = "Esta é uma frase de exemplo."
print(frase)

#Crie um código que solicite uma frase e depois imprima a frase na tela.
digite_frase = input("Digite uma frase: ")
print(digite_frase)

#Crie um código que solicite uma frase à pessoa usuária e imprima a mesma frase digitada mas com todas as letras maiúsculas.
print(f"maiscula: {digite_frase.upper()}")

#Crie um código que solicite uma frase à pessoa usuária e imprima a mesma frase digitada mas com todas as letras minúsculas.
print(f"minisculo:: {digite_frase.lower()}")

#Crie uma variável chamada “frase” e atribua a ela uma string de sua escolha. Em seguida, imprima a frase sem espaços em branco no início e no fim.
frase_espacos = "   Esta é uma frase com espaços.   "
print(frase_espacos.strip())

#Crie um código que solicite uma frase à pessoa usuária e imprima a mesma frase sem espaços em branco no início e no fim.
frase_usuario = input("Digite uma frase: ")
print(frase_usuario.strip())

#Crie um código que solicite uma frase à pessoa usuária e imprima a mesma frase sem espaços em branco no início e no fim e em letras minúsculas.
frase_sem_espacos = frase_usuario.strip()
print(frase_sem_espacos.lower())


#Crie um código que solicite uma frase à pessoa usuária e imprima a mesma frase com todas as vogais “e” trocadas pela letra “f”.
frase_trocada = frase_usuario.replace('e', 'f').replace('E', 'F')
print(frase_trocada)

#Crie um código que solicite uma frase à pessoa usuária e imprima a mesma frase com todas as vogais “a” trocadas pela caractere “@”.
palavra_trocada = frase_usuario.replace('a', '@').replace('A', '@')
print(palavra_trocada)

#Crie um código que solicite uma frase à pessoa usuária e imprima a mesma frase com todas as consoantes “s” trocadas pelo caractere “$”.
consoante_trocada = frase_usuario.replace('s', '$').replace('S', '$')
print(consoante_trocada)