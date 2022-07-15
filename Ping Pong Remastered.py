import pygame
#Main Parts
pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Ping Pong")
icon = pygame.image.load("pingpongballicon.png")
pygame.display.set_icon(icon)
hitter1 = pygame.image.load("hitter1.png")
x1 = 30
y1 = 200
hitter2 = pygame.image.load("hitter1.png")
running = True
while running:
    screen.fill((0, 0, 0))
    screen.blit(hitter1, (x1,y1))
    pygame.display.update()
    screen.blit(hitter2, (750,200))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
