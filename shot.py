import pygame
from circleshape import CircleShape
from constants import SHOT_RADIOUS


class Shot(CircleShape):
  def __init__(self, x, y):
    super().__init__(x, y, SHOT_RADIOUS) 
  
  def draw(self, screen):
    pygame.draw.circle(screen, "white", self.position, self.radius, 2)
  
  def update(self,  delta):
    self.position += self.velocity * delta