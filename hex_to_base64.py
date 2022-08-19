from base64 import b64encode
import sys

def hex_to_base64(hex_str: str):
    print("Input: " + hex_str)

    base64_str = b64encode(bytes.fromhex(hex_str)).decode("utf-8")
    print(base64_str)


if __name__ == '__main__':
    input_file = sys.argv[1]

    with open(input_file) as file:
        hex_str = file.readlines()
        hex_str = hex_str[0].rstrip()

    hex_to_base64(hex_str)

