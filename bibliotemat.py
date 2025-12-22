import matplotlib.pyplot as plt
from random import choice

estudantes = ['Ana', 'Bruno', 'Carla', 'Daniel', 'Eva']
notas = [8.5, 7.0, 9.0, 6.5, 8.0]
plt.bar( x = estudantes, height = notas)
plt.show()


estudantes_2 = ['Fabio', 'Gabriela', 'Hugo', 'Isabela', 'João']

#choice retorna um elemento aleatório de uma lista
sorteado = choice(estudantes_2)
print(f'O estudante sorteado para apresentar o trabalho é: {sorteado}')
