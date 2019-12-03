def do_operation(position, opcode, data_array):
    opcode = int(data_array[position])
    operand_1, operand_2, result_slot = int(data_array[position+1]), int(data_array[position+2]), int(data_array[position+3])
    if opcode == 1:
        data_array[result_slot] = int(data_array[operand_1]) + int(data_array[operand_2])
    elif opcode == 2:
        data_array[result_slot] = int(data_array[operand_1]) * int(data_array[operand_2])
    return position+4 , opcode, data_array

def load_memory() :
    with open("2.in","r") as infile :
        code_data = infile.readline().split(",")
    infile.close()
    return code_data

def run_program(noun,verb) :
    
    position = 0
    opcode = None
    code_data= load_memory()
    code_data[1], code_data[2] = noun, verb

    while opcode != 99 :
        position, opcode, code_data = do_operation(position,opcode,code_data)
    return code_data[0]

goal = 19690720
for noun in range(100) :
    for verb in range(100) :
        calc = run_program(noun,verb)
        if calc == goal :
            print(noun)
            print(verb)
            exit()