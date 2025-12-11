print("hello wordl")
idade = 5
print(idade)
idade = 10
print(idade)
print("A idade é " + str(idade) + " anos")
print(f"A idade é {idade} anos")
nome = 'Gabriel'
print(f"O nome é {nome} e a idade é {idade} anos")
preco = 19.99
print(f"O preço é R$ {preco}")
i = 5
type(i)

q_seguranca = 5
s_seguranca = 3000

q_docente = 16
s_docente = 6000

q_diretoria = 1
s_diretoria = 12500

total_empregados = q_seguranca + q_docente + q_diretoria
print(f"O total de empregados é {total_empregados}")

diferenca_salario = s_diretoria - s_seguranca
print(f"A diferença salarial entre diretoria e segurança é R$ {diferenca_salario}")

media = (q_seguranca*s_seguranca + q_docente*s_docente + q_diretoria*s_diretoria) / (total_empregados)
print(f"A média salarial da instituição é R$ {media}")

potencia = 2**3
print(f"O valor da potência é {potencia}")

dividendo = 7
divisor = 3
dividendo % divisor
print(f"O resto da divisão é {dividendo % divisor}")

numerador = 7
denominador = 3
numerador // denominador
print(f"O resultado da divisão inteira é {numerador // denominador}")

chr(79) + chr(108) + chr(225)
print(f"O resultado da soma dos caracteres é {chr(79) + chr(108) + chr(225)}")
