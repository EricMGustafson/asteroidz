import sys
import pygame
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *
from player import Player
from shot import Shot

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
  shots = pygame.sprite.Group()

  Player.containers = (updatables, drawables)
  player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

  Asteroid.containers = (asteroids, updatables, drawables)

  AsteroidField.containers = (updatables)
  AsteroidField()

  Shot.containers = (shots, updatables, drawables)

  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return
    
    for updatable in updatables:
      updatable.update(dt)

    for asteroid in asteroids:
      if asteroid.collision_check(player):
        print("Game over!")
        sys.exit()
      
    screen.fill("black")
    
    for drawable in drawables:
      drawable.draw(screen)

    pygame.display.flip()

    delta = time_clock.tick(60)
    dt = delta / 1000




if __name__ == "__main__":

    main()