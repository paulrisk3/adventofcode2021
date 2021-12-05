with open("input/day3_input.txt") as file:
    rotated_array = []

    for i in file.readline().rstrip():
            rotated_array.append([])

    while (line := file.readline().rstrip()):
        iter = 0
        line_array = []
        for char in line:
            rotated_array[iter].append(int(char))
            iter += 1
    
gamma = ''
epsilon = ''

# build binary string
for j in rotated_array:
    if sum(j)/len(j) < .5:
        gamma += '0'
        epsilon += '1'
    else:
        gamma += '1'
        epsilon += '0'

print("Gamma:", int(gamma, 2))
print("Epsilon:", int(epsilon,2 ))