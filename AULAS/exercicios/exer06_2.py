
frase = input("Informe a frase: ")
tamanho = len(frase)
print("Tamanho da frase é: %d" % tamanho)
print("A palavra contem Python?", "Python" in frase)
print("Ultimos 5 digitos: ", frase[tamanho-5],frase[tamanho-4],frase[tamanho-3],frase[tamanho-2],frase[tamanho-1], )