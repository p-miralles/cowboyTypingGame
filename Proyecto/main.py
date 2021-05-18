import time

import pygame, os
import pantalla

pygame.mixer.init()
pygame.font.init()


def pantallaJuego(screen, anchoScreen, altoScreen, juno):
    fondo = pygame.image.load(os.path.join('Assets', 'fondo_placeholder.jpg'))
    screen.blit(fondo, (0, 0))
    areaEntrada = pantalla.AreaEntradaTexto((191, 146, 42), 0, 400, anchoScreen, altoScreen//4)
    areaEntradaRect = pygame.Rect(areaEntrada.posX, areaEntrada.posY, areaEntrada.ancho, areaEntrada.alto)
    pygame.draw.rect(screen, (areaEntrada.color), areaEntradaRect)
    pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(areaEntrada.posX, areaEntrada.posY, areaEntradaRect.width, areaEntradaRect.height//2))
    pygame.draw.rect(screen, (0, 0, 0), juno)
    pygame.display.update()

def mostrarMenu(screen, mouse, btnEmpezar, btnEmpezarRect):
    fondo = pygame.image.load(os.path.join('Assets', 'menu_placeholder.jpg'))
    COLOR_FONDO = (183, 155, 106)
    txtBtnEmpezar = btnEmpezar.font.render(btnEmpezar.texto, 1, COLOR_FONDO)
    if colisionBotones(btnEmpezarRect, mouse):
        btnEmpezar.color = (0, 0, 0)#Negro
    else:
        btnEmpezar.color = (255, 255, 255)#Blanco
    screen.blit(fondo, (0, 0))
    pygame.draw.rect(screen, btnEmpezar.color, btnEmpezarRect)
    screen.blit(txtBtnEmpezar, (btnEmpezarRect.centerx - txtBtnEmpezar.get_width()//2, btnEmpezarRect.centery - txtBtnEmpezar.get_height()//2))
    ###
    pygame.display.update()


EVENTO_COLISION = pygame.USEREVENT = 3
def colisionBotones(boton, mouse):
    if boton.collidepoint(mouse):
        try:
            pygame.event.post(pygame.event.Event(3, dict()))
            return True
        except:
            return True
    else:
        return False

def main():
    FPS = 60
    ANCHOPANTALLA, ALTOPANTALLA = 900, 500
    SCREEN = pygame.display.set_mode((ANCHOPANTALLA, ALTOPANTALLA))
    pygame.display.set_caption("Cowboy type!")
    SONIDO_DISPARO1 = pygame.mixer.Sound(os.path.join('Assets', 'disparo.wav'))
    SONIDO_DISPARO2 = pygame.mixer.Sound(os.path.join('Assets', 'disparo-reverb.wav'))

    POSX_JUNO, POSY_JUNO = 300, 340
    POSX_JDOS, POSY_JDOS = 650, 300
    JUNO = pygame.Rect(POSX_JUNO, POSY_JUNO, 40, 60)
    DISPARA_JUNO = pygame.USEREVENT = 1
    DISPARA_JDOS = pygame.USEREVENT = 2

    btnEmpezar = pantalla.Boton(ANCHOPANTALLA//2, ALTOPANTALLA//2, 120, 60, "EMPEZAR")
    btnEmpezarRect = pygame.Rect(btnEmpezar.posX-btnEmpezar.ancho+70, btnEmpezar.posY-btnEmpezar.alto+30, btnEmpezar.ancho, btnEmpezar.alto)

    reloj = pygame.time.Clock()
    run = True
    menu = True
    while run:
        mouse = pygame.mouse.get_pos()
        reloj.tick(FPS)
        if menu == True:
            mostrarMenu(SCREEN, mouse, btnEmpezar, btnEmpezarRect)
        else:
            pantallaJuego(SCREEN, ANCHOPANTALLA, ALTOPANTALLA, JUNO)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                quit()
            #if event.type == DISPARA_JUNO:
                #SONIDO_DISPARO.play()
            #if event.type == DISPARA_JDOS:
                #SONIDO_DISPARO.play()
            if colisionBotones(btnEmpezarRect, mouse) and event.type == pygame.MOUSEBUTTONDOWN:
                SONIDO_DISPARO1.play()
                time.sleep(0.25)
                menu = False

if __name__ == "__main__":
    main()