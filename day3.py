def remove_non_matches(arr, match, counter = 0):
    arr = list(filter(lambda item: item[counter] == match[0], arr))

    # if more than one result in the array, do it again.
    if len(arr) > 1 and len(match) > 1:
        arr = list(filter(lambda item: item[counter] == match[0], arr))
        counter += 1
        remove_non_matches(arr, match[1:], counter)
    else:
        print("We've stopped.", arr)
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

o2_results = remove_non_matches(gamma_array, gamma)
co2_results = remove_non_matches(epsilon_array, epsilon)
# results = remove_non_matches(test_array, '10000111')
# print("Results:", results)
print("O2 Results:", o2_results)
print("CO2 Results:", co2_results)