from base64 import b64encode
import string
import sys

def string_to_hex(hex_string):
    return hex(int(hex_string, 16))

def hex_to_base64(hex_str: str):
    print("Input: " + hex_str)

    base64_str = b64encode(bytes.fromhex(hex_str)).decode("utf-8")

    print("Output: " + base64_str)

    return base64_str


if __name__ == '__main__':
    input_file = sys.argv[1]

    with open(input_file) as file:
        hex_str = file.readlines()
        hex_str = hex_str[0].rstrip()

    hex_to_base64(hex_str)

