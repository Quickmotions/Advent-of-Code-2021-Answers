import time


# What do you get if you multiply your final horizontal position by your final depth?

def read_input() -> list[list[str, int]]:
    commands = []
    with open('puzzle_input.txt') as f:
        for line in f.readlines():
            command, value = line.strip().split()
            commands.append([str(command), int(value)])

    return commands


def calculate_location(commands: list[list[str, int]]):
    current_depth = 0
    current_position = 0
    for direction, value in commands:
        if direction == 'forward':
            current_position += value
        elif direction == 'down':
            current_depth += value
        elif direction == 'up':
            current_depth -= value
    return current_depth, current_position


if __name__ == '__main__':
    start = time.time()
    command_list = read_input()
    depth, position = calculate_location(command_list)
    end = time.time()
    print(f'Final co-ordinates:\nposition = {position}\ndepth = {depth}\nAnswer = {position * depth}\n'
          f'Took {end - start} seconds')
