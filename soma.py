import entrada
L = []
for x in range(10):
    L.append(entrada.valida_inteiro("Digite um numero: ", 0, 20))
    print(f"Soma: {sum(L)}")