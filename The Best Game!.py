import pygame
pygame.init()
screen = pygame.display.set_mode((800,600))
icon = pygame.image.load('pingpongballicon.png')
pygame.display.set_caption('ping pong')
pygame.display.set_icon(icon)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False