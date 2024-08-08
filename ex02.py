prim = float(input("Digite o primeiro termo da PA: "))
quntidade = int(input("Digite a quantidade de termos: "))
razao = float(input("Digite a razão da PA: "))

print("Os termos da Progressão Aritmética são:")
for n in range(quntidade):
    termo = prim + n * razao
    print(termo)
