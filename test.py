"""
     CS5001_5003 Fall 2023 SV
     GreedyCat_test
     Jingjing Ji
"""
import unittest
from unittest.mock import Mock, patch
import pygame
from settings import *
from game.cube import cube
from game.cat import Cat
from game.utilities import drawGrid, drawWalls, randomSnack
from ui.display import display_score, redrawWindow

def create_key_event(key):
    """
    Helper function to create a simulated key press event.

    Args:
        key (int): The key code of the key being pressed.

    Returns:
        pygame.Event: The simulated key press event.
    """
    return pygame.event.Event(pygame.KEYDOWN, {key: True})

class TestCube(unittest.TestCase):

    def setUp(self):
        pygame.init()
        # Create a surface for drawing
        self.surface = pygame.display.set_mode((800, 600))
        
        # Initialize a cube object
        self.cube = cube((10, 10), 1, 0)

    def test_init(self):
        self.assertEqual(self.cube.pos, (10, 10))
        self.assertEqual(self.cube.dirnx, 1)
        self.assertEqual(self.cube.dirny, 0)

    def test_move(self):
        # Test movement in x-direction
        self.cube.move(1, 0)
        self.assertEqual(self.cube.pos, (11, 10))

        # Test movement in y-direction
        self.cube.move(0, 1)
        self.assertEqual(self.cube.pos, (11, 11))

    def test_create_rect(self):
        rect = self.cube.create_rect()
        self.assertIsInstance(rect, pygame.Rect)

    def test_rect_position(self):
        expected_x = self.cube.pos[0] * (self.cube.w // self.cube.rows) + 1
        expected_y = self.cube.pos[1] * (self.cube.w // self.cube.rows) + 1
        rect = self.cube.create_rect()
        self.assertEqual(rect.x, expected_x)
        self.assertEqual(rect.y, expected_y)

    def test_color(self):
        self.assertEqual(self.cube.color, ORANGE)


class TestCat(unittest.TestCase):

    def setUp(self):
        pygame.init()
        self.surface = pygame.display.set_mode((800, 600))  # Create a surface for drawing
        self.mock_hit_sound = Mock()  # Create a mock object for hit_sound
        self.cat = Cat(ORANGE, (10, 10), self.mock_hit_sound)  # Pass the mock object

    def test_init(self):
        self.assertEqual(self.cat.color, ORANGE)
        self.assertEqual(len(self.cat.body), 1)
        self.assertEqual(self.cat.score, 0)

    def test_play_hit_sound(self):
        hit_sound_played = False
        hit_sound_played = self.cat.play_hit_sound(hit_sound_played)
        self.assertTrue(hit_sound_played)
        self.mock_hit_sound.play.assert_called_once()

    @patch('pygame.event.get', return_value=[create_key_event(pygame.K_LEFT)])
    @patch('pygame.key.get_pressed', return_value = {pygame.K_LEFT: True})
    def test_move(self, mock_get, mock_get_pressed):
        self.cat.move()
        self.assertEqual(self.cat.dirnx, -1)
        self.assertEqual(self.cat.dirny, 0)

    def test_addCube(self):
        initial_length = len(self.cat.body)
        self.cat.addCube()
        self.assertEqual(len(self.cat.body), initial_length + 1)

    def test_reset(self):
        self.cat.addCube()
        self.cat.reset((5, 5))
        self.assertEqual(len(self.cat.body), 1)
        self.assertEqual(self.cat.body[0].pos, (5, 5))


class TestUtilities(unittest.TestCase):

    def setUp(self):
        pygame.init()
        self.surface = pygame.display.set_mode((800, 600))
        self.cat = Mock()
        self.cat.body = [cube((10, 10))]

    def test_randomSnack(self):
        walls = [pygame.Rect(0, 0, 50, 50)]  # Define some mock walls
        snack = randomSnack(32, self.cat, walls)

        # Check if the snack is not on the snake body
        for segment in self.cat.body:
            self.assertNotEqual(segment.pos, self.cat.pos)

        # Check if the snack is not colliding with walls
        self.assertFalse(any(snack.rect.colliderect(wall) for wall in walls))

    @patch('pygame.draw.line')
    def test_drawGrid(self, mock_draw_line):
        drawGrid(800, 20, self.surface)
        # Check if draw.line is called correct number of times
        self.assertEqual(mock_draw_line.call_count, 40)  # 20 vertical + 20 horizontal lines

    @patch('pygame.draw.rect')
    def test_drawWalls(self, mock_draw_rect):
        walls = [pygame.Rect(100, 100, 50, 50), pygame.Rect(200, 200, 50, 50)]
        drawWalls(walls, self.surface)
        # Check if draw.rect is called twice for two walls
        self.assertEqual(mock_draw_rect.call_count, 2)


class TestDisplayFunctions(unittest.TestCase):

    def setUp(self):
        pygame.init()
        self.mock_surface = Mock()
        self.surface = pygame.display.set_mode((800, 600))
        self.mock_cat = Mock()
        self.mock_cat = Mock()
        self.mock_icon_image = Mock()
        self.mock_cat.score = 10
        self.additional_score = 5
        self.snack_timer_duration = 5000
        self.walls = [pygame.Rect(100, 100, 50, 50)]

    @patch('pygame.font.SysFont')
    @patch('pygame.Surface.blit')
    def test_display_score(self, mock_blit, mock_sysfont):
        display_score(self.mock_cat, self.additional_score, self.snack_timer_duration, self.surface, self.mock_icon_image)
        self.assertTrue(mock_sysfont.called)
        self.assertEqual(mock_blit.call_count, 4)  # Check if blit is called 4 times

    @patch('pygame.Surface.fill')
    @patch('ui.display.drawGrid')
    @patch('ui.display.drawWalls')
    @patch('ui.display.display_score')
    def test_redrawWindow(self, mock_display_score, mock_draw_walls, mock_draw_grid, mock_fill):
        redrawWindow(self.surface, self.mock_cat, self.mock_snack, self.walls, self.additional_score, self.snack_timer_duration, self.mock_icon_image, self.surface)
        mock_fill.assert_called_once_with((0, 0, 0))
        mock_draw_grid.assert_called_once()
        mock_draw_walls.assert_called_once()
        mock_display_score.assert_called_once()


if __name__ == '__main__':
    unittest.main()
