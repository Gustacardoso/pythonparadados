notas = [3.5, 9.0, 6.0, 2.0]
def boletim(notas):
    media =sum(notas) / len(notas)
    
    if media >= 6:
            resultado = "Aprovado"
    elif 5 <= media < 6:
            resultado = "Recuperação"
    else:
            resultado ="Reprovado"
    return (media, resultado)


media, situacao = boletim(notas)
print(f'O(a) estudante atingiu uma média de {media} e foi {situacao}.')
