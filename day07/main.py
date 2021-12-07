def read_input_to_list(path):
    lines = []
    with open(path) as file:
        for line in file:
            lines = [int(x) for x in (line.rstrip().split(","))]

    lines.sort()
    return lines


def get_fuel(positions):
    median = positions[int(len(positions) / 2) - 1]

    total_fuel = 0
    for p in positions:
        total_fuel += abs(median - p)

    return total_fuel


def get_fuel_2(positions):
    total = 0
    for x in positions:
        total += x

    mean = int(total / len(positions))

    total_fuel = 0
    for p in positions:
        total_fuel += abs(mean - p) * (abs(mean - p) + 1) / 2

    return total_fuel


def main():
    inputs = read_input_to_list('input.txt')
    print(get_fuel_2(inputs))
    return


main()
