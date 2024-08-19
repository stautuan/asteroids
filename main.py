import pygame

from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    while True:
        # close the window and exit the game loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
    
        screen.fill("black")

        # refresh the screen
        pygame.display.flip()

if __name__ == "__main__":
    main()