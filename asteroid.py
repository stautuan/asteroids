import pygame
import random

from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()

        # smallest asteroid
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        # let's spawn 2 new asteroids as we split larger asteroids

        # generate a random angle between 20 and 50 degrees
        random_angle = random.uniform(20, 50)

        # split in opposite directions 
        a = self.velocity.rotate(random_angle)
        b = self.velocity.rotate(-random_angle)

        # this new radius is for creating smaller asteroids
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        # create two new Asteroid objects with the new radius
        # set the velocity of two new asteroids by multiplying it by 1.2
        asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid.velocity = a * 1.2
        asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid.velocity = b * 1.2

