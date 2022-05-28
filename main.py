from MarsRover import Rover, RoverProcessing, Plateau


def convert_input_to_rovers(input_string):
    """Convert input string to rovers"""

    # Split input string into lines
    lines = input_string.splitlines()
    # Get plateau size
    plateau_size = lines[0].split()
    # Get rovers
    rovers = []
    for i in range(1, len(lines)-1, 2):
        line1 = lines[i]
        line2 = lines[i+1]
        # Split line into position and instructions
        x, y, direction = line1.split()
        instructions = line2
        # Create rover
        rover = Rover((int(x), int(y)), direction, instructions)
        # Add rover to rovers list
        rovers.append(rover)
    # Create plateau
    plateau = Plateau((int(plateau_size[0]), int(plateau_size[1])), rovers)
    # Create rover processing
    rover_processing = RoverProcessing(plateau)
    return rover_processing, rovers


def main():
    """Main function"""

    stream = """5 5
1 2 N
LMLMLMLMM
3 3 E
MMRMMRMRRM"""

    # Create rover processing
    rover_processing, rovers = convert_input_to_rovers(stream)

    # Check rover bounds
    for rover in rovers:
        rover_processing.check_rover_bounds(rover.position)

    # Move rovers
    rover_processing.move_rover()
    # Print rovers
    rover_processing.print_rovers()


if __name__ == '__main__':
    main()
