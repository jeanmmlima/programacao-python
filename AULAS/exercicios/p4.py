TP = int(input("Inserir total de pessoas: "))

pessoa = 0
soma_idade = 0

while pessoa < TP:
    idade = int(input(f"Inserir a idade da pessoa {pessoa+1}: "))
    soma_idade += idade
    pessoa += 1

media = soma_idade/TP
print("Média: %f" % media)

if media >= 0 and media <= 25:
    print("Turma é jovem!")
elif media >= 26 and media <= 60:
    print("Turma é adulta!")
else:
    print("Turma é idosa!")
