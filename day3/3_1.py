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
        result.add((pos_x,pos_y))
    return pos_x, pos_y, result
    

def trace_line(instructional_desc) :
    pos_x, pos_y = 0, 0
    result = set()
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

intersections = trace_line(wire_data_1).intersection(trace_line(wire_data_2))
print(min(set(map(get_distance,intersections))))
