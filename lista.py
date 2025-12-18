lista =['Fabricio Daniel', 9.5, 9.0, 10.0, True]
len(lista)
print(f'A lista possui {len(lista)} elementos.')
lista[:3]
print('Os três primeiros elementos da lista são:', lista[:3])
lista.extend([10.0,8.0,9.0])
lista.append([10.0,8.0,9.0])
lista.remove([10.0,8.0,9.0])
raca_caes = ['Labrador Retriever','Bulldog Francês',
            'Pastor Alemão',
            'Poodle']
raca_caes.insert(1, 'Golden Retriever')
print(raca_caes)
raca_caes.pop(1)
raca_caes.index('Pastor Alemão')
raca_caes.sort()
raca_caes


loja = {'nomes': ['televisão', 'celular', 'notebook', 'geladeira', 'fogão'],
        'precos': [2000, 1500, 3500, 4000, 1500]}


for chave, elementos in loja.items():
  print(f'Chave: {chave}\nElementos:')
  for dado in elementos:
    print(dado)
    
    precos = [100.0, 400.0, 200.0]
soma = sum(precos)
soma
    