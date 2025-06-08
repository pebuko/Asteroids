import pygame
from constants import *
from circleshape import CircleShape

class Shot(CircleShape):
    def __init__(self, x, y, SHOT_RADIUS):
        super().__init__(x, y, SHOT_RADIUS)
        self.velocity = pygame.Vector2(0, 1)
        self.radius = SHOT_RADIUS

    def draw(self, screen):
        pygame.draw.circle(screen, "white", (int(self.position.x), int(self.position.y)), self.radius)

    def update(self, dt):
        self.position += self.velocity * PLAYER_SHOOT_SPEED * dt
        if not (0 <= self.position.x <= SCREEN_WIDTH and 0 <= self.position.y <= SCREEN_HEIGHT):
            self.kill()  # Remove the shot if it goes off-screen