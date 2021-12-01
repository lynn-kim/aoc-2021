def read_input_to_list(path):
    lines = []
    with open(path) as file:
        for line in file:
            lines.append(int(line.rstrip()))
    return lines

def get_number_of_increases_1(input_list):
    total_increases = 0
    for i in range(1, len(input_list)):
        if input_list[i] > input_list[i-1]:
            total_increases += 1

    return total_increases

def get_number_of_increases_2(input_list):
    total_increases = 0
    prev_sum = input_list[0] + input_list[1] + input_list[2] 
    for i in range(0, len(input_list)):
        new_sum = prev_sum - input_list[i] 
        if (i + 3 < len(input_list)):
          new_sum += input_list[i + 3]
        if (new_sum > prev_sum):
          total_increases += 1
        prev_sum = new_sum

    return total_increases

def main():
    input_list = read_input_to_list("input.txt")
    output_1 = get_number_of_increases_1(input_list)
    output_2 = get_number_of_increases_2(input_list)
    print(output_1, output_2)
    return
    
main()