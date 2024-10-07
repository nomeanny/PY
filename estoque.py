estoque = {"alface": [1000, 2.30],
          "batata": [500, 0.45],
          "tomate": [2001, 1.20],
          "feijão": [100, 1.50]}
venda = [["tomate", 5], ["batata", 10], ["alface", 5]]
total = 0
print("Vendas:\n")
for operação in venda:
    produto, quantidade = operação
    preço = estoque[produto][1]
    custo = preço * quantidade
    print(f"{produto:12s}: {quantidade:3d} x {preço:6.2f} = {custo:6.2 f}")
    estoque[produto][0] -= quantidade
    total += custo
print(f"Custo toal: [total:21.2f]\n")
print(f"Estoque:\n")
for chave, dados in estoque.items():
    print(f"Descrição: ", chave)
    print(f"Quantidade: ", dados[0])
    print(f"Preço: {dados[1]:6.2f}\n")