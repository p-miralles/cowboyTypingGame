import random

import pygame
from pygame import Rect
import os
import time

import interfazGrafica
import Comparador

pygame.mixer.init()
pygame.font.init()
numfrase= random.randint(0, 12)
class MenuOnline:
    ANCHOPANTALLA, ALTOPANTALLA = 900, 500
    pantalla_menu_online = pygame.display.set_mode((ANCHOPANTALLA, ALTOPANTALLA))
    COLOR_FONDO = (183, 155, 106)
    font_titulo = pygame.font.Font(os.path.join('Assets', 'PixelCowboy.ttf'), 55)
    font_cuerpo = pygame.font.Font(os.path.join('Assets', 'PixelCowboy.ttf'), 30)

    btn_volver = interfazGrafica.Boton(10, 430, 100, 50, "VOLVER", 20)
    btn_host = interfazGrafica.Boton(ANCHOPANTALLA//2-45, ALTOPANTALLA//5, 100, 60, "HOST", 20)
    entradaNombreSala = interfazGrafica.AreaEntradaTexto((255,255,255), ANCHOPANTALLA//3, ALTOPANTALLA//3, 300, 30)

    btn_unirse1 = interfazGrafica.Boton(ANCHOPANTALLA//2-255, ALTOPANTALLA//2+120, 80, 40, "SERVER 1", 15)
    btn_unirse2 = interfazGrafica.Boton(ANCHOPANTALLA//2-145, ALTOPANTALLA//2+120, 80, 40, "SERVER 2", 15)
    btn_unirse3 = interfazGrafica.Boton(ANCHOPANTALLA//2-40,ALTOPANTALLA//2+120, 80, 40, "SERVER 3", 15)
    btn_unirse4 = interfazGrafica.Boton(ANCHOPANTALLA//2+65,ALTOPANTALLA//2+120, 80, 40, "SERVER 4", 15)
    btn_unirse5 = interfazGrafica.Boton(ANCHOPANTALLA//2+175,ALTOPANTALLA//2+120, 80, 40, "SERVER 5", 15)

    btn_listo = interfazGrafica.Boton(ANCHOPANTALLA-110, 430, 100, 60, "LISTO", 20)
    marcador_listo = interfazGrafica.Linea((90,0,0), btn_listo.rect.centerx+49, btn_listo.rect.centery+20, btn_listo.rect.centerx-50, btn_listo.rect.centery+20, 7)
    btn_empezar = interfazGrafica.Boton(ANCHOPANTALLA-110, 350, 100, 50, "EMPEZAR", 20)
    listo = False

    def mostrarMenuOnline(self):
        self.pantalla_menu_online.fill(self.COLOR_FONDO)
        self.pantalla_menu_online.blit(self.font_titulo.render("JUGAR ONLINE", True, (0,0,0)), (10, 10))
        pygame.draw.line(self.pantalla_menu_online, (0,0,0), (150,self.ALTOPANTALLA//2),(self.ANCHOPANTALLA-150, self.ALTOPANTALLA//2), 2)

        interfazGrafica.Boton.mostrarBoton(self.btn_volver, self.pantalla_menu_online)
        interfazGrafica.Boton.mostrarBoton(self.btn_host, self.pantalla_menu_online)
        pygame.draw.rect(self.pantalla_menu_online, self.entradaNombreSala.color, self.entradaNombreSala.rect)
        self.entradaNombreSala.surface = self.entradaNombreSala.font.render(self.entradaNombreSala.txt, True, (0,0,0))
        self.pantalla_menu_online.blit(self.entradaNombreSala.surface, (self.entradaNombreSala.posX, self.entradaNombreSala.posY+5))

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
        ###
        pygame.display.update()

    def hostearSala(self):
        self.pantalla_menu_online = pygame.display.set_mode((self.ANCHOPANTALLA, self.ALTOPANTALLA))
        self.pantalla_menu_online.fill(self.COLOR_FONDO)
        pygame.draw.rect(self.pantalla_menu_online, (255, 160, 70), Rect(0,0,self.ANCHOPANTALLA, 90))
        self.pantalla_menu_online.blit(self.font_titulo.render("Servidor: " + self.entradaNombreSala.txt, True, (0, 0, 0)), (10, 10))
        self.pantalla_menu_online.blit(self.font_cuerpo.render("Esperando al inicio de partida", True, (80, 0, 0)), (self.ANCHOPANTALLA//2-180, self.ALTOPANTALLA//2))
        interfazGrafica.Boton.mostrarBoton(self.btn_volver, self.pantalla_menu_online)
        interfazGrafica.Boton.mostrarBoton(self.btn_listo, self.pantalla_menu_online)
        if self.listo:
            MenuOnline.marcador_listo.color = (0, 90, 0)
        else:
            MenuOnline.marcador_listo.color = (90, 0, 0)
        pygame.draw.line(self.pantalla_menu_online, self.marcador_listo.color, (self.marcador_listo.startX, self.marcador_listo.startY),
                         (self.marcador_listo.endX, self.marcador_listo.endY), self.marcador_listo.ancho)
        interfazGrafica.Boton.mostrarBoton(self.btn_empezar, self.pantalla_menu_online)
        pygame.display.update()

class MenuPrincipal:
    ANCHOPANTALLA, ALTOPANTALLA = 900, 500
    pantalla_menu = pygame.display.set_mode((ANCHOPANTALLA, ALTOPANTALLA))
    FONDO = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'menuPrincipal.png')), (900,500))
    COLOR_FONDO = (183, 155, 106)
    font_titulo = pygame.font.Font(os.path.join('Assets', 'PixelCowboy.ttf'), 60)
    font_cuerpo = pygame.font.Font(os.path.join('Assets', 'PixelCowboy.ttf'), 32)
    btn_solo = interfazGrafica.Boton(ANCHOPANTALLA // 2 - 45, ALTOPANTALLA // 2, 120, 60, "SOLO", 20)
    btn_online = interfazGrafica.Boton(ANCHOPANTALLA//2-45, ALTOPANTALLA//3, 120, 60, "ONLINE", 20)

    def mostrarMenu(self):
        self.pantalla_menu.blit(self.FONDO, (0, 0))
        self.pantalla_menu.blit(self.font_titulo.render("COWBOY TYPE!", True, (0,0,0)), (self.ANCHOPANTALLA//2-180,10))

        interfazGrafica.Boton.mostrarBoton(self.btn_online, self.pantalla_menu)
        interfazGrafica.Boton.mostrarBoton(self.btn_solo, self.pantalla_menu)
        self.pantalla_menu.blit(self.font_cuerpo.render("Presione 'ESC' para salir en cualquier momento", True,
                                                        (250, 30, 50)),(self.ANCHOPANTALLA//2-310, self.ALTOPANTALLA-100))

        ###
        pygame.display.update()

class PantallaJuego:
    ANCHOPANTALLA, ALTOPANTALLA = 900, 500
    pantalla = pygame.display.set_mode((ANCHOPANTALLA, ALTOPANTALLA))
    escenario = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'escenario.png')), (900,500))
    font_cuenta_regresiva = pygame.font.Font(os.path.join('Assets', 'PixelCowboy.ttf'), 55)
    skinJuno = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'skin1.png')), (150,200))
    skinJdos = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'skin1.png')), (70,100))
    sonido_reloj = pygame.mixer.Sound(os.path.join('Assets', 'reloj.wav'))
    sonido_campana = pygame.mixer.Sound(os.path.join('Assets', 'campana.wav'))

    areaEntrada = interfazGrafica.AreaEntradaTexto((60, 40, 8), 0, 400, ANCHOPANTALLA, ALTOPANTALLA // 4)
    areaEntradaRect = pygame.Rect(areaEntrada.posX, areaEntrada.posY, areaEntrada.ancho, areaEntrada.alto)

    font_txtIngresado = pygame.font.Font(os.path.join('Assets', 'PixelCowboy.ttf'), 23)
    font_txtIngresado2 = pygame.font.Font(os.path.join('Assets', 'PixelCowboy.ttf'), 23)
    font_frasemostrada = pygame.font.Font(os.path.join('Assets', 'PixelCowboy.ttf'), 22)

    n = 3
    txtIngresado = ""
    txtIngresado2 = ""
    txtIngresadoFinal = ""

    input = font_txtIngresado.render(txtIngresado, True, (0, 0, 0))
    input2 = font_txtIngresado.render(txtIngresado2, True, (0, 0, 0))
    cantborrados=0
    surfFrase = pygame.Surface((ANCHOPANTALLA, 100))
    surfFrase.fill((0, 0, 0))
    surfFrase.set_alpha(200)

    def mostrarFrase(self, numfrase):
        self.pantalla.blit(self.surfFrase, (0, self.ALTOPANTALLA//3))
        with open(os.path.join('Assets', 'Frases.txt')) as frase:
            frase = frase.read().splitlines()[numfrase]
            if len(frase) < 101:
                texto_frase = self.font_frasemostrada.render(frase, True, (255, 255, 255))
                self.pantalla.blit(texto_frase, (10, self.ALTOPANTALLA // 2.7))
            else:
                if len(frase) < 202:
                    frasemost = frase[0:101]
                    frasemost2 = frase[101:202]
                    texto_frase = self.font_frasemostrada.render(frasemost, True, (255, 255, 255))
                    texto_frase2 = self.font_frasemostrada.render(frasemost2, True, (255, 255, 255))
                    self.pantalla.blit(texto_frase, (10, self.ALTOPANTALLA // 2.7))
                    self.pantalla.blit(texto_frase2, (10, self.ALTOPANTALLA // 2.3))
                else:
                    frasemost = frase[0:101]
                    frasemost2 = frase[101:202]
                    frasemost3 = frase[202:303]
                    texto_frase = self.font_frasemostrada.render(frasemost, True, (255, 255, 255))
                    texto_frase2 = self.font_frasemostrada.render(frasemost2, True, (255, 255, 255))
                    texto_frase3 = self.font_frasemostrada.render(frasemost3, True, (255, 255, 255))
                    self.pantalla.blit(texto_frase, (10, self.ALTOPANTALLA // 2.9))
                    self.pantalla.blit(texto_frase2, (10, self.ALTOPANTALLA // 2.5))
                    self.pantalla.blit(texto_frase3, (10, self.ALTOPANTALLA // 2.2))

    def ingresoDatos(self):
        pygame.draw.rect(self.pantalla, self.areaEntrada.color, self.areaEntradaRect)
        pygame.draw.rect(self.pantalla, (255, 255, 255), pygame.Rect(self.areaEntrada.posX, self.areaEntrada.posY, self.areaEntradaRect.width, self.areaEntradaRect.height//2))
        pygame.draw.line(self.pantalla, (10, 10, 10), (0, self.areaEntrada.posY+60),(self.ANCHOPANTALLA, self.areaEntrada.posY+60), 3)
        pygame.draw.line(self.pantalla, (10,10,10), (0,self.areaEntrada.posY),(self.ANCHOPANTALLA,self.areaEntrada.posY),5)

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
                self.sonido_campana.play()
                texto_cuenta_regresiva = self.font_cuenta_regresiva.render("TYPE!", True, (0, 0, 0))
                self.pantalla.blit(texto_cuenta_regresiva,
                                   (self.ANCHOPANTALLA//2 - texto_cuenta_regresiva.get_width()//2, self.ALTOPANTALLA//3))
            else:
                self.sonido_reloj.play()
                texto_cuenta_regresiva = self.font_cuenta_regresiva.render(str(self.n), True, (0, 0, 0))
                self.pantalla.blit(texto_cuenta_regresiva, (self.ANCHOPANTALLA//2, self.ALTOPANTALLA//3))
        self.n -= 1
        pygame.display.update()
        pygame.time.wait(1000)

    def pantallaResultados(self, puntaje, presicion, tiempo_fin, tiempo_inicio):
        tiempo = tiempo_fin - tiempo_inicio
        pygame.draw.rect(self.pantalla, (230, 160, 70), pygame.Rect(0, self.ALTOPANTALLA // 4, self.ANCHOPANTALLA, 175))
        pygame.draw.rect(self.pantalla, (60, 40, 8), pygame.Rect(0, self.ALTOPANTALLA // 4, self.ANCHOPANTALLA, 5))
        pygame.draw.rect(self.pantalla, (60, 40, 8), pygame.Rect(0, self.ALTOPANTALLA // 1.67, self.ANCHOPANTALLA, 5))
        texto_titulo = self.font_cuenta_regresiva.render("Resultados:", True, (90, 50, 10))
        self.pantalla.blit(texto_titulo, (self.ANCHOPANTALLA / 2.7, self.ALTOPANTALLA / 3.8))
        texto_punt = self.font_txtIngresado.render("Puntaje: " + str(round(puntaje, 2)) + "pts", True, (90, 50, 10))
        texto_pres = self.font_txtIngresado.render("Precisión: " + str(round(presicion, 2)) + "%", True, (90, 50, 10))
        texto_tiempo = self.font_txtIngresado.render("Tiempo: " + str(round(tiempo, 2)) + " Secs", True, (90, 50, 10))
        self.pantalla.blit(texto_punt, (15, self.ALTOPANTALLA // 2.5))
        self.pantalla.blit(texto_pres, (700, self.ALTOPANTALLA // 2.5))
        self.pantalla.blit(texto_tiempo, (370, self.ALTOPANTALLA // 2.5))
        texto_salida = self.font_txtIngresado.render("Presione ESC para salir.", True, (90, 50, 10))
        self.pantalla.blit(texto_salida, (self.ANCHOPANTALLA // 2.75, self.ALTOPANTALLA / 2))
        pygame.display.update()

    def pantallaResultadosOnline(self, presicion, tiempo_fin, tiempo_inicio):
        tiempo = tiempo_fin - tiempo_inicio
        pygame.draw.rect(self.pantalla, (230, 160, 70), pygame.Rect(0, self.ALTOPANTALLA // 4, self.ANCHOPANTALLA, 175))
        texto_titulo = self.font_cuenta_regresiva.render("Ganador: " + "Jugador", True, (90, 50, 10))
        self.pantalla.blit(texto_titulo, (self.ANCHOPANTALLA / 3.4, self.ALTOPANTALLA / 3.8))
        texto_pres = self.font_txtIngresado.render("Precisión: " + str(presicion) + "%", True, (90, 50, 10))
        texto_tiempo = self.font_txtIngresado.render("Tiempo: " + str(round(tiempo, 2)), True, (90, 50, 10))
        self.pantalla.blit(texto_pres, (375, self.ALTOPANTALLA // 2.5))
        self.pantalla.blit(texto_tiempo, (375, self.ALTOPANTALLA // 2.2))
        texto_salida = self.font_txtIngresado.render("Presione ESC para salir.", True, (90, 50, 10))
        self.pantalla.blit(texto_salida, (self.ANCHOPANTALLA / 2.75, self.ALTOPANTALLA / 2))
        pygame.display.update()

    def mostrarJuego(self):
        self.pantalla.blit(self.escenario, (0, 0))
        self.pantalla.blit(self.skinJuno, (310, 250))
        self.pantalla.blit(self.skinJdos, (760, 10))

        if self.n >= 0:
            self.cuentaRegresiva(self)
        else:
            self.ingresoDatos(self)
            self.mostrarFrase(self, numfrase)
        ###
        pygame.display.update()

def main():
    #Constantes
    FPS = 60
    ANCHOPANTALLA, ALTOPANTALLA = 900, 500
    SONIDO_DISPARO1 = pygame.mixer.Sound(os.path.join('Assets', 'disparo1.wav'))
    SONIDO_DISPARO2 = pygame.mixer.Sound(os.path.join('Assets', 'disparo2.wav'))
    SONIDO_DISPARO2.set_volume(80)
    SONIDO_SALIR = pygame.mixer.Sound(os.path.join('Assets', 'salir.wav'))

    #Eventos
    DISPARA_JUNO = pygame.USEREVENT + 1
    DISPARA_JDOS = pygame.USEREVENT + 2

    pygame.display.set_caption("Cowboy type!")
    reloj = pygame.time.Clock()
    pygame.key.set_repeat(100, 100)

    mostrar_menu = True
    mostrar_menu_online = False
    mostrar_juego = False
    mostrar_sala = False
    finaliza = False

    #Bucle principal
    while True:
        mouse = pygame.mouse.get_pos()
        if finaliza:
            pantalla_j.pantallaResultados(pantalla_j, puntaje, pres, tiempo_fin, tiempo_inicio)
            mostrar_juego=False
        if mostrar_menu:
            menu_p = MenuPrincipal
            MenuPrincipal.mostrarMenu(menu_p)
        elif mostrar_menu_online:
            menu_online = MenuOnline
            MenuOnline.mostrarMenuOnline(menu_online)
        elif mostrar_juego:
            pygame.mouse.set_visible(False)
            pantalla_j = PantallaJuego
            PantallaJuego.mostrarJuego(pantalla_j)

        #Registro de eventos de usuario
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    quit()
            if mostrar_menu:
                if interfazGrafica.Boton.colisionBotones(MenuPrincipal.btn_solo, mouse) and event.type == pygame.MOUSEBUTTONDOWN:
                    #SONIDO_DISPARO1.play()
                    mostrar_menu = False
                    tiempo_inicio = (time.time() + 4)
                    mostrar_juego = True
                if interfazGrafica.Boton.colisionBotones(MenuPrincipal.btn_online, mouse) and event.type == pygame.MOUSEBUTTONDOWN:
                    #SONIDO_DISPARO2.play()
                    mostrar_menu = False
                    mostrar_menu_online = True
            if mostrar_menu_online:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        MenuOnline.entradaNombreSala.txt = MenuOnline.entradaNombreSala.txt[:-1]
                    elif menu_online.entradaNombreSala.surface.get_width()<menu_online.entradaNombreSala.rect.width-5:
                        MenuOnline.entradaNombreSala.txt += event.unicode
                if interfazGrafica.Boton.colisionBotones(MenuOnline.btn_host, mouse) and event.type == pygame.MOUSEBUTTONDOWN:
                    if MenuOnline.entradaNombreSala.txt!="":
                        print("Hostear servidor")
                        mostrar_menu_online = False
                        tiempo_inicio = (time.time() + 4)
                        mostrar_sala = True
                    else:
                        print("El nombre del server no puede estar vacío!")
                if interfazGrafica.Boton.colisionBotones(MenuOnline.btn_unirse1, mouse) and event.type == pygame.MOUSEBUTTONDOWN:
                    print("Unirse a servidor UNO")
                if interfazGrafica.Boton.colisionBotones(MenuOnline.btn_volver, mouse) and event.type == pygame.MOUSEBUTTONDOWN:
                    MenuOnline.entradaNombreSala.txt = ""
                    mostrar_menu_online = False
                    mostrar_sala = False
                    mostrar_menu = True
            if mostrar_sala:
                MenuOnline.hostearSala(MenuOnline)
                if interfazGrafica.Boton.colisionBotones(MenuOnline.btn_volver, mouse) and event.type == pygame.MOUSEBUTTONDOWN:
                    MenuOnline.listo = False
                    mostrar_sala = False
                    mostrar_menu_online = True
                if interfazGrafica.Boton.colisionBotones(MenuOnline.btn_listo, mouse) and event.type == pygame.MOUSEBUTTONDOWN:
                    if MenuOnline.listo==False:
                        MenuOnline.listo = True
                    elif MenuOnline.listo:
                        MenuOnline.listo = False
            if mostrar_juego:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        quit()
                    if event.key == pygame.K_BACKSPACE and pantalla_j.input2.get_width()==1:
                        pantalla_j.txtIngresado = pantalla_j.txtIngresado[:-1]
                        pantalla_j.cantborrados = pantalla_j.cantborrados + 1
                    elif event.key == pygame.K_BACKSPACE and pantalla_j.input.get_width()>=pantalla_j.pantalla.get_width()-10:
                        pantalla_j.txtIngresado2 = pantalla_j.txtIngresado2[:-1]
                        pantalla_j.cantborrados = pantalla_j.cantborrados + 1
                    else:
                        if pantalla_j.input.get_width() < pantalla_j.pantalla.get_width()-10:
                            pantalla_j.txtIngresado += event.unicode
                        else:
                            if pantalla_j.input2.get_width()<=pantalla_j.pantalla.get_width()-20:
                                pantalla_j.txtIngresado2 += event.unicode
                        pantalla_j.txtIngresadoFinal = pantalla_j.txtIngresado + pantalla_j.txtIngresado2
                    if event.key == pygame.K_RETURN:
                        SONIDO_DISPARO2.play()
                        puntaje, pres = (Comparador.Comparadores.compararSolo(numfrase, pantalla_j.txtIngresadoFinal, pantalla_j.cantborrados))
                        finaliza = True
                        tiempo_fin = time.time()
                if event.type == DISPARA_JUNO:
                    SONIDO_DISPARO1.play()
                if event.type == DISPARA_JDOS:
                    SONIDO_DISPARO2.play()
        ######
        reloj.tick(FPS)
if __name__ == "__main__":
    main()