import pygame

pygame.init()
gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption('Pineapple Juice')
clock = pygame.time.Clock()

died = False

while not died:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            died = True
        
        print(event)
        
    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()