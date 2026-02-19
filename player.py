import pygame 
from circleshape import CircleShape
from constants import PLAYER_RADIUS
from constants import PLAYER_TURN_SPEED
from constants import PLAYER_SPEED
from constants import LINE_WIDTH
from shot import Shot
from constants import PLAYER_SHOOT_SPEED
from constants import SHOT_RADIUS
from constants import PLAYER_SHOOT_COOLDOWN_SECONDS

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shot_timer = 0
    # in the Player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    def rotate(self, dt):
       result = PLAYER_TURN_SPEED * dt 
       self.rotation += result
       return self.rotation
    def move(self, dt):
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * dt
        self.position += rotated_with_speed_vector
    def update(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_SPACE]:
            if self.shot_timer > 0:
                pass
            else:
                self.shot_timer = PLAYER_SHOOT_COOLDOWN_SECONDS            
                Player.shoot(self)
        self.shot_timer -= dt        
    def draw(self, screen):
        #overriding draw method
        pygame.draw.polygon(screen, "white", self.triangle(), LINE_WIDTH)
    def shoot(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        spawn_position = self.position + forward * PLAYER_RADIUS
        shot = Shot(spawn_position.x, spawn_position.y, SHOT_RADIUS)
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        shot.velocity = rotated_vector * PLAYER_SHOOT_SPEED