input_file = open('day2_input.txt', 'r')
directions = [str(line).strip().split(" ") for line in input_file]

horizontal_motion = []
depth_motion = []

horizontal_position = 0
depth = 0
aim = 0

for direction in directions:
  if direction[0] == "forward":
    horizontal_motion.append(int(direction[1]))
    horizontal_position += int(direction[1])
    depth += (int(direction[1]) * aim)
  elif direction[0] == "down":
    depth_motion.append(int(direction[1]))
    aim += int(direction[1])
  elif direction[0] == "up":
    depth_motion.append(int(direction[1]) * -1)
    aim -= int(direction[1])

print("Horizontal Position: " + str(sum(horizontal_motion)))
print("Final Depth: " + str(sum(depth_motion)))
print("-----Recalculating-----")
print("Horizontal Position: " + str(horizontal_position))
print("Final Depth: " + str(depth))