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