import unittest
from ..MarsRover import Rover, RoverProcessing, Plateau


class TestRover(unittest.TestCase):
    """Test Rover class"""

    def test_rover_init(self):
        """Test rover init"""
        rover = Rover((1, 2), 'N', 'LMLMLMLMM')
        self.assertEqual(rover.position, (1, 2))
        self.assertEqual(rover.direction, 'N')
        self.assertEqual(rover.instructions, 'LMLMLMLMM')


class TestPlateau(unittest.TestCase):
    """Test Plateau class"""
    def test_plateau_init(self):
        """Test plateau init"""
        rovers = [Rover((1, 2), 'N', 'LMLMLMLMM'),
                  Rover((3, 3), 'E', 'MMRMMRMRRM')]
        plateau = Plateau((5, 5), rovers)
        self.assertEqual(plateau.size, (5, 5))
        self.assertEqual(plateau.rovers, rovers)


class TestRoverProcessing(unittest.TestCase):
    """Test RoverProcessing class"""

    def test_move_rover(self):
        """Test rover move"""

        rovers = [Rover((1, 2), 'N', 'LMLMLMLMM'),
                  Rover((3, 3), 'E', 'MMRMMRMRRM')]
        plateau = Plateau((5, 5), rovers)
        rover_processing = RoverProcessing(plateau)
        rover_processing.move_rover()
        self.assertEqual(rovers[0].position, (1, 3))
        self.assertEqual(rovers[1].position, (5, 1))
        self.assertEqual(rovers[0].direction, 'N')
        self.assertEqual(rovers[1].direction, 'E')

    def test_move_rover_exception(self):
        """Test rover move"""

        rovers = [Rover((1, 2), 'N', 'LMLMLMLMM'),
                  Rover((3, 3), 'E', 'MMRMMRMRRM'),
                  Rover((1, 3), 'E', 'MMRMMRMRRM')]
        plateau = Plateau((5, 5), rovers)
        rover_processing = RoverProcessing(plateau)
        self.assertRaises(ValueError, rover_processing.move_rover)

