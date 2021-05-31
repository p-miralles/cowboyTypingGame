import pygame
import os

import interfazGrafica

pygame.mixer.init()
pygame.font.init()

class MenuPrincipal:
    ANCHOPANTALLA, ALTOPANTALLA = 900, 500
    pantalla_menu = pygame.display.set_mode((ANCHOPANTALLA, ALTOPANTALLA))
    FONDO = pygame.image.load(os.path.join('Assets', 'menu_placeholder.jpg'))
    COLOR_FONDO = (183, 155, 106)
    BTN_EMPEZAR = interfazGrafica.Boton(ANCHOPANTALLA // 2 - 45, ALTOPANTALLA // 2, 120, 60, "EMPEZAR")
    TXT_BTN_EMPEZAR = BTN_EMPEZAR.font.render(BTN_EMPEZAR.texto, 1, COLOR_FONDO)

    def mostrarMenu(self):
        self.pantalla_menu.blit(self.FONDO, (0, 0))
        pygame.draw.rect(self.pantalla_menu, self.BTN_EMPEZAR.color, self.BTN_EMPEZAR.rect)
        self.pantalla_menu.blit(self.TXT_BTN_EMPEZAR, (
        self.BTN_EMPEZAR.rect.centerx - self.TXT_BTN_EMPEZAR.get_width() // 2, self.BTN_EMPEZAR.rect.centery - self.TXT_BTN_EMPEZAR.get_height() // 2))
        ###
        pygame.display.update()

class PantallaJuego:
    ANCHOPANTALLA, ALTOPANTALLA = 900, 500
    pantalla = pygame.display.set_mode((ANCHOPANTALLA, ALTOPANTALLA))
    fondo = pygame.image.load(os.path.join('Assets', 'fondo_placeholder.jpg'))

    font_cuenta_regresiva = pygame.font.Font(os.path.join('Assets', 'PixelCowboy.ttf'), 55)
    n = 3

    areaEntrada = interfazGrafica.AreaEntradaTexto((191, 146, 42), 0, 400, ANCHOPANTALLA, ALTOPANTALLA // 4)
    areaEntradaRect = pygame.Rect(areaEntrada.posX, areaEntrada.posY, areaEntrada.ancho, areaEntrada.alto)
    font_txtIngresado = pygame.font.Font(os.path.join('Assets', 'PixelCowboy.ttf'), 25)
    txtIngresado = ""
    frases = ["Hola"]

    def ingresoDatos(self):
        pygame.draw.rect(self.pantalla, self.areaEntrada.color, self.areaEntradaRect)
        pygame.draw.rect(self.pantalla, (255, 255, 255), pygame.Rect(self.areaEntrada.posX, self.areaEntrada.posY, self.areaEntradaRect.width, self.areaEntradaRect.height//2))
        input = self.font_txtIngresado.render(self.txtIngresado, True, (0, 0, 0))
        self.pantalla.blit(input, (5, 400))
        pygame.draw.rect(self.pantalla, (0, 0, 0), pygame.Rect(input.get_width() + 5, 405, 5, 20))

    def cuentaRegresiva(self):
        if self.n >= 0:
            if self.n == 0:
                texto_cuenta_regresiva = self.font_cuenta_regresiva.render("TYPE!", True, (0, 0, 0))
                self.pantalla.blit(texto_cuenta_regresiva,
                                   (self.ANCHOPANTALLA//2 - texto_cuenta_regresiva.get_width()//2, self.ALTOPANTALLA//3))
            else:
                texto_cuenta_regresiva = self.font_cuenta_regresiva.render(str(self.n), True, (0, 0, 0))
                self.pantalla.blit(texto_cuenta_regresiva, (self.ANCHOPANTALLA//2, self.ALTOPANTALLA//3))
        self.n -= 1
        pygame.display.update()
        pygame.time.wait(1000)


    def mostrarJuego(self, juno, jdos):
        self.pantalla.blit(self.fondo, (0, 0))
        pygame.draw.rect(self.pantalla, (0, 0, 0), juno)
        pygame.draw.rect(self.pantalla, (0, 0, 0), jdos)
        if self.n >= 0:
            self.cuentaRegresiva(self)
        else:
            self.ingresoDatos(self)
        ###
        pygame.display.update()

def main():
    #Constantes
    FPS = 60
    ANCHOPANTALLA, ALTOPANTALLA = 900, 500
    SONIDO_DISPARO1 = pygame.mixer.Sound(os.path.join('Assets', 'disparo.wav'))
    SONIDO_DISPARO2 = pygame.mixer.Sound(os.path.join('Assets', 'disparo-reverb.wav'))

    #Jugadores
    JUNO = interfazGrafica.Jugador("", 350, 340, 40, 60)
    JUNORect = pygame.Rect(JUNO.posX, JUNO.posY, JUNO.ancho, JUNO.alto)
    JDOS = interfazGrafica.Jugador("", 550, 30, 20, 30)
    JDOSRect = pygame.Rect(JDOS.posX, JDOS.posY, JDOS.ancho, JDOS.alto)

    #Eventos
    DISPARA_JUNO = pygame.USEREVENT + 1
    DISPARA_JDOS = pygame.USEREVENT + 2

    pygame.display.set_caption("Cowboy type!")
    reloj = pygame.time.Clock()
    mostrar_menu = True

    menu_p = MenuPrincipal
    pantalla_j = PantallaJuego

    #Bucle principal
    while True:
        mouse = pygame.mouse.get_pos()
        if mostrar_menu:
            MenuPrincipal.mostrarMenu(menu_p)
        else:
            PantallaJuego.mostrarJuego(pantalla_j, JUNORect, JDOSRect)

        #Registro de eventos de usuario
        for event in pygame.event.get():
            if mostrar_menu:
                if interfazGrafica.Boton.colisionBotones(MenuPrincipal.BTN_EMPEZAR, mouse) and event.type == pygame.MOUSEBUTTONDOWN:
                    SONIDO_DISPARO1.play()
                    mostrar_menu = False
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    pantalla_j.txtIngresado = pantalla_j.txtIngresado[:-1]
                else:
                    pantalla_j.txtIngresado += event.unicode
            if event.type == DISPARA_JUNO:
                SONIDO_DISPARO2.play()
            if event.type == DISPARA_JDOS:
                SONIDO_DISPARO2.play()
        reloj.tick(FPS)
if __name__ == "__main__":
    main()