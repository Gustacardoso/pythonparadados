if 2>7:
   print('condição verdadeira')
   print()
print('fora do bloco')



idade_maria = int(input('Digite a idade da Maria: '))
idade_beatriz = int(input('Digite a idade da Beatriz: '))

if idade_maria > idade_beatriz:
   print('Maria é mais velha que Beatriz.')
else:
   print('Beatriz é mais velha que Maria.')
   
livro_1 = input('Digite o título do 1° livro: ')
livro_2 = input('Digite o título do 2° livro: ')

if livro_1 == livro_2:
   print('Os livros têm o mesmo título')
   
media = float(input('Digite a média: '))

if media >= 6.0:
   print('Aprovado(a)')
else:
   print('Reprovado(a)')
  
  
   media = float(input('Digite a média: '))

if media >= 6.0:
   print('Aprovado(a)')
if 6.0 > media >= 4.0:
   print('Recuperação')
if media < 4.0:
   print('Reprovado(a)')
   
   
   
if media >= 6.0:
   print('Aprovado(a)')
elif 6.0 > media >= 4.0:
   print('Recuperação')
if media < 4.0:
   print('Reprovado(a)')
   
t1 = t2 = True
f1 = f2 = False 
if t1 and t2:
   print('expressão verdadeira')
else:
   print('expressão falsa')
   
if f1 or f2:
   print('expressão verdadeira')
else:
   print('expressão falsa')

if not t1:
   print('expressão verdadeira')
else:
   print('expressão falsa')
   


