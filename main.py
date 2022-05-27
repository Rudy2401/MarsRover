from MarsRover import Rover, RoverProcessing


def main():
    """Main function"""

    size = (5, 5)
    rovers = [
        Rover((1, 2, 'N'), 'LMLMLMLMM'),
        Rover((3, 3, 'E'), 'MMRMMRMRRM')
    ]
    rover_processing = RoverProcessing(rovers, size)
    rover_processing.check_rover_bounds(rovers[0].position)
    rover_processing.check_rover_bounds(rovers[1].position)
    rover_processing.move_rover()
    rover_processing.print_rovers()


if __name__ == '__main__':
    main()
