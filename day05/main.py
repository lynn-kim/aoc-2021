def read_input_to_list(path):
    lines = []
    with open(path) as file:
        for line in file:
            lines.append(line.rstrip())
    return lines

# x1,y1 -> x2,y2
def get_coords(lines):
  # split by "->"
  coords = []
  for line in lines:
    c = line.strip().split(" -> ")
    coords.append(c)
  
  return coords
    

def get_overlap(coords):
  dict_map = {} # ["x1,y1" = ]
  overlaps = 0
  for c in coords:
    # c = [[252,644], [491,644]]
    c[0].split(",")[0]
   
    x1 = int(c[0].split(",")[0])
    y1 = int(c[0].split(",")[1])
    x2 = int(c[1].split(",")[0])
    y2 = int(c[1].split(",")[1])
 
    
    if c[1] in dict_map:
      if (dict_map[c[1]] == 1): 
        overlaps += 1    
      dict_map[c[1]] += 1 
    else:
      dict_map[c[1]] = 1
    
    while (x1 != x2 or y1 != y2):
      if f"{x1},{y1}" in dict_map:
        if (dict_map[f"{x1},{y1}"] == 1):

          overlaps += 1
        dict_map[f"{x1},{y1}"] += 1
      else:
        dict_map[f"{x1},{y1}"] = 1
      if (y1 > y2):
        y1 -= 1
      if (y2 > y1):
        y1 += 1
      if (x1 > x2):
        x1 -= 1
      if (x2 > x1):
        x1 += 1

  return overlaps


def main():
  inputs = read_input_to_list('input.txt')
  coords = get_coords(inputs)
  print(get_overlap(coords))
  return


main()