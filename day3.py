def remove_non_matches(arr, match):
    enum_arr = enumerate(arr)
    
    # remote non-matches
    for idx, item in enum_arr:
        if item[0] != match[0]:
            arr.pop(idx)
    print(match[0], len(arr), arr, "\n")

    # if more than one result, do it again
    if len(arr) > 1 and len(match) > 1:
        remove_non_matches(arr, match[1:])
        
    return arr

with open("input/day3_input.txt") as file:
    initial_array = []
    rotated_array = []

    for i in file.readline().rstrip():
        rotated_array.append([])

    while (line := file.readline().rstrip()):
        initial_array.append(line)
        iter = 0
        line_array = []
        for char in line:
            rotated_array[iter].append(int(char))
            iter += 1
    
gamma = ''
epsilon = ''

# build binary string
for j in rotated_array:
    if sum(j)/(len(j)+1) < .5:
        gamma += '0'
        epsilon += '1'
    else:
        gamma += '1'
        epsilon += '0'

# print(initial_array)

print("Gamma", gamma, int(gamma, 2))
print("Epsilon", epsilon, int(epsilon,2 ))

results = remove_non_matches(initial_array, '011010111101')
# print("Results", results)