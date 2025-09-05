def valida_inteiro(mensagem, minimo, maximo):
    while True:
        v=int(input(mensagem))
        if v >= minimo and v <= maximo:
            return v
        else:
            print("Você deve digitar um valor entre %d e %d" % (minimo, maximo))