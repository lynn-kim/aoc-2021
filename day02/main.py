def read_input_to_list(path):
    lines = []
    with open(path) as file:
        for line in file:
            lines.append(line.rstrip())
    return lines


def calculate_final_position_1(directions):
    hor = 0  
    depth = 0  
    for d in directions:
        d = d.split(' ')
        direction = d[0]
        mag = int(d[1])
        if (direction == "forward"):
            hor += mag
        elif (direction == "down"):
            depth += mag
        elif (direction == "up"):
            depth -= mag

    return hor * depth


def calculate_final_position_2(directions):
    hor = 0  
    depth = 0  
    aim = 0
    for d in directions:
        d = d.split(' ')
        direction = d[0]
        mag = int(d[1])
        if (direction == "forward"):
            hor += mag
            depth += mag * aim
        elif (direction == "down"):
            aim += mag
        elif (direction == "up"):
            aim -= mag

    return hor * depth


directions = read_input_to_list("input.txt")
print(calculate_final_position_1(directions))
print(calculate_final_position_2(directions))