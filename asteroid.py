import pygame
import random
from constants import LINE_WIDTH
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    def draw(self, screen):
        # override        
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
    def update(self, dt):
        result = self.velocity * dt
        self.position += result
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            random_angle = random.uniform(20, 50)
            new_velocity_one = self.velocity.rotate(random_angle)
            new_velocity_two = self.velocity.rotate(-random_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            asto_one = Asteroid(self.position.x, self.position.y, new_radius)
            asto_two = Asteroid(self.position.x, self.position.y, new_radius)
            asto_one.velocity = new_velocity_one * 1.2
            asto_two.velocity = new_velocity_two * 1.2