import pygame
from constants import *
from player import Player

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # Set the screen size
    clock = pygame.time.Clock() # Create a clock to manage frame rate
    dt = 0 # Delta time for smooth movement
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2) # Create a player instance
    updatable = pygame.sprite.Group(player) # Group for updating sprites
    drawable = pygame.sprite.Group(player) # Group for drawing sprites


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill("black")
        updatable.update(dt) # Update all updatable sprites
        for sprite in drawable:
            sprite.draw(screen) # Draw all drawable sprites
        pygame.display.flip() # Update the display
        dt = clock.tick(60) / 1000 # limit the framerate to 60 FPS

if __name__ == "__main__":
    main()
