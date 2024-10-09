import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *

def main():
    pygame.init()
    print("Starting asteroids!")
    print(f'Screen width: {SCREEN_WIDTH}')
    print(f'Screen height: {SCREEN_HEIGHT}')
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    state = True
    clock = pygame.time.Clock()
    dt = 0
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Player.containers = (updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    
    AsteroidField()
    player = Player(x, y)

    while state:
        screen.fill((0, 0, 0))

        for item in updatable:
            item.update(dt)
        
        for item in drawable:
            item.draw(screen)

        # Update the screen
        pygame.display.flip()

        # End game if player collides with asteroid
        for asteroid in asteroids:
            if asteroid.detect_collision(player):
                exit("Game over!")

        # Remove objects if a shot hits an asteroid
        for asteroid in asteroids:
            for shot in shots:
                if shot.detect_collision(asteroid):
                    shot.kill()
                    asteroid.kill()       

        # End loop when screen is closed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        delta = clock.tick(60)
        dt = delta / 1000

if __name__ == "__main__":
    main()