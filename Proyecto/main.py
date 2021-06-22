import pygame
from pygame import Rect
import os

import interfazGrafica

pygame.mixer.init()
pygame.font.init()

class MenuOnline:
    ANCHOPANTALLA, ALTOPANTALLA = 900, 500
    pantalla_menu_online = pygame.display.set_mode((ANCHOPANTALLA, ALTOPANTALLA))
    COLOR_FONDO = (183, 155, 106)
    font_titulo = pygame.font.Font(os.path.join('Assets', 'PixelCowboy.ttf'), 55)
    font_cuerpo = pygame.font.Font(os.path.join('Assets', 'PixelCowboy.ttf'), 20)

    btn_volver = interfazGrafica.Boton(10, 430, 100, 50, "VOLVER", 20)
    btn_host = interfazGrafica.Boton(ANCHOPANTALLA//2-45, ALTOPANTALLA//3, 100, 60, "HOST", 20)

    btn_unirse1 = interfazGrafica.Boton(ANCHOPANTALLA//2-255, ALTOPANTALLA//2+120, 80, 40, "SERVER 1", 15)
    btn_unirse2 = interfazGrafica.Boton(ANCHOPANTALLA//2-145, ALTOPANTALLA//2+120, 80, 40, "SERVER 2", 15)
    btn_unirse3 = interfazGrafica.Boton(ANCHOPANTALLA//2-40,ALTOPANTALLA//2+120, 80, 40, "SERVER 3", 15)
    btn_unirse4 = interfazGrafica.Boton(ANCHOPANTALLA//2+65,ALTOPANTALLA//2+120, 80, 40, "SERVER 4", 15)
    btn_unirse5 = interfazGrafica.Boton(ANCHOPANTALLA//2+175,ALTOPANTALLA//2+120, 80, 40, "SERVER 5", 15)

    def mostrarMenuOnline(self):
        self.pantalla_menu_online.fill(self.COLOR_FONDO)
        self.pantalla_menu_online.blit(self.font_titulo.render("JUGAR ONLINE", True, (0,0,0)), (10, 10))
        pygame.draw.line(self.pantalla_menu_online, (0,0,0), (150,self.ALTOPANTALLA//2),(self.ANCHOPANTALLA-150, self.ALTOPANTALLA//2), 2)

        interfazGrafica.Boton.mostrarBoton(self.btn_volver, self.pantalla_menu_online)
        interfazGrafica.Boton.mostrarBoton(self.btn_host, self.pantalla_menu_online)

        pygame.draw.rect(self.pantalla_menu_online, (0,0,0), Rect(self.ANCHOPANTALLA//4-50, self.ALTOPANTALLA//2+20, 550, 160))
        pygame.draw.rect(self.pantalla_menu_online, (180, 180, 180), Rect(self.ANCHOPANTALLA//4-45,self.ALTOPANTALLA//2+25, 540, 150))

        interfazGrafica.Boton.mostrarBoton(self.btn_unirse1, self.pantalla_menu_online)
        pygame.draw.circle(self.pantalla_menu_online, (0,95,0), (self.btn_unirse1.rect.centerx, self.btn_unirse1.rect.centery-40),10)
        pygame.draw.line(self.pantalla_menu_online,(0,0,0),(290,270),(290,425),2)
        interfazGrafica.Boton.mostrarBoton(self.btn_unirse2, self.pantalla_menu_online)
        pygame.draw.circle(self.pantalla_menu_online, (95, 0, 0),(self.btn_unirse2.rect.centerx, self.btn_unirse2.rect.centery - 40), 10)
        pygame.draw.line(self.pantalla_menu_online, (0, 0, 0), (395, 270), (395, 425), 2)
        interfazGrafica.Boton.mostrarBoton(self.btn_unirse3, self.pantalla_menu_online)
        pygame.draw.circle(self.pantalla_menu_online, (95, 0, 0),(self.btn_unirse3.rect.centerx, self.btn_unirse3.rect.centery - 40), 10)
        pygame.draw.line(self.pantalla_menu_online, (0, 0, 0), (500, 270), (500, 425), 2)
        interfazGrafica.Boton.mostrarBoton(self.btn_unirse4, self.pantalla_menu_online)
        pygame.draw.circle(self.pantalla_menu_online, (95, 0, 0),(self.btn_unirse4.rect.centerx, self.btn_unirse4.rect.centery - 40), 10)
        pygame.draw.line(self.pantalla_menu_online, (0, 0, 0), (610, 270), (610, 425), 2)
        interfazGrafica.Boton.mostrarBoton(self.btn_unirse5, self.pantalla_menu_online)
        pygame.draw.circle(self.pantalla_menu_online, (95, 0, 0),(self.btn_unirse5.rect.centerx, self.btn_unirse5.rect.centery - 40), 10)

        pygame.display.update()


class MenuPrincipal:
    ANCHOPANTALLA, ALTOPANTALLA = 900, 500
    pantalla_menu = pygame.display.set_mode((ANCHOPANTALLA, ALTOPANTALLA))
    FONDO = pygame.image.load(os.path.join('Assets', 'menu_placeholder.jpg'))
    COLOR_FONDO = (183, 155, 106)
    btn_solo = interfazGrafica.Boton(ANCHOPANTALLA // 2 - 45, ALTOPANTALLA // 2, 120, 60, "SOLO", 20)
    btn_online = interfazGrafica.Boton(ANCHOPANTALLA//2-45, ALTOPANTALLA//3, 120, 60, "ONLINE", 20)

    def mostrarMenu(self):
        self.pantalla_menu.blit(self.FONDO, (0, 0))

        interfazGrafica.Boton.mostrarBoton(self.btn_online, self.pantalla_menu)
        interfazGrafica.Boton.mostrarBoton(self.btn_solo, self.pantalla_menu)

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
    font_txtIngresado = pygame.font.Font(os.path.join('Assets', 'PixelCowboy.ttf'), 23)
    font_txtIngresado2 = pygame.font.Font(os.path.join('Assets', 'PixelCowboy.ttf'), 23)

    txtIngresado = ""
    txtIngresado2 = ""
    txtIngresadoFinal = ""

    input = font_txtIngresado.render(txtIngresado, True, (0, 0, 0))
    input2 = font_txtIngresado.render(txtIngresado2, True, (0, 0, 0))

    frases = ["Hola"]

    def ingresoDatos(self):
        pygame.draw.rect(self.pantalla, self.areaEntrada.color, self.areaEntradaRect)
        pygame.draw.rect(self.pantalla, (255, 255, 255), pygame.Rect(self.areaEntrada.posX, self.areaEntrada.posY, self.areaEntradaRect.width, self.areaEntradaRect.height//2))

        input = self.font_txtIngresado.render(self.txtIngresado, True, (0, 0, 0))
        input2 = self.font_txtIngresado.render(self.txtIngresado2, True, (0, 0, 0))
        self.input = input
        self.input2 = input2
        self.pantalla.blit(input, (5, 400))
        self.pantalla.blit(input2, (5, 425))

        if(input.get_width()<=self.pantalla.get_width()-10):
            pygame.draw.rect(self.pantalla, (0, 0, 0), pygame.Rect(input.get_width() + 5, 405, 5, 20))
        elif(input.get_width()>self.pantalla.get_width()-10):
            pygame.draw.rect(self.pantalla, (0, 0, 0), pygame.Rect(input2.get_width() + 5, 430, 5, 20))

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
    SONIDO_DISPARO1 = pygame.mixer.Sound(os.path.join('Assets', 'disparo1.wav'))
    SONIDO_DISPARO2 = pygame.mixer.Sound(os.path.join('Assets', 'disparo2.wav'))
    SONIDO_SALIR = pygame.mixer.Sound(os.path.join('Assets', 'salir.wav'))

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
    pygame.key.set_repeat(100, 100)

    mostrar_menu = True
    mostrar_menu_online = False

    pantalla_j = PantallaJuego

    #Bucle principal
    while True:
        mouse = pygame.mouse.get_pos()
        if mostrar_menu:
            menu_p = MenuPrincipal
            MenuPrincipal.mostrarMenu(menu_p)
        elif mostrar_menu_online:
            menu_online = MenuOnline
            MenuOnline.mostrarMenuOnline(menu_online)
        else:
            PantallaJuego.mostrarJuego(pantalla_j, JUNORect, JDOSRect)

        #Registro de eventos de usuario
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if mostrar_menu:
                if interfazGrafica.Boton.colisionBotones(MenuPrincipal.btn_solo, mouse) and event.type == pygame.MOUSEBUTTONDOWN:
                    #SONIDO_DISPARO1.play()
                    mostrar_menu = False
                if interfazGrafica.Boton.colisionBotones(MenuPrincipal.btn_online, mouse) and event.type == pygame.MOUSEBUTTONDOWN:
                    #SONIDO_DISPARO2.play()
                    mostrar_menu = False
                    mostrar_menu_online = True
            if mostrar_menu_online:
                if interfazGrafica.Boton.colisionBotones(MenuOnline.btn_host, mouse) and event.type == pygame.MOUSEBUTTONDOWN:
                    print("Hostear servidor")
                if interfazGrafica.Boton.colisionBotones(MenuOnline.btn_unirse1, mouse) and event.type == pygame.MOUSEBUTTONDOWN:
                    print("Unirse a servidor UNO")
                if interfazGrafica.Boton.colisionBotones(MenuOnline.btn_volver, mouse) and event.type == pygame.MOUSEBUTTONDOWN:
                    mostrar_menu_online = False
                    mostrar_menu = True
            if mostrar_menu==False and mostrar_menu_online==False:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE and pantalla_j.input2.get_width()==1:
                        pantalla_j.txtIngresado = pantalla_j.txtIngresado[:-1]
                    elif event.key == pygame.K_BACKSPACE and pantalla_j.input.get_width()>=pantalla_j.pantalla.get_width()-10:
                        pantalla_j.txtIngresado2 = pantalla_j.txtIngresado2[:-1]
                    else:
                        #print(len(pantalla_j.txtIngresado))
                        if pantalla_j.input.get_width() < pantalla_j.pantalla.get_width()-10:
                            pantalla_j.txtIngresado += event.unicode
                        else:
                            if pantalla_j.input2.get_width()<=pantalla_j.pantalla.get_width()-20:
                                pantalla_j.txtIngresado2 += event.unicode
                        pantalla_j.txtIngresadoFinal = pantalla_j.txtIngresado + pantalla_j.txtIngresado2
                if event.type == DISPARA_JUNO:
                    SONIDO_DISPARO1.play()
                if event.type == DISPARA_JDOS:
                    SONIDO_DISPARO2.play()
        reloj.tick(FPS)
if __name__ == "__main__":
    main()