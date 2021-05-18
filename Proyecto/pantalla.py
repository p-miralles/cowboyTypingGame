import pygame, os
pygame.font.init()

class Boton:
    font = pygame.font.SysFont('chilanka', 20)
    color = (0, 0, 0)
    posX, posY = (0, 0)
    ancho, alto = (0, 0)
    texto = ""

    def __init__(self, posX, posY, ancho, alto, texto):
        self.posX = posX
        self.posY = posY
        self.ancho = ancho
        self.alto = alto
        self.texto = texto


class AreaEntradaTexto:
    color = (0, 0, 0)
    posX = 0
    posY = 0
    alto = 0
    ancho = 0

    def __init__(self, color, posX, posY, ancho, alto):
        self.color = color
        self.posX = posX
        self.posY = posY
        self.ancho = ancho
        self.alto = alto

class Jugador():
    skin = ""
    posX = 0
    posY = 0
    ancho = 0
    alto = 0

    def __init__(self, skin, posX, posY, ancho, alto):
        self.skin = skin
        self.posX = posX
        self.posY = posY
        self.ancho = ancho
        self.alto = alto