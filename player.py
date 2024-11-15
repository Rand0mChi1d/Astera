import pygame

from circleshape import CircleShape
from constants import *

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.cooldwn = 0

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), width = 2)

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
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()

        if self.cooldwn - dt >= 0:
            self.cooldwn -= dt
        else:
            self.cooldwn = 0

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        if self.cooldwn > 0:
            pass
        elif self.cooldwn == 0:
            new_shot = Shot(self.position)
            new_shot.current_direction = pygame.Vector2(0, 1).rotate(self.rotation)
            self.cooldwn = PLAYER_SHOOT_COOLDOWN

        

class Shot(CircleShape):
    def __init__(self, position):
        super().__init__(position[0], position[1], SHOT_RADIUS)

    def draw(self, screen):
        pygame.draw.circle(screen, "red", self.position, self.radius, width = 1)

    def update(self, dt):
        self.position += self.current_direction * PLAYER_SHOOT_SPEED * dt