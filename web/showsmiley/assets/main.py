import pygame
import asyncio

pygame.init()

# Screen settings
WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Smiley Face")

# Colors
WHITE = (255, 255, 255)
YELLOW = (255, 223, 0)
BLACK = (0, 0, 0)

clock = pygame.time.Clock()

async def main():
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Draw background
        screen.fill(WHITE)

        # Face
        pygame.draw.circle(screen, YELLOW, (250, 250), 150)

        # Eyes
        pygame.draw.circle(screen, BLACK, (200, 200), 15)
        pygame.draw.circle(screen, BLACK, (300, 200), 15)

        # Smile
        pygame.draw.arc(screen, BLACK, (170, 170, 160, 160), 0.2, 2.94, 5)

        pygame.display.flip()

        # IMPORTANT for pygbag (lets browser run properly)
        clock.tick(60)
        await asyncio.sleep(0)

    pygame.quit()

asyncio.run(main())