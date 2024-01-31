"""
     CS5001_5003 Fall 2023 SV
     GreedyCat_gamelogic_utilities
     Jingjing Ji
"""
import pygame
import random
from game.cube import cube
from settings import *


def drawGrid(w, rows, surface):
    """
    Draws a grid on the given surface.
    Args:
        w (int): Width of the surface.
        rows (int): Number of rows in the grid.
        surface (pygame.Surface): The surface on which the grid will be drawn.
    """
    sizeBtwn = w // rows

    x = 0
    y = 0
    for l in range(rows):
        x = x + sizeBtwn
        y = y + sizeBtwn
        # draw horizontal line and vertical line in each loop
        pygame.draw.line(surface, (255, 255, 255), (x, 0), (x, w))
        pygame.draw.line(surface, (255, 255, 255), (0, y), (w, y))


def drawWalls(walls, win):
    """
    Draws walls on the game window.

    Args:
    walls (list of pygame.Rect): A list of Rect objects representing walls.
    win (pygame.Surface): The game window surface.
    """
    for wall in walls:
        pygame.draw.rect(win, WHITE, wall)


def randomSnack(rows, item, walls):
    """
    Generates a random snack on the game grid, ensuring it doesn't collide with the snake or walls.

    Args:
        rows (int): Number of rows in the game grid.
        item (snake): The snake object.
        walls (list of pygame.Rect): List of wall objects.

    Returns:
        Cube: A cube object representing the generated snack.
    """
    positions = item.body

    while True:
        x = random.randrange(rows)
        y = random.randrange(rows)
        snack = cube((x, y), color=GREEN)
        # Check for collision with snake body or walls
        collide_with_snake = len(list(filter(lambda z: z.pos == (x, y), positions))) > 0
        collide_with_wall = any(snack.rect.colliderect(wall) for wall in walls)

        if (not collide_with_snake) and (not collide_with_wall):
            return snack
