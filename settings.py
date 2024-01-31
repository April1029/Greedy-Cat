"""
     CS5001_5003 Fall 2023 SV
     GreedyCat_settings
     Jingjing Ji
"""
import pygame

# Constants
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
ORANGE = (251, 133, 0)

# Screen dimensions and other settings
width = 800
rows = 32
grid_size = width / rows

# Define paths to sound files
snack_sound_file = "assets/sounds/greedycat_snack.mp3"
hit_sound_file = "assets/sounds/greedycat_hit.wav"
moonpie_snack_sound_file = "assets/sounds/greedycat_moonpiesnack.mp3"

# Sound volumes
background_volume = 0.1
snack_volume = 1.0
hit_volume = 0.2
moonpie_snack_volume = 1.0

# Wall Coordinates added here as pygame.Rect(x, y, width, height)
walls = [
    pygame.Rect(0, 300, 325, grid_size),
    pygame.Rect(600, 300, 200, grid_size),
    pygame.Rect(400, 300, 100, grid_size),
    pygame.Rect(400, 0, grid_size, 300),
    pygame.Rect(300, 400, grid_size, 400),
    pygame.Rect(600, 400, grid_size, 400),
    pygame.Rect(400, 400, 200, grid_size),
]

# Load the image/icon
icon_image = pygame.image.load("assets/images/greedycat.png")
icon_image.set_colorkey((0, 0, 0))
print(
    icon_image.get_width(), icon_image.get_height()
)  # Check to see if the image size needs to be adjusted
icon_size = (80, 80)  # Change to the size you prefer
icon_image = pygame.transform.scale(icon_image, icon_size)
