def remove_non_matches(arr, match, count = 0):
    print(match, arr)
    # filter and remove non-matches
    for item in arr:
        if item[count] != match[0]:
            arr.remove(item)

    # if more than one result in the array, do it again
    if len(arr) > 1 and len(match) > 1:
        print("Run it again.")
        count += 1
        remove_non_matches(arr, match[1:], count)

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

gamma_array = initial_array
epsilon_array = initial_array

test_array = [
    '000100011010',
    '110011110110',
    '011000101111',
    '001101100101',
    '011100001000',
    '101101011011',
    '101111010101',
    '011010000101',
    '010101000010',
    '100001111000'
]

# o2_results = remove_non_matches(gamma_array, gamma)
# print("O2 Rating:", o2_results)
# print(gamma_array)
# co2_results = remove_non_matches(epsilon_array, epsilon)
# print("CO2 Rating:", co2_results)
results = remove_non_matches(test_array, '10000111')
print(results)