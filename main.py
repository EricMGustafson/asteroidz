import pygame
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *
from player import Player

def main():

  print("Starting asteroids!")
  print("Screen width:", SCREEN_WIDTH)
  print("Screen height:", SCREEN_HEIGHT)

  pygame.init()
 
  time_clock = pygame.time.Clock()
  dt = 0

  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

  updatables = pygame.sprite.Group()
  drawables = pygame.sprite.Group()
  asteroids = pygame.sprite.Group()

  Player.containers = (updatables, drawables)
  Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

  Asteroid.containers = (asteroids, updatables, drawables)

  AsteroidField.containers = (updatables)
  AsteroidField()

  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return
    
    for updatable in updatables:
      updatable.update(dt)      
      
    screen.fill("black")
    
    for drawable in drawables:
      drawable.draw(screen)

    pygame.display.flip()

    delta = time_clock.tick(60)
    dt = delta / 1000




if __name__ == "__main__":

    main()