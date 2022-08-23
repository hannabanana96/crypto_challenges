from base64 import b64encode
import string
import sys
from binascii import unhexlify

INPUT = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
OUTPUT = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"

def string_to_hex(hex_string):
    return hex(int(hex_string, 16))

def hex_to_base64(hex_str: str):
    print("Input: " + hex_str)

    base64_str = b64encode(bytes.fromhex(hex_str)).decode("utf-8")

    print("Output: " + base64_str)

    return base64_str


if __name__ == '__main__':

    # Gets the raw binary data
    bytes_data = unhexlify(INPUT)

    # The .decode just gets rid of the b" at the beginning
    b64_string = b64encode(bytes_data).decode("utf-8")

    if b64_string == OUTPUT:
        print("You did it!")
    else:
        print("Failure is unacceptable")


