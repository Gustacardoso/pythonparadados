frase = "Aprender Python aqui na Alura é muito bom"
frase_tratada = frase.replace(',', ' ').replace('.', ' ').replace('!', ' ').replace('?', ' ')
palavras = frase_tratada.split()
palavras_filtradas = list(filter(lambda palavra: len(palavra) >= 5, palavras))
print("Palavras com tamanho maior ou igual a 5:", palavras_filtradas)