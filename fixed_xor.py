import sys
from hex_to_base64 import hex_to_base64, string_to_hex

EXPECTED_OUTPUT = "746865206b696420646f6e277420706c6179"

def fixed_or(input_1, input_2):
    #input_1 = string_to_hex(input_1) 
    #input_2 = string_to_hex(input_2)
    
    print("Input 1: \t" + input_1)
    print("Input 2: \t" + input_2)
    
    output = hex(int(input_1, 16) ^ int(input_2, 16))
    output = output[2:]
    print("Output: \t" + output)

    return output

if __name__ == '__main__':
    input_file = sys.argv[1]

    with open(input_file) as file:
        lines = [line.strip() for line in file]

    result = fixed_or(lines[0], lines[1]) 
    if result == EXPECTED_OUTPUT:
        print("They match, good job!")
    else:
        print("Something went wrong...")
    

