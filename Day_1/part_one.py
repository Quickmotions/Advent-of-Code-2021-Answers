import time

# find out how many measurements are larger than the previous one


def read_input() -> list[int]:
    values = []
    with open('puzzle_input.txt') as f:
        for number in f.readlines():
            values.append(int(number))

    return values

def find_answer(values: list[int]) -> int:
    result = 0
    for index in range(len(values[1:])):
        if values[index+1] > values[index]:
            result += 1
    return result


if __name__ == '__main__':
    start = time.time()
    input_values = read_input()
    output = find_answer(input_values)
    end = time.time()
    print(f'The amount of measurements which were larger than a previous measurement are {output}\n'
          f'It took {end - start} seconds')
