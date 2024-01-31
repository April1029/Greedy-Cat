"""
     CS5001_5003 Fall 2023 SV
     GreedyCat_gamelogic_cat
     Jingjing Ji
"""
import pygame
import time
from game.cube import cube
from settings import *


class Cat:
    """
    Represents the cat object in the game.

    Attributes:
        color (tuple): The color of the cat.
        head (Cube): The head cube of the cat.
        body (list of Cube): The list of cubes forming the cat's body.
        dirnx (int): The horizontal direction of the cat's movement.
        dirny (int): The vertical direction of the cat's movement.
        score (int): The score of the cat.
        hit_sound (pygame.mixer.Sound): The sound played when the cat hits an obstacle.

    Methods:
        __init__(self, color, pos):
            Initializes the cat object with a color and starting position.
        move(self):
            Moves the cat based on keyboard inputs and handles collisions.
        reset(self, pos):
            Resets the cat's position and attributes to start.
        addCube(self):
            Adds a cube to the cat's body.
        draw(self, surface):
            Draws the cat on the specified surface.
    """

    body = []
    turns = {}
    rows = 32

    def __init__(self, color, pos, hit_sound):
        self.color = color
        self.head = cube(pos)
        self.body = [self.head]
        self.dirnx = 0
        self.dirny = 1
        self.score = 0
        self.hit_sound = hit_sound

    def play_hit_sound(self, hit_sound_played):
        """
        Plays the hit sound effect.

        Args:
            hit_sound_played (bool): Flag indicating whether the sound has already been played.

        Returns:
            bool: Updated flag indicating whether the sound has been played.
        """
        if not hit_sound_played:
            self.hit_sound.play()
            hit_sound_played = True
            time.sleep(0.5)
        return hit_sound_played

    def move(self):
        """
        Handles the movement of the cat based on keyboard input and checks for collisions.
        """
        ##        global hit_sound_played
        hitting = False
        for event in pygame.event.get():
            if hitting:
                continue
            if event.type == pygame.QUIT:
                pygame.quit()

            # Code for handling key presses and setting direction
            keys = pygame.key.get_pressed()
            for key in keys:
                if keys[pygame.K_LEFT]:
                    self.dirnx = -1
                    self.dirny = 0
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

                elif keys[pygame.K_RIGHT]:
                    self.dirnx = 1
                    self.dirny = 0
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

                elif keys[pygame.K_UP]:
                    self.dirnx = 0
                    self.dirny = -1
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

                elif keys[pygame.K_DOWN]:
                    self.dirnx = 0
                    self.dirny = 1
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

        hit_sound_played = False
        # Body movement logic
        for i, c in enumerate(self.body):
            p = c.pos[:]

            if p in self.turns:
                turn = self.turns[p]
                c.move(turn[0], turn[1])
                # remove from the list to stop after the one last cube turns
                if i == len(self.body) - 1:
                    self.turns.pop(p)
            # if hit the edge of the screen or preset-walls, then bounce back, else, continue to move as directed
            else:
                if c.dirnx == -1 and c.pos[0] <= 0:
                    if i == 0:
                        hit_sound_played = self.play_hit_sound(hit_sound_played)
                    c.dirnx *= -1
                elif c.dirnx == 1 and c.pos[0] >= c.rows - 1:
                    if i == 0:
                        hit_sound_played = self.play_hit_sound(hit_sound_played)
                    c.dirnx *= -1
                elif c.dirny == 1 and c.pos[1] >= c.rows - 1:
                    if i == 0:
                        hit_sound_played = self.play_hit_sound(hit_sound_played)
                    c.dirny *= -1
                elif c.dirny == -1 and c.pos[1] <= 0:
                    if i == 0:
                        hit_sound_played = self.play_hit_sound(hit_sound_played)
                    c.dirny *= -1
                else:
                    for wall in walls:
                        xl = wall.left
                        xh = wall.left + wall.width
                        yl = wall.top
                        yh = wall.top + wall.height
                        x = c.pos[0] * grid_size
                        y = c.pos[1] * grid_size
                        xm = x + grid_size / 2
                        ym = y + grid_size / 2
                        if (
                            c.dirnx == 1
                            and x + grid_size == xl
                            and ym >= yl
                            and ym <= yh
                        ):
                            if i == 0:
                                hit_sound_played = self.play_hit_sound(hit_sound_played)
                            c.dirnx *= -1
                        elif c.dirnx == -1 and x == xh and ym >= yl and ym <= yh:
                            if i == 0:
                                hit_sound_played = self.play_hit_sound(hit_sound_played)
                            c.dirnx *= -1
                        elif (
                            c.dirny == 1
                            and y + grid_size == yl
                            and xm >= xl
                            and xm <= xh
                        ):
                            if i == 0:
                                hit_sound_played = self.play_hit_sound(hit_sound_played)
                            c.dirny *= -1
                        elif (
                            c.dirny == -1
                            and y - grid_size == yl
                            and xm >= xl
                            and xm <= xh
                        ):
                            if i == 0:
                                hit_sound_played = self.play_hit_sound(hit_sound_played)
                            c.dirny *= -1
                    c.move(c.dirnx, c.dirny)

    def reset(self, pos):
        """
        Resets the cat to the starting position and attributes.

        Args:
            pos (tuple): The starting position for the reset cat.
        """
        self.head = cube(pos)
        self.body = []
        self.body.append(self.head)
        self.turns = {}
        self.dirnx = 0
        self.dirny = 1

    def addCube(self):
        """
        Adds a new cube to the cat's body, extending its length.
        """
        tail = self.body[-1]
        dx, dy = tail.dirnx, tail.dirny
        # check the moving direction first, and then add the snack cube to the tail
        if dx == 1 and dy == 0:
            self.body.append(cube((tail.pos[0] - 1, tail.pos[1])))
        elif dx == -1 and dy == 0:
            self.body.append(cube((tail.pos[0] + 1, tail.pos[1])))
        elif dx == 0 and dy == 1:
            self.body.append(cube((tail.pos[0], tail.pos[1] - 1)))
        elif dx == 0 and dy == -1:
            self.body.append(cube((tail.pos[0], tail.pos[1] + 1)))
        # make the added snack cube to move in the same driection as the rest of the body
        self.body[-1].dirnx = dx
        self.body[-1].dirny = dy
        self.score += 1

    def draw(self, surface):
        """
        Draws the cat on the given surface.

        Args:
            surface (pygame.Surface): The surface on which to draw the cat.
        """
        # if it is the first cube, add eyes to it
        for i, c in enumerate(self.body):
            if i == 0: 
                c.draw(surface, True)
            else:
                c.draw(surface)
