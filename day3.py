def rotate_array(arr):
    rotated_arr = []

    for i in arr[0]:
        rotated_arr.append([])
    
    for item in arr:
        iter = 0
        for char in item:
            rotated_arr[iter].append(int(char))
            iter += 1
    
    return rotated_arr

def remove_non_matches(arr, match, counter = 0):
    rotated_arr = rotate_array(arr)
    # Find the filter by rotating the array and finding the most common number in the first bit.
    # I think the 0 needs to be counter, instead.
    if sum(rotated_arr[0])/len(rotated_arr[0]) > .5:
        o2_filter = 1
        co2_filter = 0
    else:
        o2_filter = 0
        co2_filter = 1
    arr = list(filter(lambda item: item[counter] == o2_filter, arr))

    # if more than one result in the array, do it again.
    if len(arr) > 1 and len(match) > 1:
        # uh oh. I probably shouldn't run this line twice in my recurisve function. That's not right.
        arr = list(filter(lambda item: item[counter] == o2_filter, arr))
        counter += 1
        remove_non_matches(arr, match[1:], counter)
    else:
        print("We've stopped.", arr)
        return arr

with open("input/day3_input.txt") as file:
    initial_array = []
    
    while (line := file.readline().rstrip()):
        initial_array.append(line)

    rotated_array = rotate_array(initial_array)
    
gamma = ''
epsilon = ''

# build binary string
for j in rotated_array:
    print(sum(j)/(len(j)))
    if sum(j)/(len(j)) < .5:
        gamma += '0'
        epsilon += '1'
    else:
        gamma += '1'
        epsilon += '0'

# print(initial_array)

print("Gamma", gamma, int(gamma, 2))
print("Epsilon", epsilon, int(epsilon,2 ))

# gamma_array = initial_array
# epsilon_array = initial_array

test_array = [
    '00010001',
    '11001111',
    '01100010',
    '00110110',
    '01110000',
    '10110101',
    '10111101',
    '01101000',
    '01010100',
    '10000111'
]

# So, we can't filter just by gamma. The first bit in gamma is correct, but after that,
# we need to recalculate. How do I calculate recursively...
# Do I need to rotate the newly-filtered array each time? I say yes.
# o2_results = remove_non_matches(gamma_array, rotated_array)
# co2_results = remove_non_matches(epsilon_array, rotated_array)
# # results = remove_non_matches(test_array, '10000111')
# # print("Results:", results)
# print("O2 Results:", o2_results)
# print("CO2 Results:", co2_results)