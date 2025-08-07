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

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill("black")
        player.draw(screen) # Draw the player
        player.update(dt) # Update the player based on input and time
        pygame.display.flip() # Update the display
        dt = clock.tick(60) / 1000 # limit the framerate to 60 FPS

if __name__ == "__main__":
    main()
