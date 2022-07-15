import time
import pygame
from pygame import mixer
pygame.init()
screen = pygame.display.set_mode((1287, 660))
pygame.display.set_caption("Halo PE")
icon = pygame.image.load("haloICON.png")
pygame.display.set_icon(icon)
haloIMG = pygame.image.load("HaloPE.jpg")
haloMENU = pygame.image.load("haloPEbackground.jpg")
screen.blit(haloIMG, (70,-60))
pygame.display.update()
time.sleep(5)
screen.blit(haloMENU, (70, -60))
pygame.display.update()
mixer.music.load("Halo Theme Song Original.mp3")
mixer.music.play(-1)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False