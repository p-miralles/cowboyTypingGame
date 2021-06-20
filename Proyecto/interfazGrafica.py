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