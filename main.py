# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *
from asteroidfield import *

def main():
    print(f"Starting asteroids!")
    print(f"Screen width:", SCREEN_WIDTH)
    print(f"Screen height:", SCREEN_HEIGHT)
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (updateable, drawable)
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = (updateable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)
    print(f"updeatable: {updateable.sprites()}")
    print(f"drawable: {drawable.sprites()}")
    asteroidfield = AsteroidField()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))
        for element in updateable:
            element.update(dt)
        for element in drawable:
            element.draw(screen)
        #player.update(dt)
        #player.draw(screen)
        for asteroid in asteroids:
            if asteroid.collision(player):
                print("Game over!")
                return 1
        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
