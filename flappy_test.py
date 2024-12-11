from ple import PLE
from ple.games.flappybird import FlappyBird
import pygame

# Create the Flappy Bird game instance
game = FlappyBird()

# Initialize PLE with the game, enabling display_screen to visualize the game
p = PLE(game, fps=30, display_screen=True)
p.init()

running = True
while running:
    if p.game_over():
        p.reset_game()

    # Perform a no-operation action just to run the game
    p.act(p.NOOP)

    # Handle pygame events to allow window closure
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
