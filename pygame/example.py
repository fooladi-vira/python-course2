#create graphic game
import pygame

pygame.init()
gameDisplay=pygame.display.set_mode((800,600))
pygame.display.set_caption('sample game')
color=(200,100,0)
gameDisplay.fill(color)
icon=pygame.image.load('modern.png')
gameDisplay.blit(icon,(400,400))
clock=pygame.time.Clock()
pygame.draw.rect(gameDisplay,(0,0,0),(395,0,100,10))
pygame.display.flip()
exitGame=False
while not exitGame:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exitGame=True
            break
    
    pygame.display.update()
    clock.tick(30)


