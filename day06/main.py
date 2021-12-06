def read_input_to_list(path):
    lines = []
    with open(path) as file:
        for line in file:
            lines = [int(x) for x in (line.rstrip().split(","))]
    fish = {}
    for j in range(9):
        fish[j] = 0
    for f in lines:
        fish[f] += 1

    return fish


def get_fish(fish):
    total_fish = 0

    for j in range(8):
        total_fish += fish[j]

    i = 0

    while (i < 256):
        j = 0
        temp = fish[0]

        while (j < 8):
            fish[j] = fish[j + 1]
            j += 1

        fish[8] = temp
        fish[6] += temp

        total_fish += fish[8]

        i += 1

    return total_fish


def main():
    inputs = read_input_to_list('input.txt')
    print(get_fish(inputs))
    return


main()
