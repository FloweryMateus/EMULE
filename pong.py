import pygame, random, sys

###

class LeftPlataforma:
    def __init__(self):
        self.plataformaImg = None
        self.pontuacao = 0
        self.plataformaX = .0
        self.plataformaY = .0
        self.alterarPlataformaY = .0
    
    def apresentarLeftPlataforma(self, screen, x, y):
        screen.blit(self.plataformaImg, (x, y))
        return screen


class RightPlataforma:
    def __init__(self):
        self.plataformaImg = None
        self.pontuacao = 0
        self.plataformaX = .0
        self.plataformaY = .0
        self.alterarPlataformaY = .0
    
    def apresentarRightPlataforma(self, screen, x, y):
        screen.blit(self.plataformaImg, (x, y))
        return screen


class Objeto:
    def __init__(self):
        self.objetoImg = None
        self.objetoX = .0
        self.objetoY = .0
        self.alterarObjetoX = .0
        self.alterarObjetoY = .0
    
    def apresentarObjeto(self, screen, x, y):
        screen.blit(self.objetoImg, (x, y))
        return screen

###

class Pong:
    def __init__(self):
        pygame.init()

        self.FPS = 60
        self.fpsClock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((800, 600))
        self.fundo = pygame.image.load('Assets/Pong/PlanoDeFundo.png')
        pygame.display.set_caption('Pong')
        icone = pygame.image.load('Assets/Pong/Icone.png')
        pygame.display.set_icon(icone)

###

    def exibirLeftPlataforma(self):
        self.leftPlataforma = LeftPlataforma()
        self.leftPlataforma.plataformaImg = pygame.image.load('Assets/Pong/Manipulavel/LeftPlataforma.png')
        self.leftPlataforma.plataformaX = 89
        self.leftPlataforma.plataformaY = 237
    
    def exibirRightPlataforma(self):
        self.rightPlataforma = RightPlataforma()
        self.rightPlataforma.plataformaImg = pygame.image.load('Assets/Pong/Manipulavel/RightPlataforma.png')
        self.rightPlataforma.plataformaX = 692
        self.rightPlataforma.plataformaY = 237
    
    def exibirObjeto(self):
        self.objeto = Objeto()
        self.objeto.objetoImg = pygame.image.load('Assets/Pong/Manipulavel/Objeto.png')
        self.objeto.objetoX = 390
        self.objeto.objetoY = 275

###

    def executar(self):
        self.exibirLeftPlataforma()
        self.exibirRightPlataforma()
        self.exibirObjeto()

        num = random.randint(0, 3)
        varXY = [(-4, 2), (4, -2), (-4, -2), (4, 2)]
        self.objeto.alterarObjetoX = varXY[num][0]
        self.objeto.alterarObjetoY = varXY[num][1]

        execPrograma = True
        while execPrograma == True:
            self.screen.fill((255, 255, 255))
            self.screen.blit(self.fundo, (0, 0))

###

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    execPrograma = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        execPrograma = False

                    if event.key == pygame.K_w:
                        self.leftPlataforma.alterarPlataformaY = -4
                    elif event.key == pygame.K_s:
                        self.leftPlataforma.alterarPlataformaY = 4
                    if event.key == pygame.K_UP:
                        self.rightPlataforma.alterarPlataformaY = -4
                    elif event.key == pygame.K_DOWN:
                        self.rightPlataforma.alterarPlataformaY = 4

                    if event.key == pygame.K_SPACE:
                        self.leftPlataforma.alterarPlataformaY = 0

                    
###
            
            self.leftPlataforma.plataformaY += self.leftPlataforma.alterarPlataformaY  
            self.rightPlataforma.plataformaY += self.rightPlataforma.alterarPlataformaY
            self.objeto.objetoX += self.objeto.alterarObjetoX
            self.objeto.objetoY += self.objeto.alterarObjetoY

### Detecção de colisão com as plataformas

            if self.leftPlataforma.plataformaImg.get_rect(x = self.leftPlataforma.plataformaX, y = self.leftPlataforma.plataformaY).colliderect(self.objeto.objetoImg.get_rect(x = self.objeto.objetoX, y = self.objeto.objetoY)) == True:
                self.objeto.alterarObjetoX *= -1
            
            if self.rightPlataforma.plataformaImg.get_rect(x = self.rightPlataforma.plataformaX, y = self.rightPlataforma.plataformaY).colliderect(self.objeto.objetoImg.get_rect(x = self.objeto.objetoX, y = self.objeto.objetoY)) == True:
                self.objeto.alterarObjetoX *= -1

### Detecção de colisão com os limites

            if self.leftPlataforma.plataformaY <= 0:
                self.leftPlataforma.plataformaY = 0
            elif self.leftPlataforma.plataformaY >= 552:
                self.leftPlataforma.plataformaY = 552
            if self.rightPlataforma.plataformaY <= 0:
                self.rightPlataforma.plataformaY = 0
            elif self.rightPlataforma.plataformaY >= 552:
                self.rightPlataforma.plataformaY = 552

            if self.objeto.objetoY <= 0:
                self.objeto.alterarObjetoY *= -1
            if self.objeto.objetoY >= 589:
                self.objeto.alterarObjetoY *= -1

            if self.objeto.objetoX >= 800:
                    self.leftPlataforma.pontuacao += 1
                    print('O vencedor da partida foi a plataforma direita.')
                    pygame.quit()
                    sys.exit()
            if self.objeto.objetoX <= 0:
                    self.rightPlataforma.pontuacao += 1
                    print('O vencedor da partida foi a plataforma esquerda.')
                    pygame.quit()
                    sys.exit()


###

            self.screen = self.leftPlataforma.apresentarLeftPlataforma(self.screen, self.leftPlataforma.plataformaX, self.leftPlataforma.plataformaY)
            self.screen = self.rightPlataforma.apresentarRightPlataforma(self.screen, self.rightPlataforma.plataformaX, self.rightPlataforma.plataformaY)
            self.screen = self.objeto.apresentarObjeto(self.screen, self.objeto.objetoX, self.objeto.objetoY)

            pygame.display.update()
            self.fpsClock.tick(self.FPS)
