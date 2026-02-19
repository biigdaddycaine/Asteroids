import pygame
import sys
from constants import SCREEN_HEIGHT
from constants import SCREEN_WIDTH
from logger import log_state
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from logger import log_event
from shot import Shot


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    #creating the groups to be used in the game loop
    updatable = pygame.sprite.Group() 
    drawable = pygame.sprite.Group() # ****
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    #adding groups to classes
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = (updatable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable) #assigning the player class the groups it needs. Must be done before a Player object is created
    #creating the player object and asteroid spawner
    player = Player(x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2) 
    asteroid_spawn = AsteroidField()
    while True: #creates the game loop
        log_state()#call log state
        for event in pygame.event.get():#process event queue
             if event.type == pygame.QUIT:
                return
        screen.fill("black")#fill the screen
        updatable.update(dt) #calls the updat method on the 'updatable' group
        for a in asteroids: #loop to check collisions with ship
            if a.collides_with(player) == True:
                log_event("player_hit")
                print("Game Over")
                sys.exit()
        for a in asteroids:
            for s in shots:
                if s.collides_with(a) == True:
                    log_event("asteroid_shot")
                    a.split()
                    s.kill()

        for sprite in drawable: #loops through the drawable group and runs the draw method against each object
            sprite.draw(screen)                
        pygame.display.flip()#refresh display
        dt = clock.tick (60) / 1000 # ticks the clock. assigns dt to be the time bewteen frames. caps frame rate at 60
        

    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()
