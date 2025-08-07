import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable) # Asteroid objects will be added to these groups
    AsteroidField.containers = updatable # AsteroidField will update itself
    asteroid_field = AsteroidField() # Create an instance of AsteroidField

    Player.containers = (updatable, drawable) # Player objects will be added to these groups

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2) # Create a player at the center of the screen

    dt = 0 # Initialize delta time

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # Exit the game and kill the process when the window is closed
                return

        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.collides_with(player):
                print("Game over!")
                sys.exit()

        screen.fill("black")

        for sprite in drawable:
            sprite.draw(screen)

        pygame.display.flip() # Update the display

        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
