import pygame
import os
import math

import interfazGrafica
import Comparador

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
    font_frase = pygame.font.Font(os.path.join('Assets', 'PixelCowboy.ttf'), 20)
    n = 3

    areaEntrada = interfazGrafica.AreaEntradaTexto((191, 146, 42), 0, 400, ANCHOPANTALLA, ALTOPANTALLA // 4)
    areaEntradaRect = pygame.Rect(areaEntrada.posX, areaEntrada.posY, areaEntrada.ancho, areaEntrada.alto)
    font_txtIngresado = pygame.font.Font(os.path.join('Assets', 'PixelCowboy.ttf'), 25)
    font_txtIngresado2 = pygame.font.Font(os.path.join('Assets', 'PixelCowboy.ttf'), 25)

    txtIngresado = ""
    txtIngresado2 = ""
    txtIngresadoFinal = ""
    frases = ["Hola"]
    cantborrados = 0

    def mostrarFrase(self, numfrase):
        pygame.draw.rect(self.pantalla, (0,0,0), pygame.Rect(0, self.ALTOPANTALLA//3, self.ANCHOPANTALLA, 100))
        with open(os.path.join('Assets', 'Frases.txt')) as frase:
            frase = frase.read().splitlines()[numfrase]
            if len(frase)<101:
                texto_frase = self.font_txtIngresado.render(frase, True, (255, 255, 255))
                self.pantalla.blit(texto_frase, (15, self.ALTOPANTALLA // 2.7))
            else:
                if len(frase)<202:
                    frasemost=frase[0:101]
                    frasemost2=frase[101:202]
                    texto_frase = self.font_txtIngresado.render(frasemost, True, (255, 255, 255))
                    texto_frase2 = self.font_txtIngresado.render(frasemost2, True, (255, 255, 255))
                    self.pantalla.blit(texto_frase, (15, self.ALTOPANTALLA // 2.7))
                    self.pantalla.blit(texto_frase2, (15, self.ALTOPANTALLA // 2.3))
                else:
                    frasemost=frase [0:101]
                    frasemost2=frase[101:202]
                    frasemost3=frase[202:303]
                    texto_frase = self.font_frase.render(frasemost, True, (255, 255, 255))
                    texto_frase2 = self.font_frase.render(frasemost2, True, (255, 255, 255))
                    texto_frase3 = self.font_frase.render(frasemost3, True, (255, 255, 255))
                    self.pantalla.blit(texto_frase, (15, self.ALTOPANTALLA // 2.9))
                    self.pantalla.blit(texto_frase2, (15, self.ALTOPANTALLA // 2.5))
                    self.pantalla.blit(texto_frase3, (15, self.ALTOPANTALLA // 2.2))

    def ingresoDatos(self):

        pygame.draw.rect(self.pantalla, self.areaEntrada.color, self.areaEntradaRect)
        pygame.draw.rect(self.pantalla, (255, 255, 255), pygame.Rect(self.areaEntrada.posX, self.areaEntrada.posY, self.areaEntradaRect.width, self.areaEntradaRect.height//2))

        input = self.font_txtIngresado.render(self.txtIngresado, True, (0, 0, 0))
        input2 = self.font_txtIngresado.render(self.txtIngresado2, True, (0, 0, 0))
        self.pantalla.blit(input, (5, 400))
        self.pantalla.blit(input2, (5, 425))

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

    def pantallaResultados(self, puntaje, presicion):
        print (puntaje)
        print(presicion)
        pygame.draw.rect(self.pantalla, (230, 160, 70), pygame.Rect(0, self.ALTOPANTALLA // 4, self.ANCHOPANTALLA, 175))
        pygame.draw.rect(self.pantalla, (60, 40, 8), pygame.Rect(0, self.ALTOPANTALLA // 4, self.ANCHOPANTALLA, 5))
        pygame.draw.rect(self.pantalla, (60, 40, 8), pygame.Rect(0, self.ALTOPANTALLA // 1.67, self.ANCHOPANTALLA, 5))
        texto_titulo = self.font_cuenta_regresiva.render("Resultados:", True, (90, 50, 10))
        self.pantalla.blit(texto_titulo,(self.ANCHOPANTALLA/2.7, self.ALTOPANTALLA/3.8))
        texto_punt = self.font_txtIngresado.render("Puntaje: "+str(round(puntaje, 2))+"pts", True, (90, 50, 10))
        texto_pres = self.font_txtIngresado.render("Presición: "+str(round(presicion, 2))+"%", True, (90, 50, 10))
        self.pantalla.blit(texto_punt, (15, self.ALTOPANTALLA // 2.5))
        self.pantalla.blit(texto_pres, (700, self.ALTOPANTALLA // 2.5))
        texto_salida = self.font_txtIngresado.render("Presione ESC para salir.", True, (90, 50, 10))
        self.pantalla.blit(texto_salida, (self.ANCHOPANTALLA / 2.75, self.ALTOPANTALLA / 2))
        pygame.display.update()


    def pantallaResultadosOnline(self, presicion):
        pygame.draw.rect(self.pantalla, (230, 160, 70), pygame.Rect(0, self.ALTOPANTALLA // 4, self.ANCHOPANTALLA, 175))
        texto_titulo = self.font_cuenta_regresiva.render("Ganador: "+ "Jugador", True, (90, 50, 10))
        self.pantalla.blit(texto_titulo,(self.ANCHOPANTALLA/3.4, self.ALTOPANTALLA/3.8))
        texto_pres = self.font_txtIngresado.render("Presición: "+str(presicion)+"%", True, (90, 50, 10))
        texto_tiempo = self.font_txtIngresado.render("Tiempo: ", True, (90, 50, 10))
        self.pantalla.blit(texto_pres, (375, self.ALTOPANTALLA // 2.5))
        self.pantalla.blit(texto_tiempo, (375, self.ALTOPANTALLA // 2.2))
        pygame.display.update()

    def mostrarJuego(self, juno, jdos):
        self.pantalla.blit(self.fondo, (0, 0))
        pygame.draw.rect(self.pantalla, (0, 0, 0), juno)
        pygame.draw.rect(self.pantalla, (0, 0, 0), jdos)
        if self.n >= 0:
            self.cuentaRegresiva(self)
        else:
            self.ingresoDatos(self)
            self.mostrarFrase(self, 1)
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
    finaliza = False

    menu_p = MenuPrincipal
    pantalla_j = PantallaJuego

    #Bucle principal
    while True:
        mouse = pygame.mouse.get_pos()
        if mostrar_menu:
            MenuPrincipal.mostrarMenu(menu_p)
        elif finaliza:
            #pantalla_j.pantallaResultados(pantalla_j, puntaje, pres)
            pantalla_j.pantallaResultadosOnline(pantalla_j, pres)
        else:
            PantallaJuego.mostrarJuego(pantalla_j, JUNORect, JDOSRect)


        #Registro de eventos de usuario
        for event in pygame.event.get():
            if mostrar_menu:
                if interfazGrafica.Boton.colisionBotones(MenuPrincipal.BTN_EMPEZAR, mouse) and event.type == pygame.MOUSEBUTTONDOWN:
                    #SONIDO_DISPARO1.play()
                    mostrar_menu = False
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    quit()
                if event.key == pygame.K_BACKSPACE and len(pantalla_j.txtIngresado2) <= 0:
                    pantalla_j.txtIngresado = pantalla_j.txtIngresado[:-1]
                    pantalla_j.cantborrados = pantalla_j.cantborrados + 1
                elif event.key == pygame.K_BACKSPACE and len(pantalla_j.txtIngresado) >= 70:
                    pantalla_j.txtIngresado2 = pantalla_j.txtIngresado2[:-1]
                    pantalla_j.cantborrados = pantalla_j.cantborrados + 1
                else:
                    # print(len(pantalla_j.txtIngresado))
                    if len(pantalla_j.txtIngresado) < 70 and len(pantalla_j.txtIngresado2) <= 0 and event.key != pygame.K_RETURN:
                        pantalla_j.txtIngresado += event.unicode
                    elif event.key != pygame.K_RETURN:
                        pantalla_j.txtIngresado2 += event.unicode
                    pantalla_j.txtIngresadoFinal = pantalla_j.txtIngresado + pantalla_j.txtIngresado2
                if mostrar_menu == False:
                    if event.key == pygame.K_RETURN:
                        numfrase=1
                        puntaje, pres = (Comparador.Comparadores.compararSolo(numfrase, pantalla_j.txtIngresadoFinal, pantalla_j.cantborrados))
                        print (puntaje, pres)
                        finaliza = True
            if event.type == DISPARA_JUNO:
                SONIDO_DISPARO2.play()
            if event.type == DISPARA_JDOS:
                SONIDO_DISPARO2.play()
        reloj.tick(FPS)
if __name__ == "__main__":
    main()