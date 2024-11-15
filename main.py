import pygame

from constants import *
from player import *
from circleshape import *
from asteroid import *
from asteroidfield import AsteroidField

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0 
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()
    while not False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))
        for item in drawable:
            item.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60)/1000 
        for item in updatable:
            item.update(dt)
        for item in asteroids:
            if item.check_coll(player):
                print("Game over!")
                return
        for item in asteroids:    
            for bullet in shots:
                if item.check_coll(bullet):
                    item.split()
                    bullet.kill()

updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
shots = pygame.sprite.Group()

Player.containers = (updatable, drawable)
Asteroid.containers = (updatable, drawable, asteroids)
AsteroidField.containers = (updatable)
Shot.containers = (updatable, drawable, shots)

if __name__ == "__main__":
    main() 
