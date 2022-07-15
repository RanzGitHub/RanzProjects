import turtle
import pygame
pygame.init()
Pong = turtle.Turtle()
screen = pygame.display.set_mode((1280, 660))
pygame.display.set_caption("Ping Pong Menu")
icon = pygame.image.load("pingpongballicon.png")
pygame.display.set_icon(icon)
pongMENU = pygame.image.load("pongMENU.jpg")
STARTbtn = pygame.image.load("STARTbtn.jpg")
EXITbtn = pygame.image.load("EXITbtn.jpg")
MenuRunning = True
GameRunning = False
while MenuRunning:
    screen.fill((0,0,0))
    screen.blit(pongMENU, (0,0))
    screen.blit(STARTbtn, (450, 270))
    screen.blit(EXITbtn, (450,450))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            MenuRunning = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            GameRunning = True
while GameRunning:
    Screen = turtle.Screen()
    Screen.title("Ping Pong")