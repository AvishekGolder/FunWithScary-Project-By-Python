import pygame
from time import sleep
pygame.init()
disp = pygame.display.set_mode((0,0),pygame.FULLSCREEN)

pygame.mixer.init()
pygame.mixer.music.load('src/song.mp3')
pygame.mixer.music.play()
sleep(5)

pygame.mixer.music.load('src/ghost.mp3')
pygame.mixer.music.play()
sleep(1)

image = pygame.image.load('src/ghost.jpg')
disp.blit(image, (0,0))
pygame.display.update()
sleep(3)
