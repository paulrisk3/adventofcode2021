rotated_array = []

with open("input/day3_input.txt") as file:
    iter_1 = 0
    rotated_array = []
    while (line := file.readline().rstrip()):
        iter_2 = 0
        line_array = []
        for char in line:
            print(iter_1, iter_2)
            line_array.append(int(char))
            iter_2 += 1
        rotated_array.append(line_array)
        iter_1 += 1
    
print(rotated_array)