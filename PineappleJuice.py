import random
import pygame

pygame.init()

display_width = 800
display_height = 600

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

#   cria janela do jogo (tamanho)
#                       (nome)
#   inicia o relogio
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Epilepsy')
clock = pygame.time.Clock()

died = False

#   para cada evento, mostra o evento
#   se evento == clicar X, fecha o jogo
x = 0
while not died:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            died = True    
    
    gameDisplay.fill((random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255)))
    

    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()