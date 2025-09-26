lista1 = [1,2,3,4,5,8]
lista2 = [4,5,6,7,8,9]

lista_final = []

lista_combinada = lista1 + lista2

print(lista_combinada)

for felipe in lista_combinada:
    if felipe not in lista_final:
        lista_final.append(felipe)

print(lista_final)