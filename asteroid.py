import random
import pygame
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, ASTEROID_VELOCITY_INCREASE, CIRCLESHAPE_WIDTH

class Asteroid(CircleShape):
  def __init__(self, x, y, radius):
    super().__init__(x, y, radius)
  
  def draw(self, screen):
    pygame.draw.circle(screen, "white", self.position, self.radius, CIRCLESHAPE_WIDTH)
  
  def update(self, delta):
    self.position += self.velocity * delta
  
  def split(self):
    self.kill()
    
    if self.radius <= ASTEROID_MIN_RADIUS:
      return
    
    random_angle = random.uniform(20, 50)
    smaller_radius = self.radius - ASTEROID_MIN_RADIUS

    asteroid_alpha = Asteroid(self.position.x, self.position.y, smaller_radius)
    asteroid_alpha.velocity = self.velocity.rotate(random_angle) * ASTEROID_VELOCITY_INCREASE

    asteroid_beta = Asteroid(self.position.x, self.position.y, smaller_radius)
    asteroid_beta.velocity = self.velocity.rotate(-random_angle) * ASTEROID_VELOCITY_INCREASE  
