def read_input_to_list(path):
    lines = []
    with open(path) as file:
        for line in file:
            lines.append(line.rstrip())
    return lines


def get_common_digits(numbers):
  gamma = [0 for i in range(len(numbers[0]))]
  for num in numbers:
    for i in range(len(num)):
      gamma[i] += int(num[i])

  gamma_string = ""
  for i in range(len(gamma)):
    if (gamma[i] >= ( len(numbers)/2) ):
      gamma_string += "1"
    else:
      gamma_string += "0"

  
  return gamma_string


def co2_support_rating(numbers):

  most_common = get_common_digits(numbers)

  for i in range(len(most_common)):
    j = 0
    while(j < len(numbers)):
      num = numbers[j]
      if (num[i] == most_common[i] and most_common[i] != "2"):
        numbers.remove(num)
      else:
        j += 1
      if (len(numbers) == 1):
        return int(numbers[0], 2)
    most_common = get_common_digits(numbers)
  return numbers


def oxygen_support_rating(numbers):

  most_common = get_common_digits(numbers)

  for i in range(len(most_common)):
    j = 0
    while(j < len(numbers)):
      num = numbers[j]
      if (num[i] != most_common[i] and most_common[i] != "2"):
        numbers.remove(num)
      else:
        j += 1
      if (len(numbers) == 1):
        return int(numbers[0], 2)
    most_common = get_common_digits(numbers)
  return numbers


def life_support_rating(numbers):

  return oxygen_support_rating(read_input_to_list('input.txt')) * co2_support_rating(read_input_to_list('input.txt'))



def main():
  numbers = read_input_to_list('input.txt')
  print(life_support_rating(numbers))
  return


main()