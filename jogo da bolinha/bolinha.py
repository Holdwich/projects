from graphics import *
import random
from pathlib import Path
import pygame

# pega a localização da pasta do jogo

path = Path().absolute()
print("Path do jogo: {}".format(path))

# inicializa audios do jogo e o player que será utilizado
global toggleSom

toggleSom = True

somBarra = path / 'audio' / 'barra.wav'
somParede = path / 'audio' / 'parede.wav'
somGameOver = path / 'audio' / 'GameOver.wav'
try:
    pygame.mixer.init()
except pygame.error:
    print("Dispositivo de som não encontrado")

# desenha a janela
win = GraphWin("Jogo da Bolinha", 800, 600)
win.setBackground("Black")

pontuacoesDaSessao = []


def configTema():
    global jogando
    jogando = False

    global corPrincipal
    global corSecundaria

    def apagarConfigTema():
        textoClaro.undraw()
        textoEscuro.undraw()
        opcaoClaro.undraw()
        opcaoEscuro.undraw()
        textoSelecaoTema.undraw()

    # Desenhar menu
    textoSelecaoTema = Text(Point(400, 100), "Selecione um tema")
    textoSelecaoTema.setSize(20)
    try:
        textoSelecaoTema.setFill(corSecundaria)
    except NameError:
        textoSelecaoTema.setFill('White')

    textoSelecaoTema.draw(win)

    opcaoEscuro = Rectangle(Point(200, 300), Point(300, 350))
    opcaoEscuro.setFill('black')
    opcaoEscuro.setOutline('white')
    opcaoEscuro.draw(win)

    opcaoClaro = Rectangle(Point(500, 300), Point(600, 350))
    opcaoClaro.setFill('White')
    opcaoClaro.setOutline('Black')
    opcaoClaro.draw(win)

    textoEscuro = Text(Point(250, 325), "Escuro")
    textoEscuro.setFill('White')
    textoEscuro.draw(win)

    textoClaro = Text(Point(550, 325), "Claro")
    textoClaro.setFill('black')
    textoClaro.draw(win)

    # seleção do menu
    while not jogando:
        clique = win.getMouse()
        x = clique.getX()
        y = clique.getY()
        if 200 < x < 300 and 300 < y < 350:
            corPrincipal = 'Black'
            corSecundaria = 'White'
            win.setBackground(corPrincipal)
            apagarConfigTema()
            menu()
        elif 500 < x < 600 and 300 < y < 350:
            corPrincipal = 'White'
            corSecundaria = 'Black'
            win.setBackground(corPrincipal)
            apagarConfigTema()
            menu()
        else:
            continue


def menu():
    global jogando
    global toggleSom

    def apagarMenu():
        global jogadorAnterior
        global jogador

        textoJogar.undraw()
        opcaoJogar.undraw()
        textoRankings.undraw()
        opcaoRankings.undraw()
        titulo.undraw()
        textoTemas.undraw()
        opcaoTemas.undraw()
        textoInstrucoes.undraw()
        opcaoInstrucoes.undraw()
        textoSair.undraw()
        opcaoSair.undraw()
        textoCreditos.undraw()
        opcaoCreditos.undraw()
        opcaoSom.undraw()
        textoToggleSom.undraw()
        textoSom.undraw()
        jogador = entradaJogador.getText()
        if jogador == "":
            try:
                jogador = jogadorAnterior
            except NameError:
                jogador = "Jogador"
        else:
            jogadorAnterior = jogador
        entradaJogador.undraw()
        nomeJogador.undraw()

    jogando = False

    # Desenhar Menu
    titulo = Text(Point(400, 100), "Jogo da Bolinha")
    titulo.setFill(corSecundaria)
    titulo.setSize(20)
    titulo.draw(win)

    entradaJogador = Entry(Point(450, 150), 12)
    entradaJogador.draw(win)

    nomeJogador = Text(Point(325, 150), "Insira seu nome:")
    nomeJogador.setFill(corSecundaria)
    nomeJogador.draw(win)

    opcaoJogar = Rectangle(Point(350, 200), Point(450, 250))
    opcaoJogar.setFill(corPrincipal)
    opcaoJogar.setOutline(corSecundaria)
    opcaoJogar.draw(win)

    textoJogar = Text(Point(400, 225), "Jogar")
    textoJogar.setFill(corSecundaria)
    textoJogar.draw(win)

    opcaoRankings = Rectangle(Point(350, 300), Point(450, 350))
    opcaoRankings.setFill(corPrincipal)
    opcaoRankings.setOutline(corSecundaria)
    opcaoRankings.draw(win)

    textoRankings = Text(Point(400, 325), "Rankings")
    textoRankings.setFill(corSecundaria)
    textoRankings.draw(win)

    opcaoTemas = Rectangle(Point(5, 545), Point(105, 595))
    opcaoTemas.setFill(corPrincipal)
    opcaoTemas.setOutline(corSecundaria)
    opcaoTemas.draw(win)

    textoTemas = Text(Point(55, 570), "Temas")
    textoTemas.setFill(corSecundaria)
    textoTemas.draw(win)

    opcaoInstrucoes = Rectangle(Point(350, 400), Point(450, 450))
    opcaoInstrucoes.setFill(corPrincipal)
    opcaoInstrucoes.setOutline(corSecundaria)
    opcaoInstrucoes.draw(win)

    textoInstrucoes = Text(Point(400, 425), "Instruções")
    textoInstrucoes.setFill(corSecundaria)
    textoInstrucoes.draw(win)

    opcaoSair = Rectangle(Point(350, 545), Point(450, 595))
    opcaoSair.setFill(corPrincipal)
    opcaoSair.setOutline(corSecundaria)
    opcaoSair.draw(win)

    textoSair = Text(Point(400, 570), "Sair")
    textoSair.setFill(corSecundaria)
    textoSair.draw(win)

    opcaoCreditos = Rectangle(Point(695, 545), Point(795, 595))
    opcaoCreditos.setFill(corPrincipal)
    opcaoCreditos.setOutline(corSecundaria)
    opcaoCreditos.draw(win)

    textoCreditos = Text(Point(745, 570), "Créditos")
    textoCreditos.setFill(corSecundaria)
    textoCreditos.draw(win)

    opcaoSom = Rectangle(Point(5, 5), Point(55, 55))
    opcaoSom.setFill(corPrincipal)
    opcaoSom.setOutline(corSecundaria)
    opcaoSom.draw(win)

    textoSom = Text(Point(27, 18), "Som")
    textoSom.setFill(corSecundaria)
    textoSom.draw(win)

    if toggleSom:
        textoToggleSom = Text(Point(27, 36), "Hab.")
        textoToggleSom.setFill(corSecundaria)
        textoToggleSom.draw(win)
    elif not toggleSom:
        textoToggleSom = Text(Point(27, 36), "Des.")
        textoToggleSom.setFill(corSecundaria)
        textoToggleSom.draw(win)

    # Pegar opções do Menu
    while not jogando:
        clique = win.getMouse()
        x = clique.getX()
        y = clique.getY()
        if 350 < x < 450 and 200 < y < 250:
            apagarMenu()
            jogo()
        elif 350 < x < 450 and 300 < y < 350:
            apagarMenu()
            rankings()
        elif 5 < x < 105 and 545 < y < 595:
            apagarMenu()
            configTema()
        elif 350 < x < 450 and 400 < y < 450:
            apagarMenu()
            instrucoes()
        elif 350 < x < 450 and 545 < y < 575:
            apagarMenu()
            GraphWin.close(win)
        elif 695 < x < 795 and 545 < y < 595:
            apagarMenu()
            creditos()
        elif 5 < x < 55 and 5 < y < 55:
            if toggleSom:
                textoToggleSom.undraw()
                textoToggleSom = Text(Point(27, 36), "Des.")
                textoToggleSom.setFill(corSecundaria)
                textoToggleSom.draw(win)
                toggleSom = False
            elif not toggleSom:
                textoToggleSom.undraw()
                textoToggleSom = Text(Point(27, 36), "Hab.")
                textoToggleSom.setFill(corSecundaria)
                textoToggleSom.draw(win)
                toggleSom = True
            continue
        else:
            continue


def creditos():
    global jogando
    jogando = False

    # Desenha menu
    tituloCreditos = Text(Point(400, 100), "Créditos")
    tituloCreditos.setFill(corSecundaria)
    tituloCreditos.setSize(20)
    tituloCreditos.draw(win)

    linha1 = Text(Point(400, 150), "        Professor                                               Gilberto Hiragi")
    linha1.setFill(corSecundaria)
    linha1.setStyle('bold')
    linha1.draw(win)

    linha6 = Text(Point(400, 200),
                  "          Coordenador                                            Fernando Guimarães")
    linha6.setFill(corSecundaria)
    linha6.setStyle('bold')
    linha6.draw(win)

    linha2 = Text(Point(400, 250), "Programador Líder")
    linha2.setFill(corSecundaria)
    linha2.setStyle('bold')
    linha2.draw(win)

    linha7 = Text(Point(400, 285), "Matheus Fernandes")
    linha7.setFill(corSecundaria)
    linha7.draw(win)

    linha3 = Text(Point(400, 330), "Programadores")
    linha3.setFill(corSecundaria)
    linha3.setStyle('bold')
    linha3.draw(win)

    linha4 = Text(Point(400, 380),
                  "Lucas Porto                                Brunna Coutinho                       Gustavo Monteiro")
    linha4.setFill(corSecundaria)
    linha4.draw(win)

    linha5 = Text(Point(385, 425),
                  "Augusto Marino                               Rafael Adorno                             Vitor Oliveira")
    linha5.setFill(corSecundaria)
    linha5.draw(win)

    opcaoMenu = Rectangle(Point(350, 500), Point(450, 550))
    opcaoMenu.setFill(corPrincipal)
    opcaoMenu.setOutline(corSecundaria)
    opcaoMenu.draw(win)

    textoMenu = Text(Point(400, 525), "Voltar")
    textoMenu.setFill(corSecundaria)
    textoMenu.draw(win)

    # seleção para voltar
    while not jogando:
        clique = win.getMouse()
        x = clique.getX()
        y = clique.getY()
        if 350 < x < 450 and 500 < y < 550:
            textoMenu.undraw()
            opcaoMenu.undraw()
            linha7.undraw()
            linha6.undraw()
            linha5.undraw()
            linha4.undraw()
            linha3.undraw()
            linha2.undraw()
            linha1.undraw()
            tituloCreditos.undraw()
            menu()


def instrucoes():
    global jogando
    jogando = False

    # desenha menu
    tituloInstrucoes = Text(Point(400, 100), "Instruções")
    tituloInstrucoes.setFill(corSecundaria)
    tituloInstrucoes.setSize(20)
    tituloInstrucoes.draw(win)

    linha1 = Text(Point(400, 200), "O Objetivo do jogo é fazer o máximo de pontos possíveis")
    linha1.setFill(corSecundaria)
    linha1.draw(win)

    linha2 = Text(Point(400, 225), "Cada vez que a bola bater na sua barra, você marca um ponto")
    linha2.setFill(corSecundaria)
    linha2.draw(win)

    linha3 = Text(Point(400, 250), "Se você deixar a bola cair, o jogo acaba")
    linha3.setFill(corSecundaria)
    linha3.draw(win)

    linha4 = Text(Point(400, 300), "Controles")
    linha4.setFill(corSecundaria)
    linha4.setSize(15)
    linha4.draw(win)

    linha5 = Text(Point(400, 350), "As setas para a esquerda e a direita controlam a barra")
    linha5.setFill(corSecundaria)
    linha5.draw(win)

    linha6 = Text(Point(400, 375), "Aperte ESC para interromper o jogo e voltar ao menu")
    linha6.setFill(corSecundaria)
    linha6.draw(win)

    opcaoMenu = Rectangle(Point(350, 500), Point(450, 550))
    opcaoMenu.setFill(corPrincipal)
    opcaoMenu.setOutline(corSecundaria)
    opcaoMenu.draw(win)

    textoMenu = Text(Point(400, 525), "Voltar")
    textoMenu.setFill(corSecundaria)
    textoMenu.draw(win)

    # seleção para voltar
    while not jogando:
        clique = win.getMouse()
        x = clique.getX()
        y = clique.getY()
        if 350 < x < 450 and 500 < y < 550:
            textoMenu.undraw()
            opcaoMenu.undraw()
            linha6.undraw()
            linha5.undraw()
            linha4.undraw()
            linha3.undraw()
            linha2.undraw()
            linha1.undraw()
            tituloInstrucoes.undraw()
            menu()


def rankings():
    global jogando
    jogando = False

    # desenhar menu
    MenuRanking = Text(Point(400, 100), "Rankings")
    MenuRanking.setFill(corSecundaria)
    MenuRanking.setSize(20)
    MenuRanking.draw(win)

    # Desenhar pontuações de uma forma que haja como apagar depois (Provavelmente há uma forma melhor de fazer isso)
    try:
        pontuacaoNoRanking = pontuacoesDaSessao[0]
    except IndexError:
        pontuacaoNoRanking = "nulo"
    rank1 = Text(Point(400, 150), "1º - {}".format(pontuacaoNoRanking))
    rank1.setFill(corSecundaria)
    rank1.draw(win)

    try:
        pontuacaoNoRanking = pontuacoesDaSessao[1]
    except IndexError:
        pontuacaoNoRanking = "nulo"
    rank2 = Text(Point(400, 175), "2º - {}".format(pontuacaoNoRanking))
    rank2.setFill(corSecundaria)
    rank2.draw(win)

    try:
        pontuacaoNoRanking = pontuacoesDaSessao[2]
    except IndexError:
        pontuacaoNoRanking = "nulo"
    rank3 = Text(Point(400, 200), "3º - {}".format(pontuacaoNoRanking))
    rank3.setFill(corSecundaria)
    rank3.draw(win)

    try:
        pontuacaoNoRanking = pontuacoesDaSessao[3]
    except IndexError:
        pontuacaoNoRanking = "nulo"
    rank4 = Text(Point(400, 225), "4º - {}".format(pontuacaoNoRanking))
    rank4.setFill(corSecundaria)
    rank4.draw(win)

    try:
        pontuacaoNoRanking = pontuacoesDaSessao[4]
    except IndexError:
        pontuacaoNoRanking = "nulo"
    rank5 = Text(Point(400, 250), "5º - {}".format(pontuacaoNoRanking))
    rank5.setFill(corSecundaria)
    rank5.draw(win)

    try:
        pontuacaoNoRanking = pontuacoesDaSessao[5]
    except IndexError:
        pontuacaoNoRanking = "nulo"
    rank6 = Text(Point(400, 275), "6º - {}".format(pontuacaoNoRanking))
    rank6.setFill(corSecundaria)
    rank6.draw(win)

    try:
        pontuacaoNoRanking = pontuacoesDaSessao[6]
    except IndexError:
        pontuacaoNoRanking = "nulo"
    rank7 = Text(Point(400, 300), "7º - {}".format(pontuacaoNoRanking))
    rank7.setFill(corSecundaria)
    rank7.draw(win)

    try:
        pontuacaoNoRanking = pontuacoesDaSessao[7]
    except IndexError:
        pontuacaoNoRanking = "nulo"
    rank8 = Text(Point(400, 325), "8º - {}".format(pontuacaoNoRanking))
    rank8.setFill(corSecundaria)
    rank8.draw(win)

    try:
        pontuacaoNoRanking = pontuacoesDaSessao[8]
    except IndexError:
        pontuacaoNoRanking = "nulo"
    rank9 = Text(Point(400, 350), "9º - {}".format(pontuacaoNoRanking))
    rank9.setFill(corSecundaria)
    rank9.draw(win)

    try:
        pontuacaoNoRanking = pontuacoesDaSessao[9]
    except IndexError:
        pontuacaoNoRanking = "nulo"
    rank10 = Text(Point(400, 375), "10º - {}".format(pontuacaoNoRanking))
    rank10.setFill(corSecundaria)
    rank10.draw(win)

    # Opção de voltar
    opcaoMenu = Rectangle(Point(350, 500), Point(450, 550))
    opcaoMenu.setFill(corPrincipal)
    opcaoMenu.setOutline(corSecundaria)
    opcaoMenu.draw(win)

    textoMenu = Text(Point(400, 525), "Voltar")
    textoMenu.setFill(corSecundaria)
    textoMenu.draw(win)

    # Input do usuário para voltar
    while not jogando:
        clique = win.getMouse()
        x = clique.getX()
        y = clique.getY()
        if 350 < x < 450 and 500 < y < 550:
            rank10.undraw()
            rank9.undraw()
            rank8.undraw()
            rank7.undraw()
            rank6.undraw()
            rank5.undraw()
            rank4.undraw()
            rank3.undraw()
            rank2.undraw()
            rank1.undraw()
            MenuRanking.undraw()
            textoMenu.undraw()
            opcaoMenu.undraw()
            menu()
        else:
            continue


def jogo():
    global jogando
    global jogadorAnterior
    jogando = False

    def apagarDificuldade():
        global jogando

        opcaoDificil.undraw()
        opcaoMedio.undraw()
        opcaoFacil.undraw()
        textoDificil.undraw()
        textoMedio.undraw()
        textoFacil.undraw()
        textoDificuldade.undraw()
        explicacaoDificuldades.undraw()
        ObsDificuldades.undraw()
        opcaoVoltar.undraw()
        textoVoltar.undraw()
        jogando = True

    # Caixas de seleção de dificuldade
    textoDificuldade = Text(Point(400, 100), "Selecione sua dificuldade")
    textoDificuldade.setFill(corSecundaria)
    textoDificuldade.setSize(20)
    textoDificuldade.draw(win)

    explicacaoDificuldades = Text(Point(400, 200),
                                  "A dificuldade determina o raio da bolinha, o tamanho da barra inicial, e o multiplicador ao final da partida.")
    explicacaoDificuldades.setFill(corSecundaria)
    explicacaoDificuldades.draw(win)

    ObsDificuldades = Text(Point(400, 450),
                           "Obs: Por padrão, a velocidade da bolinha vai ao longo do tempo aumentando, e a barra, diminuindo de tamanho.")
    ObsDificuldades.setFill(corSecundaria)
    ObsDificuldades.setSize(11)
    ObsDificuldades.draw(win)

    opcaoFacil = Rectangle(Point(150, 300), Point(250, 350))
    opcaoFacil.setFill(corPrincipal)
    opcaoFacil.setOutline(corSecundaria)
    opcaoFacil.draw(win)

    textoFacil = Text(Point(200, 325), "Fácil")
    textoFacil.setFill(corSecundaria)
    textoFacil.draw(win)

    opcaoMedio = Rectangle(Point(350, 300), Point(450, 350))
    opcaoMedio.setFill(corPrincipal)
    opcaoMedio.setOutline(corSecundaria)
    opcaoMedio.draw(win)

    textoMedio = Text(Point(400, 325), "Médio")
    textoMedio.setFill(corSecundaria)
    textoMedio.draw(win)

    opcaoDificil = Rectangle(Point(550, 300), Point(650, 350))
    opcaoDificil.setFill(corPrincipal)
    opcaoDificil.setOutline(corSecundaria)
    opcaoDificil.draw(win)

    textoDificil = Text(Point(600, 325), "Difícil")
    textoDificil.setFill(corSecundaria)
    textoDificil.draw(win)

    opcaoVoltar = Rectangle(Point(350, 500), Point(450, 550))
    opcaoVoltar.setFill(corPrincipal)
    opcaoVoltar.setOutline(corSecundaria)
    opcaoVoltar.draw(win)

    textoVoltar = Text(Point(400, 525), "Voltar")
    textoVoltar.setFill(corSecundaria)
    textoVoltar.draw(win)

    # Seleção da dificuldade
    while not jogando:
        clique = win.getMouse()
        x = clique.getX()
        y = clique.getY()
        if 150 < x < 250 and 300 < y < 350:
            Dificuldade = "Fácil"
            MultDif = 1
            raio = 12
            tamanho = 125
            velocidade = 5
            apagarDificuldade()
            break
        elif 350 < x < 450 and 300 < y < 350:
            Dificuldade = "Médio"
            MultDif = 1.25
            raio = 10
            tamanho = 100
            velocidade = 5
            apagarDificuldade()
            break
        elif 550 < x < 650 and 300 < y < 350:
            Dificuldade = "Difícil"
            MultDif = 1.5
            raio = 8
            tamanho = 75
            velocidade = 5
            apagarDificuldade()
            break
        elif 350 < x < 450 and 500 < y < 550:
            apagarDificuldade()
            menu()
        else:
            continue

    # Desenhar jogo
    linhaSuperior = Line(Point(0, 40), Point(800, 40))
    linhaSuperior.setWidth(10)
    linhaSuperior.setFill(corSecundaria)
    linhaSuperior.draw(win)

    linhaInferior = Line(Point(0, 550), Point(800, 550))
    linhaInferior.setWidth(3)
    linhaInferior.setFill(corSecundaria)
    linhaInferior.draw(win)

    col = 390
    lin = 80
    circulo = Circle(Point(col, lin), raio)
    circulo.setFill(corSecundaria)
    circulo.draw(win)

    colIni = 340
    barra = Line(Point(colIni, 530), Point(colIni + tamanho, 530))
    barra.setFill(corSecundaria)
    barra.setWidth(10)
    barra.draw(win)

    bateu = True
    continuar = True

    caixaPontos = Rectangle(Point(350, 550), Point(450, 600))
    caixaPontos.setFill(corPrincipal)
    caixaPontos.setOutline(corSecundaria)
    caixaPontos.draw(win)

    pts = 0
    pontos = Text(Point(400, 575), "Pontos: {}".format(pts))
    pontos.setFill(corSecundaria)
    pontos.setSize(14)
    pontos.draw(win)

    preparar = Text(Point(400, 200), "Preparar...")
    preparar.setFill(corSecundaria)
    preparar.draw(win)

    time.sleep(1)

    preparar.undraw()

    # Lógica do jogo
    while continuar:

        if bateu:
            passo = random.randrange(1, 10)
            if random.random() < 0.5:
                passo = -passo
            bateu = False

        if (col + raio + passo) > 800:
            passo = -passo
            if toggleSom:
                try:
                    pygame.mixer.music.load(somBarra)
                    pygame.mixer.music.play()
                except pygame.error:
                    pass

        if (col - raio + passo) < 0:
            passo = -passo
            if toggleSom:
                try:
                    pygame.mixer.music.load(somBarra)
                    pygame.mixer.music.play()
                except pygame.error:
                    pass

        if lin < 65:
            velocidade = -velocidade
            print("pong")
            if toggleSom:
                try:
                    pygame.mixer.music.load(somParede)
                    pygame.mixer.music.play()
                except pygame.error:
                    pass

        if lin == 515 and col > colIni and col < (colIni + tamanho):
            bateu = True
            velocidade = -velocidade
            if velocidade > 0:
                velocidade += 1
                if velocidade > 10 and tamanho != 50:
                    tamanho -= 1
            if velocidade < 0:
                velocidade -= 1
                if velocidade < -10 and tamanho != 50:
                    tamanho -= 1
            pts += 1
            print("ping")
            if toggleSom:
                try:
                    pygame.mixer.music.load(somBarra)
                    pygame.mixer.music.play()
                except pygame.error:
                    pass

        if lin > 535:
            continuar = False

        # Nova posição do círculo
        circulo.undraw()
        col += passo
        lin += velocidade
        circulo = Circle(Point(col, lin), raio)
        circulo.setFill(corSecundaria)
        circulo.draw(win)

        # Movimento horizontal da barra pelas setas direita/esquerda
        tecla = win.checkKey()

        # Voltar ao menu
        if tecla == "Escape":
            continuar = False
            continue

        if tecla == "Right":
            if (colIni - 10) < 701 + 10:
                colIni = colIni + 10

            barra.undraw()
            barra = Line(Point(colIni, 530), Point(colIni + tamanho, 530))
            barra.setFill(corSecundaria)
            barra.setWidth(10)
            barra.draw(win)

        if tecla == "Left":
            if (colIni - 10) > -1:
                colIni = colIni - 10

            barra.undraw()
            barra = Line(Point(colIni, 530), Point(colIni + tamanho, 530))
            barra.setFill(corSecundaria)
            barra.setWidth(10)
            barra.draw(win)

        # Esperar o ser humano reagir
        time.sleep(.07)

        pontos.undraw()
        pontos = Text(Point(400, 575), "Pontos: {}".format(pts))
        pontos.setFill(corSecundaria)
        pontos.setSize(14)
        pontos.draw(win)

    # fim de jogo
    barra.undraw()
    circulo.undraw()
    pontos.undraw()
    linhaInferior.undraw()
    linhaSuperior.undraw()
    caixaPontos.undraw()

    if toggleSom:
        try:
            pygame.mixer.music.load(somGameOver)
            pygame.mixer.music.play()
        except pygame.error:
            pass

    gameOver = Text(Point(400, 275), "Fim de jogo!")
    gameOver.setFill(corSecundaria)
    gameOver.draw(win)

    finalDificuldade = Text(Point(400, 300), "Dificuldade: {}".format(Dificuldade))
    finalDificuldade.setFill(corSecundaria)
    finalDificuldade.draw(win)

    pontuacaoFinal = Text(Point(400, 325), "Pontos: {} x {} = {}".format(pts, MultDif, round(pts * MultDif)))
    pontuacaoFinal.setFill(corSecundaria)
    pontuacaoFinal.draw(win)

    pontuacoesDaSessao.append("{} - {}".format(round(pts * MultDif), jogador))
    pontuacoesDaSessao.sort(key=lambda x: int(x.split('-', 1)[0]), reverse=True)

    jogadorAnterior = jogador

    time.sleep(5)

    pontuacaoFinal.undraw()
    gameOver.undraw()
    finalDificuldade.undraw()

    menu()


configTema()