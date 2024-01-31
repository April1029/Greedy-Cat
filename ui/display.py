"""
     CS5001_5003 Fall 2023 SV
     GreedyCat_UI display
     Jingjing Ji
"""
import pygame
from settings import WHITE
from game.utilities import *
from settings import *

def display_score(cat, additional_score, snack_timer_duration, win, icon_image):
    """
    Displays the scores and cat icon (if available) on the game window.
    """
    font = pygame.font.SysFont("comicsans", 20)
    text = font.render("Ginkgo: " + str(cat.score), True, WHITE)
    additional_text = font.render("Moonpie: " + str(additional_score), True, WHITE)
    difficulty_level_text = font.render("Snatching the treat within a mere " + str(snack_timer_duration/1000) + " seconds!", True, WHITE)
    if icon_image:
        win.blit(icon_image, (0, 790))
        win.blit(icon_image, (0, 815))
    else:
        print("Error loading the cat icon.")
    win.blit(text, (70, 810))  # Display score at (10, 10) on the window
    win.blit(additional_text, (70, 835))  # Display score at (10, 30) on the window
    win.blit(difficulty_level_text, (350, 835))
    pygame.display.update()


def redrawWindow(surface, cat, snack, walls, additional_score, snack_timer_duration, icon_image, win):
    """
    Redraws the game window with updated elements.
    Parameters:
        surface (pygame.Surface): The surface to draw the game elements on.
    """
    surface.fill((0,0,0))
    cat.draw(surface)
    snack.draw(surface)
    drawGrid(width,rows, surface)
    drawWalls(walls, surface)
    display_score(cat, additional_score, snack_timer_duration, win, icon_image)
    pygame.display.update()
