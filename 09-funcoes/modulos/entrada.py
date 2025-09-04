def valida_inteiro(mensagem, mínimo, máximo):
    while True:
        v=int(input(mensagem))
        if v >= mínimo and v <= máximo:
            return v
        else:
            print("Digite um valor entre %d e %d" % (mínimo, máximo))