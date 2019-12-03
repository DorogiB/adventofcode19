def make_coordinate_line(pos_x, pos_y, direction, distance, result) :
    for i in range(int(distance)):
        if direction == "L" :
            pos_x -= 1
        elif direction == "U" :
            pos_y += 1
        elif direction == "R" :
            pos_x += 1
        elif direction == "D" :
            pos_y -= 1
        result.append((pos_x,pos_y))
    return pos_x, pos_y, result
    

def trace_line(instructional_desc) :
    pos_x, pos_y = 0, 0
    result = []
    for instruction in instructional_desc :
        instruction = instruction.strip()
        direction = instruction[0]
        distance = instruction[1:]
        pos_x, pos_y, result = make_coordinate_line(pos_x, pos_y, direction, distance, result)
    return result

def get_distance(coordinate) :
    return abs(coordinate[0]) + abs(coordinate[1])

with open("3.in", "r") as infile :
    wire_data_1 = infile.readline().split(",")
    wire_data_2 = infile.readline().split(",")
infile.close()

line_coords_1, line_coords_2 = trace_line(wire_data_1), trace_line(wire_data_2)
intersections = set(line_coords_1).intersection(set(line_coords_2))

steps = set()
for intersection in intersections :
    steps.add(line_coords_1.index(intersection)+1 + line_coords_2.index(intersection)+1)

print(min(steps))
