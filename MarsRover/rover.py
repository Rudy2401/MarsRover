class Rover:
    """Rover class with postion and instructions"""

    def __init__(self, start: tuple, instructions: str) -> None:
        self.position = start
        self.instructions = instructions
