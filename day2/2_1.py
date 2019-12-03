def do_operation(position, opcode, data_array):
    opcode = int(data_array[position])
    operand_1, operand_2, result_slot = int(data_array[position+1]), int(data_array[position+2]), int(data_array[position+3])
    if opcode == 1:
        data_array[result_slot] = int(data_array[operand_1]) + int(data_array[operand_2])
    elif opcode == 2:
        data_array[result_slot] = int(data_array[operand_1]) * int(data_array[operand_2])
    return position+4 , opcode, data_array

with open("2.in","r") as infile :
    code_data = infile.readline().split(",")
infile.close()

position = 0
opcode = None

while opcode != 99 :
    position, opcode, code_data = do_operation(position,opcode,code_data)
print(code_data[0])

