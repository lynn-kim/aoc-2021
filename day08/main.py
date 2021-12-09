def read_input_to_list(path):
    lines = []
    with open(path) as file:
        for line in file:
            lines.append(line.rstrip())

    return lines


def split_line_to_array(line):

    signals, code = line.split(" | ")
    signals = signals.split(" ")
    code = code.split(" ")

    return [signals, code]


def get_letter_count(line):
    letter_count = {}
    for signal in line:
        for letter in signal:
            if letter in letter_count:
                letter_count[letter] += 1
            else:
                letter_count[letter] = 1
    return letter_count


def get_code(line):

    decoded = {}
    letter_count = get_letter_count(line[0])

    for letter in letter_count:
        if letter_count[letter] == 9:
            decoded[letter] = "f"
        elif letter_count[letter] == 4:
            decoded[letter] = "e"
        elif letter_count[letter] == 6:
            decoded[letter] = "b"

    for signal in line[0]:
        if len(signal) == 2:
            if signal[0] in decoded:
                decoded[signal[1]] = "c"
            else:
                decoded[signal[0]] = "c"
            break

    for signal in line[0]:
        if len(signal) == 3:
            if signal[0] not in decoded:
                decoded[signal[0]] = "a"
            elif signal[1] not in decoded:
                decoded[signal[1]] = "a"
            else:
                decoded[signal[2]] = "a"
            break

    for signal in line[0]:
        if len(signal) == 4:
            for letter in signal:
                if letter not in decoded:
                    decoded[letter] = "d"
            break

    for signal in line[0]:
        for letter in signal:
            if letter not in decoded:
                decoded[letter] = "g"
                break

    return decoded


def decode(lines):
    total = 0
    for line in lines:
        cur = 0
        line = split_line_to_array(line)
        m = get_code(line)

        for n in line[1]:
            print(n)
            cur *= 10
            if len(n) == 2:
                cur += 1
            elif len(n) == 4:
                cur += 4
            elif len(n) == 3:
                cur += 7
            elif len(n) == 7:
                cur += 8
            else:
                temp = ""
                for letter in n:
                    temp += m[letter]
                temp = sorted(temp)
                temp = "".join(temp)

                if temp == "acdeg":
                    cur += 2
                elif temp == "acdfg":
                    cur += 3
                elif temp == "abdfg":
                    cur += 5
                elif temp == "abdefg":
                    cur += 6
                elif temp == "abcdfg":
                    cur += 9
        total += cur
    return total


def main():
    inputs = read_input_to_list('input.txt')
    print(decode(inputs))
    return


main()
