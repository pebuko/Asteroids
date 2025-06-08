import pygame
from constants import *
from circleshape import CircleShape


class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt    

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
            
        if keys[pygame.K_d]:
            self.rotate(dt)\

    def move(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.velocity += pygame.Vector2(0, PLAYER_SPEED * dt).rotate(self.rotation)
        elif keys[pygame.K_s]:
            self.velocity += pygame.Vector2(0, -PLAYER_SPEED * dt).rotate(self.rotation)

        self.position += self.velocity * dt
                

        