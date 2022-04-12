import pygame
pygame.display.set_caption("Snake")
from pygame.locals import *
def draw_block():
    #surface.fill((0, 0, 0))
    surface.blit(block, (100, 100))
    pygame.display.flip()

if __name__ == "__main__":
    pygame.init()

    surface = pygame.display.set_mode((1000, 500))
    surface.fill((0,0,0))

    block = pygame.image.load("icons8-blockly-light-green-30.png").convert()
    block_x = 100
    block_y = 100
    surface.blit(block,(block_x, block_y))

    pygame.display.flip()

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:


                    if event.key == K_UP:
                        block_y -= 10
                        draw_block()

                    if event.key == K_DOWN:
                        block_y += 10
                        draw_block()

                    if event.key == K_LEFT:
                        block_x -= 10
                        draw_block()

                    if event.key == K_RIGHT:
                        block_x += 10
                        draw_block()

                    running = False

            elif event.type == QUIT:

                running = False