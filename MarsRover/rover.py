class Rover:
    """Rover class with postion and instructions"""

    def __init__(self,
                 start: tuple,
                 direction: str,
                 instructions: str) -> None:
        self.position = start
        self.direction = direction
        self.instructions = instructions

    def __repr__(self) -> str:
        return f"Rover({self.position}, {self.instructions})"

    def __str__(self) -> str:
        return f"Rover({self.position}, {self.instructions})"
