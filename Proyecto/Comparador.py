class comparador:
    frase = "Dios creó a todos los hombres. Samuel Colt los hizo iguales."
    car = len(frase)
    ingreso = input ()
    diferencias = 0
    print (ingreso)
    for i in range(car):
        if frase[i] != ingreso[i]:
            diferencias= diferencias + 1
    porcentaje = (diferencias*100)/car
    print (porcentaje, "%")