from typing import List, Set
from .rover import Rover


class Plateau:
    """Plateau class with size and rovers"""

    def __init__(self, size: tuple, rovers: List[Rover]) -> None:
        self.size = size
        self.rovers = rovers
        self.occupied_positions = set()

    def __repr__(self) -> str:
        return f"Plateau({self.size}, Rovers: {self.rovers})"

    def __str__(self) -> str:
        return f"Plateau({self.size}, Rovers: {self.rovers})"

    def set_occupied_positions(self, rover: Rover) -> None:
        """Set occupied positions"""

        self.occupied_positions.add(rover.position)

    def get_occupied_positions(self) -> Set[tuple]:
        """Get occupied positions"""

        return self.occupied_positions

    def get_rovers(self) -> List[Rover]:
        """Get rovers"""

        return self.rovers
