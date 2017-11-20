import pygame
from pygame.locals import *

class Graphics:
    def __init__(self):

        self.display()

    def display(self):
        pygame.init()
        screen = pygame.display.set_mode((900, 900))
        screen.fill([0,0,0])
        pygame.display.update()
        done = False
        #pygame.draw.rect(screen, [200,200,200], (450,450,20,20), 10)
        while not done:
            pygame.event.set_grab(True)
            #print (pygame.key.get_focused)
            pygame.draw.rect(screen, [200,200,200], (450,450,20,20), 10)
            for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        done = True
                        pygame.quit()
                        return
                    if event.type == pygame.KEYDOWN:
                        print ("key")
                        if event.key == pygame.K_ESCAPE:
                            pygame.quit()
                            print ("exiting")
                            return


        pygame.display.flip()

g = Graphics()
