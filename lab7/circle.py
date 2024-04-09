import pygame

pygame.init()
w = 800
import pygame
from pygame.locals import QUIT

pygame.init()
w = 200
h = 200
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption('ball')

x = 100
y = 100
r = 25

red = (200, 0, 0)

running = True
while True:
   for event in pygame.event.get():
      if event.type == QUIT:
           pygame.quit()
           running = False
      elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
          x -= 20
        elif event.key == pygame.K_RIGHT:
          x += 20
        elif event.key == pygame.K_UP:  
          y -= 20
        elif event.key == pygame.K_DOWN:
          y += 20

   x = max(r, min(w - r, x))
   y = max(r, min(h - r, y))

   screen.fill((255, 255, 255))
   pygame.draw.circle(screen, red, (x, y), r)

   pygame.display.update()
