class comparador:
    frase = open ("Frase prueba.txt")
    car = len(frase)
    ingreso = input ()
    diferencias = 0
    print (ingreso)
    for i in range(car):
        if frase[i] != ingreso[i]:
            diferencias= diferencias + 1
    print (diferencias)