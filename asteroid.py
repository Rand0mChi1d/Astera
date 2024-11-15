import pygame
import random

from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    

    def draw(self, screen):
        pygame.draw.circle(screen, "gray", self.position, self.radius, width = 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            randegree = random.uniform(20, 50)
            new_rad = self.radius - ASTEROID_MIN_RADIUS

            split_asteroid_1 = Asteroid(self.position[0], self.position[1], new_rad)
            split_asteroid_2 = Asteroid(self.position[0], self.position[1], new_rad)
            split_asteroid_1.velocity = 1.2 * self.velocity.rotate(randegree)
            split_asteroid_2.velocity = 1.2 * self.velocity.rotate(-randegree)
            


    