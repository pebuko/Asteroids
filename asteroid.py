import pygame
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.rotation = 0
        

    def draw(self, screen):
        pygame.draw.circle(screen, "gray", (int(self.position.x), int(self.position.y)), self.radius)

    def update(self, dt):
        self.position += super().velocity * dt 
        