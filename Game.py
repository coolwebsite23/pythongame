from pygame import *
pygame.init()
width = 500
height = 500
screen = pygame.display.set_mode(height, width)
running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
 screen.
