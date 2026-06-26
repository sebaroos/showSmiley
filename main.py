import pygame
import asyncio

pygame.init()

WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Smiley Face")

WHITE = (255, 255, 255)
YELLOW = (255, 223, 0)
BLACK = (0, 0, 0)
RED = (200, 50, 50)

clock = pygame.time.Clock()

def read_expression():
    try:
        with open("smiley.txt", "r") as f:
            return f.read().strip().lower()
    except:
        return "happy"


def draw_face(state):
    screen.fill(WHITE)

    # face base
    pygame.draw.circle(screen, YELLOW, (250, 250), 150)

    # eyes (same for all)
    pygame.draw.circle(screen, BLACK, (200, 200), 15)
    pygame.draw.circle(screen, BLACK, (300, 200), 15)

    # mouth changes
    if state == "happy":
        pygame.draw.arc(screen, BLACK, (170, 170, 160, 160), 0.2, 2.94, 5)

    elif state == "sad":
        pygame.draw.arc(screen, BLACK, (170, 220, 160, 160), 3.2, 6.0, 5)

    elif state == "angry":
        pygame.draw.line(screen, BLACK, (180, 320), (320, 320), 6)
        pygame.draw.line(screen, RED, (190, 260), (220, 240), 3)
        pygame.draw.line(screen, RED, (280, 240), (310, 260), 3)

    else:
        pygame.draw.line(screen, BLACK, (180, 300), (320, 300), 5)


async def main():
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        state = read_expression()
        draw_face(state)

        pygame.display.flip()

        clock.tick(60)
        await asyncio.sleep(0)

    pygame.quit()

asyncio.run(main())