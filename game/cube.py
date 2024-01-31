"""
     CS5001_5003 Fall 2023 SV
     GreedyCat_gamelogic_cube
     Jingjing Ji
"""
import pygame
from settings import ORANGE, WHITE, grid_size


class cube(object):
    """
    Represents a cube object in the game(cat object contains the cube object)
    Attributes:
        pos (tuple): The position of the cube on the grid.
        dirnx (int): The horizontal direction of the cube's movement.
        dirny (int): The vertical direction of the cube's movement.
        color (tuple): The color of the cube.
        score (int): The score associated with the cube.
        snack_eaten (bool): Indicates whether a snack has been eaten by the cube.
        rect (pygame.Rect): The rectangle representing the cube's position and size on the screen.
    Methods:
        __init__(self, start, dirnx=1, dirny=0, color=ORANGE):
            Initializes a cube object with a starting position, direction, and color.
        move(self, dirnx, dirny):
            Moves the cube in the specified direction.
        create_rect(self):
            Creates a Pygame Rect object representing the cube.
        draw(self, surface, eyes=False):
            Draws the cube on the specified surface with optional 'eyes'.
    """

    rows = 32
    w = 800

    def __init__(self, start, dirnx=1, dirny=0, color=ORANGE):
        self.pos = start
        self.dirnx = 1
        self.dirny = 0
        self.color = color
        self.score = 0
        self.snack_eaten = False
        self.rect = self.create_rect()

    def move(self, dirnx, dirny):
        """
        Moves the cube in the specified direction.

        Args:
            dirnx (int): The horizontal direction of movement.
            dirny (int): The vertical direction of movement.
        """
        self.dirnx = dirnx
        self.dirny = dirny
        self.pos = (self.pos[0] + self.dirnx, self.pos[1] + self.dirny)
        self.rect = self.create_rect()

    def create_rect(self):
        """
        Creates a pygame.Rect object representing the cube's position and size.

        Returns:
            pygame.Rect: The rectangle representing the cube.
        """
        dis = self.w // self.rows
        i = self.pos[0]
        j = self.pos[1]
        return pygame.Rect(i * dis + 1, j * dis + 1, dis - 2, dis - 2)

    def draw(self, surface, eyes=False):
        """
        Draws the cube on the specified surface. Optionally draws eyes, ears and whiskers to represent a cat's head.

        Args:
            surface (pygame.Surface): The surface on which to draw the cube.
            eyes (bool): If True, draws eyes, ears and whiskers on the cube.
        """
        dis = self.w // self.rows
        i = self.pos[0]
        j = self.pos[1]
        # make sure the drawn grid does not take the whole space of the grid, the edge can still be seen
        pygame.draw.rect(surface, self.color, self.rect)

        if eyes:
            # Drawing eyes and additional features (whiskers, ears) to represent a cat
            centre = dis // 2
            radius = 3
            circleMiddle = (i * dis + centre - radius, j * dis + 6)
            circleMiddle2 = (i * dis + dis - radius * 2, j * dis + 6)
            pygame.draw.circle(surface, (0, 0, 0), circleMiddle, radius)
            pygame.draw.circle(surface, (0, 0, 0), circleMiddle2, radius)

            # Draw whiskers (lines)
            whisker1_start = (i * dis + 17, j * dis + 10)
            whisker1_end = (i * dis + 25, j * dis + 10)
            whisker2_start = (i * dis + 17, j * dis + 15)
            whisker2_end = (i * dis + 25, j * dis + 15)
            whisker3_start = (i * dis, j * dis + 10)
            whisker3_end = (i * dis + 8, j * dis + 10)
            whisker4_start = (i * dis, j * dis + 15)
            whisker4_end = (i * dis + 8, j * dis + 15)

            pygame.draw.line(surface, (0, 0, 0), whisker1_start, whisker1_end, 2)
            pygame.draw.line(surface, (0, 0, 0), whisker2_start, whisker2_end, 2)
            pygame.draw.line(surface, (0, 0, 0), whisker3_start, whisker3_end, 2)
            pygame.draw.line(surface, (0, 0, 0), whisker4_start, whisker4_end, 2)

            # Draw cat ears
            ear_width = 10
            ear_height = 10
            ear1_bottom_left = (i * dis + 25 - ear_width, j * dis)
            ear1_bottom_right = (i * dis + 25, j * dis)
            ear1_top = (i * dis + 17.5, j * dis - ear_height * 0.5)
            ear2_bottom_left = (i * dis, j * dis)
            ear2_bottom_right = (i * dis + ear_width, j * dis)
            ear2_top = (i * dis + 2.5, j * dis - ear_height * 0.5)
            pygame.draw.polygon(
                surface, WHITE, [ear1_bottom_left, ear1_bottom_right, ear1_top]
            )
            pygame.draw.polygon(
                surface, WHITE, [ear2_bottom_left, ear2_bottom_right, ear2_top]
            )
