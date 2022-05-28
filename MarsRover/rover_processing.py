from .plateau import Plateau


EAST = 'E'
NORTH = 'N'
SOUTH = 'S'
WEST = 'W'
MOVE = 'M'
LEFT = 'L'
RIGHT = 'R'

DIRECTION_MAP = {
    (NORTH, LEFT): WEST,
    (NORTH, RIGHT): EAST,
    (SOUTH, LEFT): EAST,
    (SOUTH, RIGHT): WEST,
    (EAST, LEFT): NORTH,
    (EAST, RIGHT): SOUTH,
    (WEST, LEFT): SOUTH,
    (WEST, RIGHT): NORTH
}

MOVE_MAP = {
    NORTH: (0, 1),
    SOUTH: (0, -1),
    EAST: (1, 0),
    WEST: (-1, 0)
}


class RoverProcessing:
    def __init__(self, plateau: Plateau) -> None:
        self.plateau = plateau

    def check_rover_bounds(self, position: tuple) -> bool:
        """Check if initial position of rover is out of bounds"""

        max_x = self.plateau.size[0]
        max_y = self.plateau.size[1]
        sx = position[0]
        sy = position[1]
        if sx < 0 or sx > max_x or sy < 0 or sy > max_y:
            return False
        return True

    def move_rover(self) -> None:
        """Move rover according to instructions"""

        for rover in self.plateau.get_rovers():
            # Get current position of rover
            sx = rover.position[0]
            sy = rover.position[1]

            # Check if current position is occupied
            self.check_if_occupied((sx, sy))
            direction = rover.direction
            for instruction in rover.instructions:
                next_move = (direction, instruction)
                if next_move in DIRECTION_MAP:
                    # Get next direction if in bounds
                    direction = DIRECTION_MAP[next_move]
                elif instruction == MOVE:
                    # Get next position if in bounds
                    dx = sx + MOVE_MAP[direction][0]
                    dy = sy + MOVE_MAP[direction][1]
                    if self.check_rover_bounds((dx, dy)):
                        sx = dx
                        sy = dy
                else:
                    # Invalid instruction
                    raise ValueError(f"Invalid instruction: {instruction}")
            rover.position = (sx, sy)
            rover.direction = direction
            self.plateau.set_occupied_positions(rover)

    def check_if_occupied(self, position: tuple) -> None:
        """Check if position is occupied and raise Error"""

        if position in self.plateau.get_occupied_positions():
            raise ValueError(f"Rover {position} is already occupied")

    def print_rovers(self) -> None:
        """Print current position of rovers"""

        for rover in self.plateau.get_rovers():
            print(f'{rover.position[0]} {rover.position[1]} {rover.direction}')
