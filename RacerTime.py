import pygame
pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("RacerTime")
icon = pygame.image.load("iconRACE.png")
pygame.display.set_icon(icon)
car = pygame.image.load("SeekPng.com_car-png_2105717.png")
car = pygame.transform.rotate(car, 90)
running = True
while running:
    screen.fill((0, 255, 0))
    screen.blit(car, (0,0))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False