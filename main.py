"""
     CS5001_5003 Fall 2023 SV
     GreedyCat_main
     Jingjing Ji
"""
import pygame
import time

# Initialize Pygame and its modules
pygame.init()
pygame.mixer.init()

from settings import *
from game.cat import Cat
from game.utilities import randomSnack, drawGrid, drawWalls
from ui.display import display_score, redrawWindow


def main():
    """
    The main function of the ggreedy cat game. It initializes the game environment,
    handles the game loop including the movements, body growth, and collisions.
    It also manages the game's score and level difficulty.
    """
    additional_score = 0
    snack_timer = pygame.time.get_ticks()

    # Load the background music
    background_music = "assets/sounds/greedycat_bg.wav"
    pygame.mixer.music.load(background_music)
    pygame.mixer.music.play(-1)  # '-1' plays the music in an infinite loop

    # Load sound effects
    snack_sound = pygame.mixer.Sound(snack_sound_file)
    hit_sound = pygame.mixer.Sound(hit_sound_file)
    moonpie_snack_sound = pygame.mixer.Sound(moonpie_snack_sound_file)

    # Flags to control sound play
    snack_sound_played = False
    hit_sound_played = False
    moonpie_snack_sound_played = False

    # Gsme window initialization
    win = pygame.display.set_mode((width, width + 100))
    cat = Cat(ORANGE, (10, 10), hit_sound)
    snack = randomSnack(rows, cat, walls)

    flag = True
    clock = pygame.time.Clock()
    delay = 50  # Initial delay

    # Set initial snack timer duration
    snack_timer_duration = 5000

    while flag:
        current_time = pygame.time.get_ticks()
        pygame.time.delay(50)
        clock.tick(10)
        cat.move()

        """ Here is the level of difficulty adjustment:
        when either Ginkgo or Moonpie reaches a score of 10,
        let's reset the scores for both and change the level of difficulty accordingly.
        (if Ginkgo reaches 10, snack_timer_duration becomes smaller, or
        if Moonpie reaches 10, snack_timer_duration becomes bigger)
        """
        if cat.score >= 10 or additional_score >= 10:
            if cat.score >= 10:
                snack_timer_duration = snack_timer_duration - 1000
                cat.score = 0
                additional_score = 0
            elif additional_score >= 10:
                snack_timer_duration = snack_timer_duration + 1000
                additional_score = 0
                cat.score = 0
        """ Here is the snack consumption logicL
        if Ginkgo hits the snack within the timeframe of
        snack_timer_duration, the length grows in one cube,
        add one point, otherwise, Moonpie gets the snack and the point.
        """
        if current_time - snack_timer <= snack_timer_duration:
            if cat.body[0].pos == snack.pos:
                if not snack_sound_played:
                    snack_sound.play()
                    snack_sound_played = True
                cat.addCube()
                snack = randomSnack(rows, cat, walls)
                snack_timer = current_time  # Reset the timer
                snack_sound_played = False  # Reset the flag to play sound again
        elif current_time - snack_timer > snack_timer_duration:
            additional_score += 1  # Increment the additional score
            if not moonpie_snack_sound_played:
                moonpie_snack_sound.play()
                moonpie_snack_sound_played = True
                moonpie_snack_sound_played = False
            snack = randomSnack(rows, cat, walls)  # Update the snack position
            snack_timer = current_time  # Reset the timer
        redrawWindow(
            win,
            cat,
            snack,
            walls,
            additional_score,
            snack_timer_duration,
            icon_image,
            win,
        )


if __name__ == "__main__":
    try:
        main()
    except OSError as e:
        print("Error!", e)
