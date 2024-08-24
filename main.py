# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *

def main():
    print(f"Starting asteroids!")
    print(f"Screen width:", SCREEN_WIDTH)
    print(f"Screen height:", SCREEN_HEIGHT)
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)
    updateable = pygame.sprite.Group(player)
    drawable = pygame.sprite.Group(player)
    player.containers = (updateable, drawable)
    print(f"updeatable: {updateable.sprites()}")
    print(f"drawable: {drawable.sprites()}")
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
        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
