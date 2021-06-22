import os

class Comparadores:
    # Comparador para modo 2 jugadores
    def compararOnline(numfrase, txtIngresadoFinal):
        with open(os.path.join('Assets', 'Frases.txt')) as frase:
            frase = frase.readlines()[numfrase]
        car = len(frase)
        ingreso = txtIngresadoFinal
        diferencias = 0
        for i in range(car - 1):
            # Si el ingreso es incorrecto en cuanto a la cantidad de carácteres sale Out of range.
            if frase[i] != ingreso[i]:
                diferencias = diferencias + 1
        porcentaje = (diferencias * 100) / car
        pres = (100 - (porcentaje))
        return pres
    # Comparador para modo práctica
    def compararSolo(numfrase, txtIngresadoFinal, cantborrados):
        with open(os.path.join('Assets', 'Frases.txt')) as frase:
            frase = frase.readlines()[numfrase]
        car = len(frase) - 1
        ingreso = txtIngresadoFinal
        diferencias = 0
        vecesBS=cantborrados
        if len(ingreso)< car:
            faltante = car - len(ingreso)
            for i in range(car - (faltante)):
                # Si el ingreso es incorrecto en cuanto a la cantidad de carácteres sale Out of range.
                if frase[i] != ingreso[i]:
                    diferencias = diferencias + 1
            diferencias = diferencias + faltante
        else:
            if len(ingreso)>car:
                sobrante = len(ingreso)-car
                for i in range(car):
                    # Si el ingreso es incorrecto en cuanto a la cantidad de carácteres sale Out of range.
                    if frase[i] != ingreso[i]:
                        diferencias = diferencias + 1
                diferencias = diferencias + sobrante
            else:
                for i in range(car):
                    # Si el ingreso es incorrecto en cuanto a la cantidad de carácteres sale Out of range.
                    if frase[i] != ingreso[i]:
                        diferencias = diferencias + 1
        porcentaje = (diferencias * 100) / car
        pres = (100 - porcentaje)
        puntaje=(100 - (porcentaje + vecesBS))
        return puntaje, pres