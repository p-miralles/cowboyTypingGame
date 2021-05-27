import pygame
import os
pygame.font.init()

class Boton:
    font = pygame.font.SysFont('chilanka', 20)
    color = (0, 0, 0)
    posX, posY = (0, 0)
    ancho, alto = (0, 0)
    texto = ""
    rect = pygame.rect.Rect(posX, posY, ancho, alto)

    def __init__(self, posX, posY, ancho, alto, texto):
        self.posX = posX
        self.posY = posY
        self.ancho = ancho
        self.alto = alto
        self.texto = texto
        self.rect = pygame.rect.Rect(posX, posY, ancho, alto)

    def colisionBotones(self, mouse):
        if self.rect.collidepoint(mouse):
            self.color = (0, 0, 0)  # Negro
            return True
        else:
            self.color = (255, 255, 255)  # Blanco
            return False


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