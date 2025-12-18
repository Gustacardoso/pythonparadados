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