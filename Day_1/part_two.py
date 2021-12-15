import time

# Consider sums of a three-measurement sliding window. How many sums are larger than the previous sum?


def read_input() -> list[int]:
    values = []
    with open('puzzle_input.txt') as f:
        for number in f.readlines():
            values.append(int(number))

    return values

def calculate_windows(values: list[int]) -> list[int]:
    windows = []
    for index in range(len(values)):
        if index + 2 < len(values):
            windows.append(values[index] + values[index+1] + values[index+2])
    return windows

def calculate_result(windows: list[int]) -> int:
    result = 0
    for index in range(len(windows[1:])):
        if windows[index+1] > windows[index]:
            result += 1
    return result


if __name__ == '__main__':
    start = time.time()
    input_values = read_input()
    three_measurement_windows = calculate_windows(input_values)
    output = calculate_result(three_measurement_windows)
    end = time.time()
    print(f'The amount of measurements which were larger than a previous measurement are {output}\n'
          f'It took {end - start} seconds')
