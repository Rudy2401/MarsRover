import unittest
from ..MarsRover import Rover, RoverProcessing


class TestRover(unittest.TestCase):
    """Test Rover class"""

    def test_rover_init(self):
        """Test rover init"""
        rover = Rover((1, 2, 'N'), 'LMLMLMLMM')
        self.assertEqual(rover.position, (1, 2, 'N'))
        self.assertEqual(rover.instructions, 'LMLMLMLMM')


class TestRoverProcessing(unittest.TestCase):
    """Test RoverProcessing class"""

    def test_rover_bounds(self):
        """Test rover bounds"""
        size = (5, 5)
        rovers = [
            Rover((1, 2, 'N'), 'LMLMLMLMM'),
            Rover((3, 3, 'E'), 'MMRMMRMRRM')
        ]
        rover_processing = RoverProcessing(rovers, size)
        rover_processing.check_rover_bounds(rovers[0].position)
        rover_processing.check_rover_bounds(rovers[1].position)
        self.assertTrue(True)

    def test_move_rover(self):
        """Test rover move"""

        size = (5, 5)
        rovers = [
            Rover((1, 2, 'N'), 'LMLMLMLMM'),
            Rover((3, 3, 'E'), 'MMRMMRMRRM')
        ]
        rover_processing = RoverProcessing(rovers, size)
        rover_processing.move_rover()
        self.assertTrue(rovers[0].position == (1, 3, 'N'))
        self.assertTrue(rovers[1].position == (5, 1, 'E'))

    def test_move_rover_exception(self):
        """Test rover move"""

        size = (5, 5)
        rovers = [
            Rover((1, 2, 'N'), 'LMLMLMLMM'),
            Rover((3, 3, 'E'), 'MMRMMRMRRM'),
            Rover((1, 3, 'E'), 'MMRMMRMRRM')
        ]
        rover_processing = RoverProcessing(rovers, size)
        self.assertRaises(ValueError, rover_processing.move_rover)

    def test_print_rovers(self):
        """Test rover print"""

        size = (5, 5)
        rovers = [
            Rover((1, 2, 'N'), 'LMLMLMLMM'),
            Rover((1, 3, 'E'), 'MMRMMRMRRM')
        ]
        rover_processing = RoverProcessing(rovers, size)
        rover_processing.print_rovers()
        self.assertTrue(True)
