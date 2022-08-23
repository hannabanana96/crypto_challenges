import sys
from hex_to_base64 import hex_to_base64, string_to_hex
from binascii import unhexlify, b2a_hex
from base64 import b64encode

INPUT_1 = "1c0111001f010100061a024b53535009181c"
INPUT_2 = "686974207468652062756c6c277320657965"
EXPECTED_OUTPUT = "746865206b696420646f6e277420706c6179"

def fixed_or(input_1, input_2):
    
    print(INPUT_1)
    print(INPUT_2)
    print("Input 1: \t" + input_1)
    print("Input 2: \t" + input_2)

    input_1 = unhexlify(INPUT_1)
    input_2 = unhexlify(INPUT_2)
    print(input_1)
    print(input_2)
    

    output = bytes([a ^ b for a,b in zip(input_1, input_2)])
    print(output)
    output = b2a_hex(output).decode()
    print(output)

    return output

if __name__ == '__main__':

    result = fixed_or(INPUT_1, INPUT_2) 
    if result == EXPECTED_OUTPUT:
        print("They match, good job!")
    else:
        print("Something went wrong...")
