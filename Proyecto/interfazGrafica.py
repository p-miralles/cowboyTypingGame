import pygame
from pygame import Rect
import os
pygame.font.init()

class Boton:
    color = (106, 68, 1)
    colortxt = (0, 0, 0)
    posX, posY = (0, 0)
    ancho, alto = (0, 0)
    txt = ""
    tamanoFont = 20
    font = pygame.font.SysFont('chilanka', tamanoFont)
    rect = Rect(posX, posY, ancho, alto)

    def __init__(self, posX, posY, ancho, alto, txt, tamanoFont):
        self.posX = posX
        self.posY = posY
        self.ancho = ancho
        self.alto = alto
        self.txt = txt
        self.tamanoFont = tamanoFont
        self.font = pygame.font.SysFont('chilanka', tamanoFont)
        self.rect = Rect(posX, posY, ancho, alto)

    def colisionBotones(self, mouse):
        if self.rect.collidepoint(mouse):
            self.color = (97, 97, 97)  # Gris
            self.colortxt = (0,0,0)
            return True
        else:
            self.color = (106, 68, 1)  # Marrón Claro
            self.colortxt = (218, 218, 218)
            return False

    def mostrarBoton(self, pantalla):
        pygame.draw.rect(pantalla, self.color, self.rect)
        surface = self.font.render(self.txt, True, self.colortxt)
        pantalla.blit(surface, (self.rect.centerx-surface.get_width()//2 , self.rect.centery-surface.get_height()//2))

class AreaEntradaTexto:
    color = (0, 0, 0)
    posX = 0
    posY = 0
    ancho = 0
    alto = 0

    def __init__(self, color, posX, posY, ancho, alto):
        self.color = color
        self.posX = posX
        self.posY = posY
        self.ancho = ancho
        self.alto = alto

class Texto:
    texto = ""
    color = (0, 0, 0)
    posX = 0
    posY = 0
    font = pygame.font.Font(os.path.join('Assets', 'PixelCowboy.ttf'), 25)
    surface = font.render(texto, True, color)

    def __init__(self, texto, color, posX, posY):
        self.texto = texto
        self.color = color
        self.posX = posX
        self.posY = posY

    def mostrarTexto(self, pantalla):
        self.surface = self.font.render(self.texto, True, self.color)
        pantalla.blit(self.surface, (self.posX, self.posY))
        if self.surface.get_width() > pantalla.get_width():
            self.posX = -20
        else:
            self.posX = +20
        pygame.draw.rect(pantalla, (0, 0, 0), pygame.Rect(self.surface.get_width() + 5, 410, 5, 20))


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