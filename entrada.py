def valida_inteiro(menagem, minimo, maximo):
    while True:
        try:
            v = int(input(menagem))
            if v >= minimo and v <= maximo:
                return v
            else:
                print("Digite um valor entre {minimo} e {maximo}")
        except ValueError:
            print("Você deve digitar um numero inteiro")