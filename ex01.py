numa = int(input("Digite um número: "))
numb = int(input("Digite outro número: "))

if numa < numb:
    soma = 0
    
    for inter in range(numa, numb + 1):
        soma += inter
    print(f"O valor da soma do intervalo entre {numa} e {numb} é: {soma}")

else:
    print("Erro: o primeiro número deve ser menor que o segundo.")
