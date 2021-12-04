count = 0
window_count = 0

input_file = open('day1_input.txt', 'r')
depths = [int(line) for line in input_file]

for first, second in zip(depths, depths[1:]):
	if second > first:
		count += 1
print("count: " + str(count))

for x in range(len(depths) - 3):
	window1 = sum(depths[x:x+3])
	window2 = sum(depths[x+1:x+4])
	if(window2 > window1):
		window_count += 1
print("window_count: " + str(window_count))
