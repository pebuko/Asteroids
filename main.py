import pygame
from constants import *
from circleshape import CircleShape
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from bullet import Shot
import sys
def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Asteroid.containers = (updatables, drawables, asteroids)
    Player.containers = (updatables, drawables)
    AsteroidField.containers = (updatables)
    Shot.containers = (shots,updatables, drawables)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    
    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
    
        screen.fill(0, rect=None, special_flags=0)
        for drawable in drawables:
            drawable.draw(screen)
              
        updatables.update(dt)

        for asteroid in asteroids:
            if asteroid.collides_with(player):
                print("Game over!")
                sys.exit()

            for shot in shots:
                if asteroid.collides_with(shot):
                    shot.kill()
                    asteroid.split()
     

        
        pygame.display.flip()
        
        dt = clock.tick(60) / 1000

    
    
if __name__ == "__main__":
    main()