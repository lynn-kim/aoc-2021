def read_input_to_list(path):
    lines = []
    with open(path) as file:
        for line in file:
            lines.append(line.strip())

    return lines


def error_score(lines):
    points = 0
    for line in lines:
        stack = []
        for p in line:
            if p in "([<{":
                stack.append(p)
            else:
                end = stack.pop()
                if p == ")" and end != "(":
                    points += 3
                    break
                elif p == "]" and end != "[":
                    points += 57
                    break
                elif p == "}" and end != "{":
                    points += 1197
                    break
                elif p == ">" and end != "<":
                    points += 25137
                    break

    return points


def auto_complete_score(lines):

    scores = []
    for line in lines:
        stack = []
        score = 0

        for p in line:
            if p in "([<{":
                stack.append(p)

            elif len(stack) == 0:
                break

            else:
                end = stack.pop()
                if (p == ")" and end != "(") or (p == "]" and end != "[") or (
                        p == "}" and end != "{") or (p == ">" and end != "<"):
                    stack = []
                    break

        for p in reversed(stack):
            score *= 5
            if p == "(":
                score += 1
            if p == "[":
                score += 2
            if p == "{":
                score += 3
            if p == "<":
                score += 4

        if score:
            scores.append(score)

    scores.sort()
    return scores[int(len(scores) / 2)]


def main():
    inputs = read_input_to_list('input.txt')
    print(auto_complete_score(inputs))
    return


main()
