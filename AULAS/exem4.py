produto1 = ["maça", 10, 0.30]
produto2 = ["banana", 15, 0.10]
produto3 = ["morango", 20, 2.50]

print(produto1)

compras = [produto1, produto2, produto3]

print(compras)

for item in compras:
    print("Produto: %s" % item[0])
    print("Quantidade: %s" % item[1])
    print("Preço unitário: %s" % item[2])