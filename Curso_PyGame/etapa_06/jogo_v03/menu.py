# -*- coding: iso-8859-1 -*-

#
#  Copylefth (c) 2009, Grudejo:
#    Aline Grazielle Silva Reis
#    Julia Carmona Almeida Chaves
#    Luziany Maria de Oliveira
#    Joyce Karoline Dare
#    Prof. Douglas Machado Tavares
#

import pygame
from pygame.constants import *


class Menu:
    """ Classe Menu """

    def __init__(self, tela):
        """ Construtor:  __init__() -> instancia de jogo """
        self.tela = tela
        self.opcao = 1
        self.enter = False


    def tratar_eventos_menu(self):
        """ Observa e trata eventos desejados """
        for evento in pygame.event.get():
            if (evento.type == QUIT):
                raise SystemExit
            elif (evento.type == KEYDOWN):
                if ((evento.key == K_ESCAPE) or (evento.key == K_q)):
                    raise SystemExit
                elif (evento.key == K_UP):
                    if(self.opcao == 1):
                        self.opcao = 3
                    else:
                        self.opcao -= 1
                    self.enter = False
                elif (evento.key == K_DOWN):
                    if(self.opcao == 3):
                        self.opcao = 1
                    else:
                        self.opcao += 1
                    self.enter = False
                elif (evento.key == K_RETURN):
                    self.enter = True


    def repintar_menu(self):
        """ Repinta o menu """
        fundo = pygame.image.load("dados/imagens/fundo_menu.png")
        self.tela.blit(fundo, (0, 0))
        fonte = pygame.font.Font("dados/fontes/pristina.ttf", 50)
        fonte.set_bold(True)
        fonte_rend = fonte.render(" T�tulo ", True, (255, 255, 255))
        self.tela.blit(fonte_rend, (420, 130))
        if (self.opcao == 1):
            op1 = "[ Caminhar ]"
            op2 = "  Cr�ditos  "
            op3 = "  Sair      "
            cor1 = ( 47, 112, 175)
            cor2 = (255, 255, 255)
            cor3 = (255, 255, 255)
        elif (self.opcao == 2):
            op1 = "  Caminhar  "
            op2 = "[ Cr�ditos ]"
            op3 = "  Sair      "
            cor1 = (255, 255, 255)
            cor2 = ( 47, 112, 175)
            cor3 = (255, 255, 255)
        else:
            op1 = "  Caminhar  "
            op2 = "  Cr�ditos  "
            op3 = "[ Sair ]    "
            cor1 = (255, 255, 255)
            cor2 = (255, 255, 255)
            cor3 = ( 47, 112, 175)
        fonte = pygame.font.Font("dados/fontes/dejavu_sans.ttf", 25)
        fonte_rend = fonte.render(op1, True, cor1)
        self.tela.blit(fonte_rend, (420, 200))
        fonte_rend = fonte.render(op2, True, cor2)
        self.tela.blit(fonte_rend, (480, 260))
        fonte_rend = fonte.render(op3, True, cor3)
        self.tela.blit(fonte_rend, (540, 320))
        pygame.display.update()


    def rodar(self):
        """ Roda o menu """
        self.enter = False
        while (True):
            self.tratar_eventos_menu()
            self.repintar_menu()
            if (self.enter):
                return self.opcao
