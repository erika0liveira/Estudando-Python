import pygame

pygame.init()
pygame.mixer.music.load("swanlake.ogg")
pygame.mixer.music.play(0)

clock = pygame.time.Clock()
clock.tick(10)
while pygame.mixer.music.get_busy():
    pygame.event.poll()
    clock.tick(10)

